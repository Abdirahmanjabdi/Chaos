#!/usr/bin/env python3
"""check_links - verify every external link in the curriculum and the root docs.

A dead link on the morning card is friction, and the whole system is built to remove friction. Run this every
few months (and after editing a curriculum) to catch link rot before `today` opens a 404.

    python tools/check_links.py              check everything; list anything that isn't plain OK
    python tools/check_links.py -v           also list the OK links
    python tools/check_links.py FILE ...     check only these markdown files

Each unique URL is requested once (HEAD, falling back to GET), redirects are followed, and requests to the same
host are spaced out. Results:

    ok            2xx, no redirect (or only a trivial one, e.g. a trailing slash)
    redirected    reachable, but via a redirect - permanent ones (301/308) should be updated to the final URL
    unverifiable  the site blocks bots or needs JavaScript (401/403/429/999, bot challenges) - check by hand
    broken        4xx/5xx, DNS failure, timeout - fix these

Exits non-zero if anything is broken. Standard library only (Python 3.11+).
"""

from __future__ import annotations

import argparse
import re
import socket
import ssl
import sys
import threading
import time
import urllib.error
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urldefrag, urlsplit

ROOT = Path(__file__).resolve().parent.parent
ROOT_DOCS = ("README.md", "START-HERE.md", "HABITS.md", "SYSTEM.md", "OPERATIONS.md", "CURRICULUM.md")

LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")  # the same pattern tools/today.py uses
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)
HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-GB,en;q=0.9",
}
TIMEOUT = 15
HOST_DELAY = 1.0  # seconds between requests to the same host
RETRY_DELAY = 5.0  # seconds before retrying a transient failure
WORKERS = 8  # hosts checked in parallel
BLOCKED_CODES = {401, 403, 429, 999}  # 999 is LinkedIn's "no bots"
CHALLENGE_MARKERS = ("Just a moment...", "cf-chl", "challenge-platform", "Attention Required!", "captcha")


@dataclass
class Link:
    file: str
    line: int
    label: str
    url: str


@dataclass
class Result:
    status: str  # ok | redirected | unverifiable | broken
    detail: str = ""
    final: str = ""
    permanent: bool = False
    chain: list[int] = field(default_factory=list)


class Recorder(urllib.request.HTTPRedirectHandler):
    """Follows redirects like the default handler, but remembers each hop's status code."""

    def __init__(self) -> None:
        self.codes: list[int] = []

    def redirect_request(self, req, fp, code, msg, headers, newurl):  # type: ignore[override]
        self.codes.append(code)
        new = super().redirect_request(req, fp, code, msg, headers, newurl)
        if new is not None:
            new.method = req.get_method()  # keep HEAD as HEAD across hops
        return new


def extract(paths: list[Path]) -> list[Link]:
    links = []
    for path in paths:
        rel = path.relative_to(ROOT).as_posix()
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            links += [Link(rel, number, m.group(1), m.group(2)) for m in LINK_RE.finditer(line)]
    return [link for link in links if "." in urlsplit(link.url).netloc.strip(".")]  # skip "https://..." examples


def default_files() -> list[Path]:
    docs = [ROOT / name for name in ROOT_DOCS if (ROOT / name).exists()]
    return docs + sorted((ROOT / "tracks").glob("*/curriculum.md"))


def request(url: str, method: str, verify: bool = True) -> tuple[int, str, list[int], str]:
    """One request; returns (status, final url, redirect codes, start of body). Raises on network errors."""
    recorder = Recorder()
    context = ssl.create_default_context() if verify else ssl._create_unverified_context()
    opener = urllib.request.build_opener(recorder, urllib.request.HTTPSHandler(context=context))
    req = urllib.request.Request(url, headers=HEADERS, method=method)
    try:
        with opener.open(req, timeout=TIMEOUT) as resp:
            body = resp.read(65536).decode("utf-8", "replace") if method == "GET" else ""
            return resp.status, resp.geturl(), recorder.codes, body
    except urllib.error.HTTPError as err:
        body = ""
        try:
            body = err.read(65536).decode("utf-8", "replace")
        except Exception:
            pass
        return err.code, err.geturl() or url, recorder.codes, body


def trivial(a: str, b: str) -> bool:
    """True if two URLs differ only by scheme upgrade, a trailing slash or a 'www.'."""

    def norm(u: str) -> str:
        parts = urlsplit(u)
        host = parts.netloc.lower().removeprefix("www.")
        return f"{host}{parts.path.rstrip('/')}?{parts.query}"

    return norm(a) == norm(b)


def check(url: str) -> Result:
    target, fragment = urldefrag(url)
    attempts = []
    note = ""
    for method in ("HEAD", "GET", "GET"):  # the second GET is a retry, for flaky servers (5xx, timeouts)
        if attempts and method == "GET" and len(attempts) == 2:
            if attempts[-1].status != "broken" or attempts[-1].detail.startswith("HTTP 4"):
                break
            time.sleep(RETRY_DELAY)
        try:
            try:
                code, final, chain, body = request(target, method, verify=not note)
            except urllib.error.URLError as err:
                # Python can't fetch missing intermediate certificates the way browsers do; the page may be fine.
                if not isinstance(err.reason, ssl.SSLCertVerificationError):
                    raise
                note = " (TLS chain not verifiable by Python; fine in a browser?)"
                code, final, chain, body = request(target, method, verify=False)
        except ConnectionResetError:  # incl. "remote end closed connection": the usual bot wall for some hosts
            attempts.append(Result("unverifiable", f"{method}: connection dropped - often bot blocking"))
            continue
        except (urllib.error.URLError, socket.timeout, TimeoutError, ConnectionError, ssl.SSLError) as err:
            reason = getattr(err, "reason", err)
            attempts.append(Result("broken", f"{method}: {reason}"))
            continue
        except Exception as err:  # noqa: BLE001 - http.client oddities shouldn't kill the run
            attempts.append(Result("broken", f"{method}: {type(err).__name__}: {err}"))
            continue
        if fragment:
            final = f"{final}#{fragment}"
        permanent = bool(chain) and all(c in (301, 308) for c in chain)
        challenge = any(marker in body for marker in CHALLENGE_MARKERS)
        if 200 <= code < 300:
            moved = bool(chain) and not trivial(url, final)
            status = "redirected" if moved else "ok"
            return Result(status, f"{code}{note}", final if moved else "", permanent, chain)
        if code in BLOCKED_CODES or challenge or (code == 503 and "cloudflare" in body.lower()):
            attempts.append(Result("unverifiable", f"HTTP {code} - blocks bots / needs a browser", final))
            continue
        attempts.append(Result("broken", f"HTTP {code}", final, permanent, chain))
    # GET is the more faithful answer; prefer "unverifiable" over "broken" if either attempt saw a bot wall
    if any(a.status == "unverifiable" for a in attempts):
        return next(a for a in reversed(attempts) if a.status == "unverifiable")
    return attempts[-1]


def check_all(urls: list[str]) -> dict[str, Result]:
    by_host: dict[str, list[str]] = defaultdict(list)
    for url in urls:
        by_host[urlsplit(url).netloc.lower()].append(url)
    results: dict[str, Result] = {}
    lock = threading.Lock()
    done = [0]

    def run_host(host_urls: list[str]) -> None:
        for i, url in enumerate(host_urls):
            if i:
                time.sleep(HOST_DELAY)
            result = check(url)
            with lock:
                results[url] = result
                done[0] += 1
                print(f"\r  checked {done[0]}/{len(urls)}", end="", file=sys.stderr, flush=True)

    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        list(pool.map(run_host, by_host.values()))
    print(file=sys.stderr)
    return results


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check every external link in the curriculum and root docs.")
    parser.add_argument("files", nargs="*", type=Path, help="markdown files to check (default: curricula + root docs)")
    parser.add_argument("-v", "--verbose", action="store_true", help="also list links that are OK")
    args = parser.parse_args(argv)
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[union-attr]

    files = [p.resolve() for p in args.files] or default_files()
    links = extract(files)
    urls = list(dict.fromkeys(link.url for link in links))
    print(f"{len(links)} links ({len(urls)} unique URLs) in {len(files)} files")
    results = check_all(urls)

    where: dict[str, list[Link]] = defaultdict(list)
    for link in links:
        where[link.url].append(link)
    order = ("broken", "unverifiable", "redirected", "ok")
    for status in order:
        group = [u for u in urls if results[u].status == status]
        if status == "ok" and not args.verbose:
            group = [u for u in group if "TLS" in results[u].detail]  # OK, but worth knowing about
        if not group:
            continue
        print(f"\n{status.upper()} ({len(group)})")
        for url in group:
            r = results[url]
            print(f"  {url}")
            if status == "redirected":
                kind = "permanent" if r.permanent else "temporary"
                print(f"    -> {r.final}  ({kind}: {' '.join(map(str, r.chain))})")
            elif r.detail and (status != "ok" or "TLS" in r.detail):
                print(f"    {r.detail}")
            for link in where[url]:
                print(f"    {link.file}:{link.line}  [{link.label}]")

    counts = {s: sum(1 for u in urls if results[u].status == s) for s in order}
    print("\nSummary: " + " · ".join(f"{counts[s]} {s}" for s in order))
    return 1 if counts["broken"] else 0


if __name__ == "__main__":
    sys.exit(main())
