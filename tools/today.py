#!/usr/bin/env python3
"""today - the daily driver for the Chaos learning repo.

One command starts the day; one command closes it. The right action should be the easy action.

    today              today's card: the cue and the exact session(s), hardest first (opens the first link)
    today done         close a block: log it, tick the session, refresh PROGRESS.md, commit and push
    today swap TRACK   study a different track next (it's logged - choosing keeps this enjoyable)
    today more         a bonus block, aimed at your weakest score (or most neglected track)
    today rate         rate your confidence 1-5 per module; weakest-first tracks serve the lowest next
    today job EVENT N  count job-search events: applied, screen, interview, offer, rejected
    today week         this week's review, pre-filled from your logs and KPIs
    today status       the progress and KPI dashboard (also rewrites PROGRESS.md)
    today doctor       check this computer's setup and the curriculum files' format

In a phase with `blocks` (system/config.toml), every day is the same list of blocks, hardest first; otherwise the
weekday schedule picks one track. Standard library only (Python 3.11+). Every number is derived from the markdown -
the curriculum checkboxes, the logs, the ratings - so there is no hidden state to drift between computers. Git is
the sync.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import textwrap
import webbrowser
from dataclasses import dataclass, field
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # Python < 3.11
    try:
        import tomli as tomllib  # type: ignore[no-redef]
    except ModuleNotFoundError:
        sys.exit("today needs Python 3.11+ (or: pip install tomli)")

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "system" / "config.toml"
TRACKS_DIR = ROOT / "tracks"
LOGS_DIR = ROOT / "logs"
WEEKLY_DIR = ROOT / "review" / "weekly"
TEMPLATES_DIR = ROOT / "templates"
PROGRESS_PATH = ROOT / "PROGRESS.md"
STATE_PATH = LOGS_DIR / ".today.json"  # local and git-ignored: today's swap/bonus choice
RATINGS_PATH = LOGS_DIR / "ratings.md"
JOBS_PATH = LOGS_DIR / "job-search.md"
JOB_EVENTS = ("applied", "screen", "interview", "offer", "rejected")

WEEKDAYS = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
WIDTH = 74

MODULE_RE = re.compile(r"^##\s+([A-Z]{1,2}\d{2})\s+[·:—-]\s+(.+?)\s*$")
META_RE = re.compile(r"^<!--\s*(.*?)\s*-->\s*$")
SESSION_RE = re.compile(r"^\s*- \[([ xX])\]\s+([A-Z]{1,2}\d{2}\.S\d{2})\s+[—:-]\s+(.+?)\s*$")
LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")
ENTRY_RE = re.compile(r"^###\s+(\d{4}-\d{2}-\d{2})\s+[·-]\s+Day\s+(\d+)")
FIELD_RE = re.compile(r"^- \*\*(.+?):\*\*\s*(.*)$")
DONE_ON_RE = re.compile(r"\s*\((\d{4}-\d{2}-\d{2})\)\s*$")
LOG_NAME_RE = re.compile(r"^\d{4}-\d{2}\.md$")
SCORE_RE = re.compile(r"^\s*(\d+)\s*/\s*(\d+)\s*$")
DATE_HEAD_RE = re.compile(r"^###\s+(\d{4}-\d{2}-\d{2})")
RATING_RE = re.compile(r"^- ([A-Z]{1,2}\d{2})\b.*:\s*([1-5])\s*$")
JOB_RE = re.compile(r"^- (\d{4}-\d{2}-\d{2})\s+·\s+(\w+)\s+·\s+(\d+)")

# Short nudges in the spirit of the habit design (HABITS.md). Rotated by day number.
NUDGES = (
    "Show up first. Optimise later.",
    "Results lag effort. This is the quiet stretch where it compounds.",
    "Make it small enough that you can't say no - then do a bit more.",
    "One miss is noise. Two is a pattern. Today keeps it noise.",
    "Every session is a vote for the person you're becoming.",
    "Boredom is the real opponent. Show up anyway; make it fun after.",
    "You're not behind. You're early in a long game.",
    "Hard today means easy next year.",
    "Understanding over coverage. Slow is smooth, smooth is fast.",
    "Do the work; the work does the rest.",
)

_TO_ASCII = str.maketrans({
    "—": "-", "–": "-", "−": "-", "·": "|", "’": "'", "‘": "'", "“": '"', "”": '"', "→": "->", "←": "<-",
    "↔": "<->", "…": "...", "×": "x", "≥": ">=", "≤": "<=", "≠": "!=", "√": "sqrt", "²": "^2", "³": "^3",
    "ⁿ": "^n", "ˣ": "^x", "ᵖ": "^p", "⁸": "^8", "½": "1/2", "°": " deg", "ε": "e", "δ": "d", "π": "pi",
    "α": "a", "θ": "theta", "σ": "sigma", "∞": "inf", "∪": "u", "∩": "n", "Ω": "Ohm", "é": "e", "ô": "o",
    "ö": "o", "ü": "u",
})


# ----------------------------------------------------------------------------------------------------- models

@dataclass
class Session:
    sid: str
    text: str
    done: bool
    line: int  # 0-based line index in the curriculum file

    @property
    def done_on(self) -> dt.date | None:
        match = DONE_ON_RE.search(self.text)
        return dt.date.fromisoformat(match.group(1)) if match else None


@dataclass
class Module:
    mid: str
    title: str
    meta: dict[str, str] = field(default_factory=dict)
    goal: str = ""
    resources: list[str] = field(default_factory=list)
    gate: str = ""
    sessions: list[Session] = field(default_factory=list)

    @property
    def done(self) -> bool:
        return bool(self.sessions) and all(s.done for s in self.sessions)

    def next_session(self) -> Session | None:
        return next((s for s in self.sessions if not s.done), None)


@dataclass
class Track:
    key: str
    title: str
    path: Path
    modules: list[Module]
    weakest: bool = False  # served lowest-rated module first, not top to bottom
    rank: dict[str, int] = field(default_factory=dict)  # module id -> your latest confidence rating, 1-5

    @property
    def sessions(self) -> list[Session]:
        return [s for m in self.modules for s in m.sessions]

    def current(self) -> tuple[Module | None, Session | None]:
        """The module to work on, and its next session. Strictly top to bottom - unless the track is weakest-first,
        where a started module is finished first and then the lowest-rated module comes next."""
        modules = self.modules
        if self.weakest:
            started = [m for m in modules if not m.done and any(s.done for s in m.sessions)]
            rest = sorted((m for m in modules if m not in started), key=lambda m: self.rank.get(m.mid, 3))
            modules = started + rest
        for module in modules:
            session = module.next_session()
            if session is not None:
                return module, session
        return None, None

    def percent(self) -> float:
        sessions = self.sessions
        return sum(s.done for s in sessions) / len(sessions) if sessions else 0.0


@dataclass
class Entry:
    date: dt.date
    day: int
    fields: dict[str, str]

    @property
    def track(self) -> str:
        return self.fields.get("Track / topic", "").split(" ")[0].strip()

    @property
    def minutes(self) -> int:
        match = re.match(r"\d+", self.fields.get("Block (min)", ""))
        return int(match.group()) if match else 0

    @property
    def finished(self) -> bool:
        return "(in progress)" not in self.fields.get("Track / topic", "")

    @property
    def score(self) -> tuple[int, int] | None:
        match = SCORE_RE.match(self.fields.get("Score", ""))
        return (int(match.group(1)), int(match.group(2))) if match and int(match.group(2)) > 0 else None


@dataclass
class Kpi:
    label: str
    now: float | None
    before: float | None
    target: float | None = None
    kind: str = "n"  # n (count) | h (hours) | pct

    def show(self, value: float | None) -> str:
        if value is None:
            return "-"
        return f"{value:.0%}" if self.kind == "pct" else f"{value:.1f}" if self.kind == "h" else f"{value:g}"

    @property
    def met(self) -> bool | None:
        return None if self.target is None else (self.now or 0) >= self.target

    @property
    def trend(self) -> str:
        if self.now is None or self.before is None or self.now == self.before:
            return "="
        return "up" if self.now > self.before else "down"


@dataclass
class Stats:
    days: int
    current: int
    longest: int
    resilient: int
    hours: float
    last: dt.date | None
    gap: int | None  # days since the last study day (1 = studied yesterday)
    today_done: bool


# ----------------------------------------------------------------------------------------------------- files

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        sys.exit(f"Missing {CONFIG_PATH.relative_to(ROOT)} - the settings file `today` needs.")
    with CONFIG_PATH.open("rb") as fh:
        return tomllib.load(fh)


def study_day(cfg: dict, now: dt.datetime | None = None) -> dt.date:
    """The day a block belongs to: closing at 00:30 after a late-night block still counts for the night before."""
    hours, _, minutes = str(cfg.get("habit", {}).get("day_starts", "00:00")).partition(":")
    now = now or dt.datetime.now()
    return (now - dt.timedelta(hours=int(hours), minutes=int(minutes or 0))).date()


def parse_track(path: Path) -> Track:
    lines = read(path).splitlines()
    title = next((line[2:].strip() for line in lines if line.startswith("# ")), path.parent.name)
    modules: list[Module] = []
    current: Module | None = None
    section: str | None = None
    for index, raw in enumerate(lines):
        line = raw.rstrip()
        heading = MODULE_RE.match(line)
        if heading:
            current = Module(heading.group(1), heading.group(2))
            modules.append(current)
            section = None
            continue
        if current is None:
            continue
        if line.startswith("## "):  # a non-module H2 closes the module
            current, section = None, None
            continue
        meta = META_RE.match(line)
        if meta and not current.meta:
            for part in meta.group(1).split("|"):
                if ":" in part:
                    key, value = part.split(":", 1)
                    current.meta[key.strip().lower()] = value.strip()
            continue
        if line.startswith("**Goal:**"):
            current.goal, section = line[len("**Goal:**"):].strip(), None
            continue
        if line.startswith("**Gate artifact:**"):
            current.gate, section = line[len("**Gate artifact:**"):].strip(), None
            continue
        if line.startswith("**Resources:**"):
            section = "resources"
            continue
        if line.startswith("**"):
            section = None
        session = SESSION_RE.match(line)
        if session:
            current.sessions.append(Session(session.group(2), session.group(3), session.group(1).lower() == "x", index))
            continue
        if section == "resources" and line.lstrip().startswith("- "):
            current.resources.append(line.lstrip()[2:].strip())
    return Track(path.parent.name, title, path, modules)


def load_tracks(cfg: dict) -> dict[str, Track]:
    found = {p.parent.name: p for p in sorted(TRACKS_DIR.glob("*/curriculum.md"))}
    order = [k for k in cfg.get("tracks", {}).get("order", []) if k in found]
    order += [k for k in found if k not in order]
    tracks = {k: parse_track(found[k]) for k in order}
    ratings = latest_ratings(parse_ratings())
    for key in cfg.get("tracks", {}).get("weakest_first", []):
        if key in tracks:
            tracks[key].weakest = True
            tracks[key].rank = {m.mid: ratings[m.mid] for m in tracks[key].modules if m.mid in ratings}
    return tracks


def get_track(tracks: dict[str, Track], key: str) -> Track:
    if key not in tracks:
        sys.exit(f"Unknown track '{key}'. Tracks: {', '.join(tracks)}")
    return tracks[key]


def parse_logs() -> list[Entry]:
    entries: list[Entry] = []
    if not LOGS_DIR.exists():
        return entries
    for path in sorted(LOGS_DIR.glob("*.md")):
        if not LOG_NAME_RE.match(path.name):
            continue
        current: Entry | None = None
        for line in read(path).splitlines():
            heading = ENTRY_RE.match(line)
            if heading:
                day = int(heading.group(2))
                current = Entry(dt.date.fromisoformat(heading.group(1)), day, {}) if day >= 1 else None
                if current is not None:
                    entries.append(current)
                continue
            if current is not None:
                field_match = FIELD_RE.match(line)
                if field_match:
                    current.fields[field_match.group(1)] = field_match.group(2).strip()
    return entries


def parse_ratings() -> dict[str, list[tuple[dt.date, int]]]:
    """logs/ratings.md, written by `today rate`: a dated heading, then one `- MID Title: N` line per module."""
    history: dict[str, list[tuple[dt.date, int]]] = {}
    if not RATINGS_PATH.exists():
        return history
    current: dt.date | None = None
    for line in read(RATINGS_PATH).splitlines():
        heading = DATE_HEAD_RE.match(line)
        if heading:
            current = dt.date.fromisoformat(heading.group(1))
            continue
        rating = RATING_RE.match(line)
        if rating and current is not None:
            history.setdefault(rating.group(1), []).append((current, int(rating.group(2))))
    return history


def latest_ratings(history: dict[str, list[tuple[dt.date, int]]]) -> dict[str, int]:
    return {mid: sorted(points, key=lambda p: p[0])[-1][1] for mid, points in history.items() if points}


def parse_jobs() -> list[tuple[dt.date, str, int]]:
    """logs/job-search.md, written by `today job`: `- YYYY-MM-DD · event · count`. Counts only - the repo is public."""
    if not JOBS_PATH.exists():
        return []
    return [(dt.date.fromisoformat(m.group(1)), m.group(2), int(m.group(3)))
            for m in map(JOB_RE.match, read(JOBS_PATH).splitlines()) if m]


def stats(entries: list[Entry], today: dt.date) -> Stats:
    dates = sorted({e.date for e in entries if e.date <= today})
    hours = sum(e.minutes for e in entries) / 60
    if not dates:
        return Stats(0, 0, 0, 0, hours, None, None, False)
    longest = run = 1
    for earlier, later in zip(dates, dates[1:]):
        run = run + 1 if (later - earlier).days == 1 else 1
        longest = max(longest, run)
    last = dates[-1]
    gap = (today - last).days
    current = 0
    if gap <= 1:  # alive if you studied today or yesterday
        day, have = last, set(dates)
        while day in have:
            current += 1
            day -= dt.timedelta(days=1)
    resilient = 0
    if gap <= 2:  # "never miss twice": consecutive study days allowing single-day gaps, measured in calendar days
        start = last
        for earlier, later in zip(reversed(dates[:-1]), reversed(dates[1:])):
            if (later - earlier).days <= 2:
                start = earlier
            else:
                break
        resilient = (last - start).days + 1
    return Stats(len(dates), current, longest, resilient, hours, last, gap, last == today)


# ----------------------------------------------------------------------------------------------------- state & schedule

def read_state(day: dt.date) -> dict:
    try:
        state = json.loads(read(STATE_PATH))
    except (OSError, ValueError):
        return {}
    return state if state.get("date") == day.isoformat() else {}


def write_state(day: dt.date, **values: str) -> None:
    write(STATE_PATH, json.dumps({"date": day.isoformat(), **values}))


def clear_state() -> None:
    try:
        STATE_PATH.unlink()
    except OSError:
        pass


def scheduled(cfg: dict, day: dt.date) -> str:
    slot = cfg.get("schedule", {}).get(WEEKDAYS[day.weekday()], "math")
    if isinstance(slot, list):
        return slot[day.isocalendar()[1] % len(slot)] if slot else "math"
    return slot


def phase(cfg: dict) -> tuple[str, dict]:
    """The active phase's name and settings; settings are empty when the phase has no daily blocks."""
    name = str(cfg.get("phase", {}).get("current", ""))
    settings = cfg.get("phase", {}).get(name, {})
    return name, settings if isinstance(settings, dict) and settings.get("blocks") else {}


def blocks(cfg: dict) -> list[tuple[str, int]]:
    """The phase's daily blocks as (track, minutes), hardest first. Empty means: use the weekday schedule."""
    default = int(cfg.get("habit", {}).get("block_minutes", 75))
    return [(str(b["track"]), int(b.get("minutes", default))) for b in phase(cfg)[1].get("blocks", [])]


def block_minutes(cfg: dict, key: str) -> int:
    return dict(blocks(cfg)).get(key, int(cfg.get("habit", {}).get("block_minutes", 75)))


def day_plan(cfg: dict, day: dt.date, entries: list[Entry]) -> list[tuple[str, int, bool]]:
    """Today's blocks as (track, minutes, done); a block is done once a log entry for its track exists today."""
    logged: dict[str, int] = {}
    for e in entries:
        if e.date == day:
            logged[e.track] = logged.get(e.track, 0) + 1
    plan = []
    for key, minutes in blocks(cfg):
        done = logged.get(key, 0) > 0
        if done:
            logged[key] -= 1
        plan.append((key, minutes, done))
    return plan


def score_rate(entries: list[Entry], key: str, start: dt.date, end: dt.date) -> float | None:
    hit = asked = 0
    for e in entries:
        if e.track == key and start <= e.date <= end and e.score:
            hit, asked = hit + e.score[0], asked + e.score[1]
    return hit / asked if asked else None


def weakest_block(cfg: dict, entries: list[Entry], day: dt.date) -> str:
    """The phase track with the lowest score over the last 7 days (unscored counts as 0) - where a bonus pays most."""
    keys = [k for k, _ in blocks(cfg)]
    start = day - dt.timedelta(days=6)
    return min(keys, key=lambda k: (score_rate(entries, k, start, day) or 0.0, keys.index(k)))


def choose_track(cfg: dict, day: dt.date, override: str | None = None,
                 entries: list[Entry] | None = None) -> tuple[str, str]:
    if override:
        return override, "your choice"
    state = read_state(day)
    if state.get("track"):
        return state["track"], state.get("why", "your choice")
    if blocks(cfg):
        entries = parse_logs() if entries is None else entries
        plan = day_plan(cfg, day, entries)
        for index, (key, _, done) in enumerate(plan, 1):
            if not done:
                return key, f"block {index} of {len(plan)}"
        return weakest_block(cfg, entries, day), "bonus - your lowest score this week"
    return scheduled(cfg, day), "scheduled"


# ----------------------------------------------------------------------------------------------------- text helpers

def plain(text: str) -> str:
    """Markdown -> console text: links become their labels, emphasis is dropped, symbols become ASCII."""
    text = LINK_RE.sub(lambda m: m.group(1), text)
    text = DONE_ON_RE.sub("", text.replace("**", "").replace("`", ""))
    return text.translate(_TO_ASCII)


def links_in(text: str) -> list[str]:
    return [m.group(2) for m in LINK_RE.finditer(text)]


def wrap(text: str, indent: str = "  ", hang: str | None = None) -> list[str]:
    return textwrap.wrap(plain(text), WIDTH, initial_indent=indent,
                         subsequent_indent=indent if hang is None else hang) or [indent]


def labelled(label: str, value: str) -> list[str]:
    head = f"  {label:<8}"
    return wrap(value, head, " " * len(head))


def bullet(value: str) -> list[str]:
    return wrap(value, "    - ", "      ")


def cell(text: str, limit: int = 90) -> str:
    text = DONE_ON_RE.sub("", LINK_RE.sub(lambda m: m.group(1), text)).replace("|", "/").strip()
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def bar(fraction: float, width: int = 10) -> str:
    filled = round(fraction * width)
    return "[" + "#" * filled + "-" * (width - filled) + "]"


def schedule_cell(cfg: dict, weekday: str) -> str:
    slot = cfg.get("schedule", {}).get(weekday, "")
    return " / ".join(slot) if isinstance(slot, list) else str(slot)


def open_target(target: Path | str) -> None:
    try:
        if str(target).startswith(("http://", "https://")):
            webbrowser.open(str(target))
        elif sys.platform.startswith("win"):
            os.startfile(str(target))  # type: ignore[attr-defined]
        elif sys.platform == "darwin":
            subprocess.run(["open", str(target)], check=False)
        else:
            subprocess.run(["xdg-open", str(target)], check=False)
    except Exception:  # opening things is a convenience, never a failure
        pass


# ----------------------------------------------------------------------------------------------------- git

def git(*args: str, timeout: int = 60) -> tuple[int, str]:
    env = {**os.environ, "GIT_TERMINAL_PROMPT": "0"}  # fail fast instead of hanging on a hidden prompt
    try:
        proc = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, timeout=timeout,
                              env=env, encoding="utf-8", errors="replace")
    except (OSError, subprocess.TimeoutExpired) as exc:
        return 1, str(exc)
    return proc.returncode, (proc.stdout + proc.stderr).strip()


def sync(cfg: dict) -> str | None:
    if not cfg.get("git", {}).get("pull_on_start", True) or not (ROOT / ".git").exists():
        return None
    code, _ = git("pull", "--ff-only", "--quiet", timeout=30)
    return None if code == 0 else "couldn't sync from GitHub (offline?) - using this computer's copy"


def commit_and_push(cfg: dict, message: str) -> str:
    settings = cfg.get("git", {})
    if not settings.get("auto_commit", True) or not (ROOT / ".git").exists():
        return "Not committed (auto_commit is off)."
    git("add", "-A")
    code, out = git("commit", "-m", message)
    if code != 0 and "nothing to commit" not in out:
        return f"Commit failed: {out.splitlines()[-1] if out else 'unknown error'}"
    if not settings.get("auto_push", True):
        return "Committed locally (auto_push is off)."
    code, _ = git("pull", "--rebase", "--autostash", "--quiet", timeout=60)
    if code != 0:
        git("rebase", "--abort")
        return "Committed locally, but another computer changed the same lines - run `git pull --rebase` and fix it."
    code, _ = git("push", timeout=120)
    if code == 0:
        return "Committed and pushed - every device sees it now."
    return "Committed locally; push failed (offline or not signed in) - it goes up with your next `today done`."


# ----------------------------------------------------------------------------------------------------- KPIs

def kpis(cfg: dict, tracks: dict[str, Track], entries: list[Entry], jobs: list[tuple[dt.date, str, int]],
         day: dt.date) -> list[Kpi]:
    """The scoreboard: the last 7 days against the 7 before, each against its target in [kpi.targets]."""
    targets = cfg.get("kpi", {}).get("targets", {})
    start = day - dt.timedelta(days=6)
    prev_end = start - dt.timedelta(days=1)
    prev_start = prev_end - dt.timedelta(days=6)
    windows = ((start, day), (prev_start, prev_end))

    def inside(a: dt.date, b: dt.date) -> list[Entry]:
        return [e for e in entries if a <= e.date <= b]

    def target(name: str) -> float | None:
        value = targets.get(name)
        return float(value) if isinstance(value, (int, float)) else None

    now, before = (inside(a, b) for a, b in windows)
    rows = [Kpi("Days showed up", len({e.date for e in now}), len({e.date for e in before}), target("days_per_week")),
            Kpi("Blocks completed", len(now), len(before), target("blocks_per_week")),
            Kpi("Deep-work hours", sum(e.minutes for e in now) / 60, sum(e.minutes for e in before) / 60,
                target("hours_per_week"), "h")]
    keys = [k for k, _ in blocks(cfg)] or list(tracks)
    for key in keys:
        title = plain(tracks[key].title) if key in tracks else key
        if key in targets.get("sessions", {}) or blocks(cfg):
            rows.append(Kpi(f"{title}: sessions finished",
                            sum(e.finished for e in now if e.track == key),
                            sum(e.finished for e in before if e.track == key),
                            targets.get("sessions", {}).get(key)))
        if key in targets.get("score", {}):
            rows.append(Kpi(f"{title}: score", *(score_rate(entries, key, a, b) for a, b in windows),
                            targets["score"][key], "pct"))
    if blocks(cfg) or jobs:
        def count(events: tuple[str, ...], a: dt.date, b: dt.date) -> int:
            return sum(n for d, event, n in jobs if event in events and a <= d <= b)
        rows.append(Kpi("Applications sent", *(count(("applied",), a, b) for a, b in windows),
                        target("applications_per_week")))
        rows.append(Kpi("Screens + interviews", *(count(("screen", "interview"), a, b) for a, b in windows),
                        target("interviews_per_week")))
    return rows


def furthest_behind(rows: list[Kpi]) -> Kpi | None:
    behind = [k for k in rows if k.met is False and k.target]
    return min(behind, key=lambda k: (k.now or 0) / (k.target or 1)) if behind else None


def weakest_modules(track: Track, limit: int = 3) -> list[tuple[Module, str]]:
    """The lowest-rated open modules, as (module, "2/5" or "unrated"); unrated sorts as a 3."""
    open_modules = sorted((m for m in track.modules if not m.done), key=lambda m: track.rank.get(m.mid, 3))
    return [(m, f"{track.rank[m.mid]}/5" if m.mid in track.rank else "unrated") for m in open_modules[:limit]]


def exit_checks(cfg: dict, tracks: dict[str, Track], entries: list[Entry], jobs: list[tuple[dt.date, str, int]],
                day: dt.date) -> list[tuple[str, bool]]:
    """The phase's finish line ([phase.<name>.exit]): all true - or an offer in hand - means switch phase."""
    rules = phase(cfg)[1].get("exit", {})
    if not rules:
        return []
    window = int(rules.get("window_days", 28))
    start = day - dt.timedelta(days=window - 1)
    checks = []
    for key in rules.get("complete", []):
        if key in tracks:
            checks.append((f"{plain(tracks[key].title)}: curriculum complete ({tracks[key].percent():.0%})",
                           tracks[key].percent() >= 1))
    for key, goal in rules.get("score", {}).items():
        rate = score_rate(entries, key, start, day)
        title = plain(tracks[key].title) if key in tracks else key
        checks.append((f"{title}: score >= {goal:.0%} over the last {window} days (now "
                       f"{'-' if rate is None else f'{rate:.0%}'})", rate is not None and rate >= goal))
    for key, goal in rules.get("rating", {}).items():
        if key in tracks and tracks[key].modules:
            lowest = min(tracks[key].rank.get(m.mid, 0) for m in tracks[key].modules)
            checks.append((f"{plain(tracks[key].title)}: every module rated >= {goal} (lowest now {lowest})",
                           lowest >= goal))
    offers = sum(n for _, event, n in jobs if event == "offer")
    checks.append((f"...or an offer in hand ({offers} so far)", offers > 0))
    return checks


# ----------------------------------------------------------------------------------------------------- the card

def deep_block(track: Track, minutes: int, reason: str, label: str = "2) DEEP BLOCK", full: bool = True,
               score_hint: str = "") -> tuple[list[str], list[str]]:
    module, session = track.current()
    if module is None or session is None:
        return wrap(f"{label}  {track.title}: every session is ticked. Design the next rung "
                    "(OPERATIONS.md, 'Editing the curriculum').", "  "), []
    done = sum(s.done for s in module.sessions)
    lines = [f"  {label}  {minutes} min  |  {plain(track.title).upper()}  ({reason})"]
    rated = f"  |  you rated it {track.rank[module.mid]}/5" if module.mid in track.rank else ""
    lines += labelled("Module", f"{module.mid} {module.title}  [rung {module.meta.get('rung', '?')}]  session "
                                f"{done + 1} of {len(module.sessions)}  |  track {track.percent():.0%} done{rated}")
    if module.goal and full:
        lines += labelled("Goal", module.goal)
    lines += labelled("TODAY", f"{session.sid} - {session.text}")
    links = links_in(session.text) or [url for r in module.resources for url in links_in(r)][:3 if full else 1]
    for i, url in enumerate(links):
        lines.append(f"  {'Links' if i == 0 else '':<8}{url}")
    if score_hint:
        lines += labelled("Score", score_hint)
    if module.gate and full:
        lines += labelled("Gate", module.gate)
    if done == 0 and full:
        lines += labelled("New", "First session of this module: do the 2-minute module kickoff "
                                 "(OPERATIONS.md) before you start.")
    return lines, links


def score_hint(cfg: dict, key: str) -> str:
    return str(cfg.get("kpi", {}).get("score_prompt", {}).get(key, ""))


def phase_blocks(cfg: dict, tracks: dict[str, Track], day: dt.date, entries: list[Entry],
                 key: str, reason: str) -> tuple[list[str], list[str]]:
    """Every block of the day, hardest first: the next one in full, the rest compact, the finished ones ticked."""
    plan = day_plan(cfg, day, entries)
    if not reason.startswith("block") and any(k == key and not done for k, _, done in plan):
        plan.sort(key=lambda p: (p[0] != key or p[2]))  # a swap moves that block to the front
    out: list[str] = []
    links: list[str] = []
    first = True
    for index, (k, minutes, done) in enumerate(plan, 1):
        title = plain(tracks[k].title).upper() if k in tracks else k
        if done:
            out += [f"  [x] {index}) {title}  - done today", ""]
            continue
        block, found = deep_block(get_track(tracks, k), minutes, reason if first else "next", f"[ ] {index})",
                                  full=first, score_hint=score_hint(cfg, k))
        out += block + [""]
        links = links or found
        first = False
    if first:  # every block done
        bonus = weakest_block(cfg, entries, day)
        out += wrap(f"All {len(plan)} blocks done - that's the whole day. Bonus? `today more` gives you another "
                    f"{plain(tracks[bonus].title) if bonus in tracks else bonus} session (your lowest score this "
                    "week). Or rest: recovery is part of the system.", "  ") + [""]
    return out, links


def kpi_strip(cfg: dict, tracks: dict[str, Track], entries: list[Entry], jobs: list[tuple[dt.date, str, int]],
              day: dt.date) -> list[str]:
    rows = [k for k in kpis(cfg, tracks, entries, jobs, day) if k.target is not None]
    if not rows:
        return []
    on = sum(bool(k.met) for k in rows)
    text = f"KPIs, last 7 days: {on} of {len(rows)} on target."
    worst = furthest_behind(rows)
    if worst:
        text += f" Furthest behind: {worst.label} {worst.show(worst.now)} (target {worst.show(worst.target)})."
    return wrap(text + " Full table: `today status`.", "  ")


def build_card(cfg: dict, tracks: dict[str, Track], st: Stats, day: dt.date, entries: list[Entry],
               jobs: list[tuple[dt.date, str, int]], key: str, reason: str) -> tuple[list[str], list[str]]:
    habit = cfg.get("habit", {})
    phased = bool(blocks(cfg))
    day_no = st.days + (0 if st.today_done else 1)
    rule = "=" * WIDTH
    title = f"  |  {phase(cfg)[0].replace('-', ' ').upper()}" if phased else ""
    out = [rule, f"  CHAOS  |  {day:%a %d %b %Y}  |  Day {day_no}  |  streak {st.current} (best {st.longest}){title}",
           rule]
    if habit.get("identity"):
        out += wrap(habit["identity"], "  ")
    out.append("")
    if st.today_done and not phased:
        out += wrap("Today's block is logged - well done. Another? `today more` picks your most neglected track. "
                    "Or rest: recovery is part of the system.", "  ")
        out.append("")
    elif st.today_done:
        pass  # the block list below shows what's done and what's left
    elif st.gap == 2:
        out += wrap("You missed yesterday. Never miss twice: today is the day that counts - even the "
                    "two-minute version keeps the chain alive.", "  ! ", "    ")
        out.append("")
    elif st.gap is not None and st.gap > 2:
        out += wrap(f"Welcome back after {st.gap - 1} days. No guilt, no catching up: 30 minutes on the first "
                    "block today, the full day tomorrow (OPERATIONS.md, 'Restart').", "  ! ", "    ")
        out.append("")
    cue = f"{habit.get('time', '')} {habit.get('place', '')}".strip()
    if habit.get("after"):
        cue += f", after {habit['after']}"
    if cue:
        out += labelled("CUE", cue + ".")
        out.append("")
    if phased:
        rated = latest_ratings(parse_ratings())
        for t in (t for t in tracks.values() if t.weakest and not any(m.mid in rated for m in t.modules)):
            out += wrap(f"First, 2 minutes: `today rate` - score yourself 1-5 on each {plain(t.title)} module, so "
                        "your weakest skill comes first.", "  ! ", "    ") + [""]
        out += wrap("HARDEST FIRST. The first link is already open - start the timer and begin.", "  ") + [""]
        block, links = phase_blocks(cfg, tracks, day, entries, key, reason)
        out += block
    else:
        warm = cfg.get("warmup", {})
        snack = warm.get("snack", {}).get(WEEKDAYS[day.weekday()], "")
        if warm.get("anki") or snack:
            out.append("  1) WARM-UP  5-10 min  (the two-minute rule lives here)")
            if warm.get("anki"):
                out += bullet(warm["anki"])
            if snack:
                name, _, url = snack.partition("|")
                out += bullet(name.strip())
                if url.strip():
                    out.append(f"      {url.strip()}")
            out.append("")
        block, links = deep_block(get_track(tracks, key), int(habit.get("block_minutes", 75)), reason)
        out += block
        out.append("")
    if habit.get("minimum"):
        out += wrap(f"Bad day? Two-minute version: {habit['minimum']}.", "  ")
        out.append("")
    if phased:
        out.append("  CLOSE  after each block:   today done   (logs it, ticks it, scores it, pushes)")
        out += kpi_strip(cfg, tracks, entries, jobs, day)
        out += wrap("Applied somewhere / got a call?   today job applied 1   |   today job interview 1", "  ")
    else:
        out.append("  3) CLOSE  when you're done:   today done")
    out += [rule, f"  1.01^{day_no} = {1.01 ** day_no:.2f}x   |   {NUDGES[day_no % len(NUDGES)]}", rule]
    return out, links


# ----------------------------------------------------------------------------------------------------- progress

def last_studied(entries: list[Entry]) -> dict[str, dt.date]:
    last: dict[str, dt.date] = {}
    for e in entries:
        if e.track:
            last[e.track] = max(last.get(e.track, e.date), e.date)
    return last


def progress_md(cfg: dict, tracks: dict[str, Track], entries: list[Entry], day: dt.date) -> str:
    st = stats(entries, day)
    last = last_studied(entries)
    upcoming = day + dt.timedelta(days=1) if st.today_done else day
    jobs = parse_jobs()
    lines = ["# Progress", "",
             f"_Written by `today` on {day.isoformat()}. Regenerated every time you close a block - don't edit by "
             "hand._", ""]
    if blocks(cfg):
        lines += [f"**Phase: {phase(cfg)[0].replace('-', ' ')}.** Every day, hardest first:", ""]
        for index, (key, minutes, done) in enumerate(day_plan(cfg, day, entries), 1):
            _, session = tracks[key].current() if key in tracks else (None, None)
            lines.append(f"{index}. {'~~' if done else ''}**{tracks[key].title if key in tracks else key}** "
                         f"({minutes} min){'~~ done today' if done else ''} — " +
                         (f"`{session.sid}` {cell(session.text, 120)}" if session else "complete"))
        lines.append("")
    else:
        next_key = scheduled(cfg, upcoming)
        if next_key in tracks:
            _, session = tracks[next_key].current()
            if session:
                lines += [f"**Up next ({upcoming:%A %d %b}):** {tracks[next_key].title} — `{session.sid}` "
                          f"{cell(session.text, 140)}", ""]
    lines += ["| The habit | |", "|---|---|",
              f"| Study days | {st.days} |",
              f"| Current streak | {st.current} days |",
              f"| Longest streak | {st.longest} days |",
              f"| Never-missed-twice run | {st.resilient} days |",
              f"| Hours in deep blocks | {st.hours:.1f} |",
              f"| Compounding (1.01^days) | {1.01 ** st.days:.2f}x |", ""]
    rows = kpis(cfg, tracks, entries, jobs, day)
    lines += ["## KPIs — last 7 days", "", "| KPI | Last 7 days | The 7 before | Trend | Target | |",
              "|---|---|---|---|---|---|"]
    for k in rows:
        mark = "" if k.met is None else ("on target" if k.met else "**behind**")
        lines.append(f"| {k.label} | {k.show(k.now)} | {k.show(k.before)} | {k.trend} | "
                     f"{k.show(k.target) if k.target is not None else '—'} | {mark} |")
    lines += ["", "_Targets live in `system/config.toml` → `[kpi.targets]`. Every Sunday, pick the KPI furthest "
              "behind and change one thing in the system for it (`today week`)._", ""]
    weakest = [t for t in tracks.values() if t.weakest]
    for t in weakest:
        lines += [f"**Weakest first — {t.title}:** " + ", ".join(
            f"{m.mid} {m.title} ({r})" for m, r in weakest_modules(t)) + " · re-rate with `today rate`", ""]
    checks = exit_checks(cfg, tracks, entries, jobs, day)
    if checks:
        lines += ["## Finish line for this phase", "",
                  *(f"- [{'x' if ok else ' '}] {text}" for text, ok in checks), "",
                  "_All ticked (or an offer in hand) → set `phase.current = \"long-path\"` in `system/config.toml`, "
                  "and the decade plan takes over._", ""]
    lines += ["## Tracks", "",
              "| Track | Progress | Modules | Current module | Next session | Last studied |",
              "|---|---|---|---|---|---|"]
    for t in tracks.values():
        module, session = t.current()
        lines.append(
            f"| [{t.title}](tracks/{t.key}/curriculum.md) | `{bar(t.percent())}` {t.percent():.0%} | "
            f"{sum(m.done for m in t.modules)}/{len(t.modules)} | "
            f"{cell(f'{module.mid} {module.title}') if module else 'complete'} | "
            f"{cell(f'{session.sid} — {session.text}') if session else '—'} | {last.get(t.key, '—')} |")
    if blocks(cfg):
        lines += ["", "## The day", "",
                  "Every day is the same: " + " → ".join(
                      f"{tracks[k].title if k in tracks else k} ({m} min)" for k, m in blocks(cfg)) +
                  ". The weekday schedule in `system/config.toml` takes over again in the long-path phase.", ""]
    else:
        lines += ["", "## The week", "",
                  "| " + " | ".join(d[:3].title() for d in WEEKDAYS) + " |",
                  "|" + "---|" * len(WEEKDAYS),
                  "| " + " | ".join(schedule_cell(cfg, d) for d in WEEKDAYS) + " |", "",
                  "_Lists alternate week by week. Change the schedule in `system/config.toml`._", ""]
    return "\n".join(lines)


# ----------------------------------------------------------------------------------------------------- commands

def interactive() -> bool:
    return sys.stdin is not None and sys.stdin.isatty()


def ask(prompt: str, default: str = "") -> str:
    try:
        answer = input(f"  {prompt}{f' [{default}]' if default else ''}: ").strip()
    except EOFError:
        return default
    return answer or default


def ask_yes(prompt: str, default: bool = True) -> bool:
    try:
        answer = input(f"  {prompt} [{'Y/n' if default else 'y/N'}]: ").strip().lower()
    except EOFError:
        return default
    return default if not answer else answer.startswith("y")


def cmd_show(args: argparse.Namespace, cfg: dict) -> int:
    note = None if args.no_sync else sync(cfg)
    tracks = load_tracks(cfg)
    entries = parse_logs()
    key, reason = choose_track(cfg, args.date, entries=entries)
    get_track(tracks, key)
    st = stats(entries, args.date)
    lines, links = build_card(cfg, tracks, st, args.date, entries, parse_jobs(), key, reason)
    if note:
        lines.insert(3, f"  ({note})")
    print("\n".join(lines))
    finished = all(done for _, _, done in day_plan(cfg, args.date, entries)) if blocks(cfg) else st.today_done
    if links and not args.no_open and not finished and cfg.get("open", {}).get("first_link", True):
        open_target(links[0])
    return 0


def append_log(day: dt.date, entry: list[str]) -> Path:
    path = LOGS_DIR / f"{day:%Y-%m}.md"
    existing = read(path) if path.exists() else (
        f"# Log — {day:%B %Y}\n\n<!-- One block per study day, written by `today done`. "
        "Template: ../templates/daily-log.md -->\n")
    write(path, existing.rstrip("\n") + "\n\n" + "\n".join(entry) + "\n")
    return path


def tick(track: Track, session: Session, day: dt.date) -> None:
    lines = read(track.path).splitlines()
    line = lines[session.line]
    if session.sid not in line or "[ ]" not in line:
        sys.exit(f"Couldn't find {session.sid} unticked on line {session.line + 1} of {track.path} - "
                 "was the file edited mid-session?")
    lines[session.line] = line.replace("[ ]", "[x]", 1).rstrip() + f" ({day.isoformat()})"
    write(track.path, "\n".join(lines) + "\n")


def cmd_done(args: argparse.Namespace, cfg: dict) -> int:
    day = args.date
    tracks = load_tracks(cfg)
    before = parse_logs()
    key, _ = choose_track(cfg, day, args.track, before)
    track = get_track(tracks, key)
    module, session = track.current()
    st = stats(before, day)
    day_no = st.days + (0 if st.today_done else 1)
    blocks_today = sum(e.date == day for e in before)
    quick = args.yes or not interactive()
    anki = bool(cfg.get("warmup", {}).get("anki"))

    print(f"\n  Closing Day {day_no} - {plain(track.title)}" + (f" - {session.sid}" if session else ""))

    def value(given: str | None, prompt: str, default: str = "") -> str:
        if given is not None:
            return given
        return default if quick else ask(prompt, default)

    raw_minutes = value(None if args.minutes is None else str(args.minutes), "Minutes in the block",
                        str(block_minutes(cfg, key)))
    digits = re.match(r"\d+", raw_minutes)
    minutes = int(digits.group()) if digits else 0
    did = value(args.did, "What did you do? (one line)")
    note = value(args.note, "One thing you understood - or where you got stuck")
    hint = score_hint(cfg, key)
    score = value(args.score, f"Score - {hint} (Enter to skip)" if hint else "Score, as hit/asked (Enter to skip)")
    while score and not SCORE_RE.match(score):
        if quick:
            sys.exit(f"Score must look like 2/3, got '{score}'.")
        score = ask("Score as two numbers, e.g. 2/3 (Enter to skip)")
    artifact = value(args.artifact, "Artifact produced (path/link, Enter for none)")
    if session is None or args.partial:
        finished = False
    elif quick:
        finished = True
    else:
        finished = ask_yes(f"Finished {session.sid}? (No keeps it as next time's session)", True)
    deck_ok = ((not args.no_deck) if quick else ask_yes("Anki reviews done?", True)) if anki else None

    topic = key
    if session is not None:
        topic += f" · {session.sid} — {LINK_RE.sub(lambda m: m.group(1), session.text)}"
        topic += "" if finished else " (in progress)"
    if not st.today_done:
        label = ""
    elif blocks(cfg) and blocks_today < len(blocks(cfg)):
        label = f" · block {blocks_today + 1}"
    else:
        label = " · bonus"
    entry = [f"### {day.isoformat()} · Day {day_no}{label}",
             f"- **Track / topic:** {topic}",
             f"- **Block (min):** {minutes}",
             f"- **Did:** {did or '—'}",
             f"- **Understood / stuck:** {note or '—'}"]
    if score:
        entry.append(f"- **Score:** {score.replace(' ', '')}")
    if deck_ok is not None:
        entry.append(f"- **Deck:** {'reviewed' if deck_ok else 'skipped'}")
    entry.append(f"- **Artifact:** {artifact or '—'}")
    message = (f"Day {day_no}: {key}" + (f" {session.sid}" if session else "") + ("" if finished else " (in progress)")
               + (f" ({score.replace(' ', '')})" if score else ""))

    if args.dry_run:
        print(f"\n  [dry run] would append to logs/{day:%Y-%m}.md:\n")
        print("\n".join("    " + line for line in entry))
        if finished and session:
            print(f"\n  [dry run] would tick {session.sid} in {track.path.relative_to(ROOT)}")
        print(f"  [dry run] would commit: {message}")
        return 0

    append_log(day, entry)
    module_finished = False
    if finished and session is not None and module is not None:
        tick(track, session, day)
        refreshed = parse_track(track.path)
        module_finished = any(m.mid == module.mid and m.done for m in refreshed.modules)
    clear_state()
    tracks = load_tracks(cfg)
    entries = parse_logs()
    write(PROGRESS_PATH, progress_md(cfg, tracks, entries, day))
    git_note = commit_and_push(cfg, message)

    after = stats(entries, day)
    print()
    which = ("a bonus block on " if label == " · bonus" else f"block {blocks_today + 1} of " if blocks(cfg) else "")
    print(f"  Logged {which}Day {day_no}. Streak {after.current} "
          f"(best {after.longest})  |  never-missed-twice run {after.resilient} days  |  {after.hours:.1f} h total")
    if module_finished and module is not None:
        print()
        print("\n".join(wrap(f"MODULE COMPLETE: {module.mid} {module.title}. Produce the gate artifact, run the "
                             "module close-out (OPERATIONS.md), and collect the reward you promised yourself."
                             + (" Then re-rate it: `today rate`." if track.weakest else ""), "  * ", "    ")))
    _, upcoming = tracks[key].current()
    if upcoming:
        print("\n".join(wrap(f"Next time on {tracks[key].title}: {upcoming.sid} - {upcoming.text}", "  ", "    ")))
    if blocks(cfg):
        left = [(k, m) for k, m, done in day_plan(cfg, day, entries) if not done]
        if left:
            nxt_key, nxt_minutes = left[0]
            _, nxt = tracks[nxt_key].current() if nxt_key in tracks else (None, None)
            print("\n".join(wrap(f"NEXT BLOCK ({nxt_minutes} min): {tracks[nxt_key].title}"
                                 + (f" - {nxt.sid} - {nxt.text.rstrip('.')}" if nxt else "") + ". Take 5 minutes away from the "
                                 "screen, then `today` again.", "  > ", "    ")))
        else:
            print("  That's every block today. Done is done - rest. (Bonus: `today more`.)")
    else:
        tomorrow = day + dt.timedelta(days=1)
        next_key = scheduled(cfg, tomorrow)
        if next_key in tracks:
            _, nxt = tracks[next_key].current()
            if nxt:
                print("\n".join(wrap(f"Tomorrow ({tomorrow:%A}): {tracks[next_key].title} - {nxt.sid} - {nxt.text}",
                                     "  ", "    ")))
    print(f"  {git_note}")
    print()
    return 0


def cmd_swap(args: argparse.Namespace, cfg: dict) -> int:
    get_track(load_tracks(cfg), args.track)
    write_state(args.date, track=args.track, why="swapped - your choice")
    return cmd_show(args, cfg)


def cmd_more(args: argparse.Namespace, cfg: dict) -> int:
    day = args.date
    tracks = load_tracks(cfg)
    entries = parse_logs()
    if blocks(cfg):
        left = [k for k, _, done in day_plan(cfg, day, entries) if not done]
        if left:
            print(f"  Today's blocks come first - next up is {plain(tracks[left[0]].title)}. Run `today`.")
            return 0
        key, reason = weakest_block(cfg, entries, day), "bonus - your lowest score this week"
    else:
        studied_today = {e.track for e in entries if e.date == day}
        last = last_studied(entries)
        spine = set(cfg.get("tracks", {}).get("spine", list(tracks)))
        candidates = [k for k, t in tracks.items() if t.current()[1] is not None and k not in studied_today]
        if not candidates:
            print("  Every track is covered today. Rest - you've earned it.")
            return 0
        candidates.sort(key=lambda k: (last.get(k, dt.date.min), k not in spine))
        key, reason = candidates[0], "bonus - your most neglected track"
    write_state(day, track=key, why=reason)
    block, links = deep_block(get_track(tracks, key), block_minutes(cfg, key), reason,
                              score_hint=score_hint(cfg, key))
    rule = "=" * WIDTH
    print("\n".join([rule, "  BONUS BLOCK - optional. Today is already a win.", rule, *block, "",
                     "  When you're done:   today done", rule]))
    if links and not args.no_open and cfg.get("open", {}).get("first_link", True):
        open_target(links[0])
    return 0


def cmd_week(args: argparse.Namespace, cfg: dict) -> int:
    day = args.date
    year, week, _ = day.isocalendar()
    path = WEEKLY_DIR / f"{year}-W{week:02d}.md"
    if path.exists():
        print(f"  This week's review already exists: {path.relative_to(ROOT)}")
    else:
        monday = day - dt.timedelta(days=day.weekday())
        sunday = monday + dt.timedelta(days=6)
        everything = parse_logs()
        tracks = load_tracks(cfg)
        entries = [e for e in everything if monday <= e.date <= sunday]
        days = sorted({e.date for e in entries})
        rows = [f"- **{t.title}** — `{s.sid}` {cell(s.text)}"
                for t in tracks.values() for s in t.sessions
                if s.done and s.done_on and monday <= s.done_on <= sunday]
        numbers = "\n".join([
            f"- Days studied: **{len(days)}/7** ({', '.join(d.strftime('%a') for d in days) or 'none'})",
            f"- Deep-block time: **{sum(e.minutes for e in entries) / 60:.1f} h**",
            f"- Sessions completed: **{len(rows)}**"])
        board = kpis(cfg, tracks, everything, parse_jobs(), min(day, sunday))
        table = ["| KPI | This week | Last week | Target | |", "|---|---|---|---|---|"]
        table += [f"| {k.label} | {k.show(k.now)} | {k.show(k.before)} | "
                  f"{k.show(k.target) if k.target is not None else '—'} | "
                  f"{'' if k.met is None else 'on target' if k.met else '**behind**'} |" for k in board]
        worst = furthest_behind(board)
        table += ["", f"Furthest behind: **{worst.label}** ({worst.show(worst.now)} vs {worst.show(worst.target)})."
                  if worst else "Every KPI with a target is on target. Raise one target by a notch."]
        notes = "\n".join(f"- {e.date:%a}: {e.fields.get('Understood / stuck', '—')}" for e in entries)
        template_path = TEMPLATES_DIR / "weekly-review.md"
        template = read(template_path) if template_path.exists() else "# Weekly review — {{WEEK}}\n\n{{STATS}}\n"
        text = (template.replace("{{WEEK}}", f"{year}-W{week:02d} ({monday:%d %b} – {sunday:%d %b %Y})")
                .replace("{{STATS}}", numbers)
                .replace("{{KPIS}}", "\n".join(table))
                .replace("{{SESSIONS}}", "\n".join(rows) or "- (none ticked this week)")
                .replace("{{TAKEAWAYS}}", notes or "- (no log entries this week)"))
        write(path, text)
        print(f"  Created {path.relative_to(ROOT)}, pre-filled from your logs. 30-45 minutes; honest, not harsh.")
    if not args.no_open:
        open_target(path)
    return 0


def cmd_status(args: argparse.Namespace, cfg: dict) -> int:
    tracks = load_tracks(cfg)
    entries = parse_logs()
    st = stats(entries, args.date)
    write(PROGRESS_PATH, progress_md(cfg, tracks, entries, args.date))
    rule = "=" * WIDTH
    print(rule)
    print(f"  PROGRESS  |  {st.days} study days  |  streak {st.current} (best {st.longest})  |  "
          f"{st.hours:.1f} h  |  1.01^{st.days} = {1.01 ** st.days:.2f}x")
    print(rule)
    focus = [k for k, _ in blocks(cfg)]
    shown = [tracks[k] for k in focus if k in tracks] or list(tracks.values())
    for t in shown:
        module, _ = t.current()
        name = plain(t.title)[:24]
        print(f"  {name:<24} {bar(t.percent(), 24)} {t.percent():>4.0%}   "
              f"{module.mid + ' ' + plain(module.title)[:22] if module else 'complete'}")
    if focus:
        print(f"  (+ {len(tracks) - len(shown)} long-path tracks, waiting for the next phase - see PROGRESS.md)")
    jobs = parse_jobs()
    rows = kpis(cfg, tracks, entries, jobs, args.date)
    print(rule)
    print(f"  {'KPI - last 7 days':<36}{'now':>7}{'before':>8}{'target':>8}   ")
    for k in rows:
        mark = "" if k.met is None else ("ok" if k.met else "BEHIND")
        print(f"  {plain(k.label)[:36]:<36}{k.show(k.now):>7}{k.show(k.before):>8}"
              f"{k.show(k.target) if k.target is not None else '-':>8}   {mark}")
    for t in (t for t in tracks.values() if t.weakest):
        print("\n".join(wrap("Weakest first: " + ", ".join(f"{m.mid} {m.title} {r}" for m, r in weakest_modules(t)),
                             "  ", "    ")))
    checks = exit_checks(cfg, tracks, entries, jobs, args.date)
    if checks:
        print(rule)
        print(f"  FINISH LINE for this phase - {sum(ok for _, ok in checks)} of {len(checks)}")
        for text, ok in checks:
            print("\n".join(wrap(text, f"  [{'x' if ok else ' '}] ", "      ")))
    print(rule)
    print("  PROGRESS.md updated.")
    return 0


def cmd_rate(args: argparse.Namespace, cfg: dict) -> int:
    """Confidence 1-5 per module on the weakest-first tracks; the lowest is served next. Re-rate every Sunday."""
    tracks = load_tracks(cfg)
    keys = [k for k in cfg.get("tracks", {}).get("weakest_first", []) if k in tracks]
    if args.track:
        keys = [get_track(tracks, args.track).key]
    if not keys:
        sys.exit("No track to rate: add one to `weakest_first` under [tracks] in system/config.toml.")
    given: dict[str, int] = {}
    for item in args.ratings:
        mid, _, value = item.partition("=")
        if not re.fullmatch(r"[1-5]", value.strip()):
            sys.exit(f"Use MODULE=N with N from 1 to 5, e.g. CV04=3 (got '{item}').")
        given[mid.strip().upper()] = int(value)
    quick = bool(given) or args.yes or not interactive()
    current = latest_ratings(parse_ratings())
    if not quick:
        print("\n  1 can't explain it | 2 used it, wobbly on why | 3 can explain and use it | "
              "4 can build and debug it | 5 could teach it\n  Enter keeps the current rating.\n")
    lines: list[str] = []
    for key in keys:
        for m in tracks[key].modules:
            if quick and m.mid not in given:
                continue  # only record what you actually rated
            old = current.get(m.mid, 3)
            rating = given.get(m.mid, old)
            if not quick:
                while True:
                    answer = ask(f"{m.mid} {plain(m.title)}", str(old))
                    if re.fullmatch(r"[1-5]", answer):
                        rating = int(answer)
                        break
            lines.append(f"- {m.mid} {m.title}: {rating}")
    unknown = set(given) - {line.split()[1] for line in lines}
    if unknown:
        sys.exit(f"Unknown module(s): {', '.join(sorted(unknown))}")
    if not lines:
        sys.exit("Nothing rated. Run `today rate` in a terminal, or pass pairs like `today rate CV04=3 CV11=2`.")
    if args.dry_run:
        print("\n".join(["  [dry run] would append to logs/ratings.md:", *("    " + line for line in lines)]))
        return 0
    existing = read(RATINGS_PATH) if RATINGS_PATH.exists() else (
        "# Skill ratings\n\n<!-- Confidence 1-5 per module, written by `today rate`. The latest heading wins. -->\n")
    write(RATINGS_PATH, existing.rstrip("\n") + f"\n\n### {args.date.isoformat()}\n" + "\n".join(lines) + "\n")
    tracks = load_tracks(cfg)
    write(PROGRESS_PATH, progress_md(cfg, tracks, parse_logs(), args.date))
    for key in keys:
        weakest = ", ".join(f"{m.mid} {plain(m.title)} ({r})" for m, r in weakest_modules(tracks[key]))
        print("\n".join(wrap(f"{plain(tracks[key].title)} - weakest first: {weakest}", "  ", "    ")))
    print(f"  {commit_and_push(cfg, f'Ratings {args.date.isoformat()}')}")
    return 0


def cmd_job(args: argparse.Namespace, cfg: dict) -> int:
    """Count job-search events. Counts only - no company names, because the repo is public."""
    event = args.event.lower()
    if event not in JOB_EVENTS:
        sys.exit(f"Event must be one of: {', '.join(JOB_EVENTS)}")
    if args.count < 1:
        sys.exit("Count must be 1 or more.")
    line = f"- {args.date.isoformat()} · {event} · {args.count}"
    if args.dry_run:
        print(f"  [dry run] would append to logs/job-search.md: {line}")
        return 0
    existing = read(JOBS_PATH) if JOBS_PATH.exists() else (
        "# Job search\n\n<!-- Counts only, written by `today job`. No company names or salaries: "
        "this repo is public. -->\n")
    write(JOBS_PATH, existing.rstrip("\n") + "\n" + line + "\n")
    tracks = load_tracks(cfg)
    entries = parse_logs()
    write(PROGRESS_PATH, progress_md(cfg, tracks, entries, args.date))
    week = [k for k in kpis(cfg, tracks, entries, parse_jobs(), args.date) if k.label in
            ("Applications sent", "Screens + interviews")]
    print("  Logged. Last 7 days: " + " | ".join(
        f"{k.label} {k.show(k.now)}" + (f"/{k.show(k.target)}" if k.target is not None else "") for k in week))
    if event == "offer":
        print("  An offer! Check the finish line (`today status`) - this is what the whole phase was for.")
    elif event == "rejected":
        print("  A no is data, not a verdict. Add the questions you were asked to the right question bank.")
    print(f"  {commit_and_push(cfg, f'Job search: {event} {args.count}')}")
    return 0


def cmd_doctor(args: argparse.Namespace, cfg: dict) -> int:
    problems: list[str] = []

    def ok(text: str) -> None:
        print(f"  ok    {text}")

    def fix(text: str) -> None:
        problems.append(text)
        print(f"  FIX   {text}")

    print("  Checking this computer and the curriculum...\n")
    if sys.version_info >= (3, 11):
        ok(f"Python {sys.version.split()[0]}")
    else:
        fix(f"Python {sys.version.split()[0]} is too old - install 3.11+")
    code, out = git("--version")
    ok(out) if code == 0 else fix("git not found - install Git")
    for setting in ("user.name", "user.email"):
        code, out = git("config", setting)
        ok(f"git {setting} = {out}") if code == 0 and out else fix(
            f'git {setting} not set: git config --global {setting} "..."')
    code, out = git("remote", "get-url", "origin")
    ok(f"remote origin = {out}") if code == 0 else fix("no git remote 'origin'")
    code, out = git("status", "-sb")
    if code == 0:
        ok(f"branch: {out.splitlines()[0].lstrip('# ')}")

    tracks = load_tracks(cfg)
    seen: dict[str, str] = {}
    modules = sessions = 0
    for t in tracks.values():
        module_ids: set[str] = set()
        for m in t.modules:
            modules += 1
            if m.mid in module_ids:
                fix(f"{t.key}: duplicate module id {m.mid}")
            module_ids.add(m.mid)
            for label, present in (("**Goal:**", m.goal), ("**Resources:**", m.resources),
                                   ("**Gate artifact:**", m.gate), ("sessions", m.sessions)):
                if not present:
                    fix(f"{t.key}/{m.mid}: missing {label}")
            for s in m.sessions:
                sessions += 1
                if not s.sid.startswith(m.mid + "."):
                    fix(f"{t.key}: {s.sid} is filed under {m.mid}")
                if s.sid in seen:
                    fix(f"duplicate session id {s.sid} (in {seen[s.sid]} and {t.key})")
                seen[s.sid] = t.key
    ok(f"curriculum: {len(tracks)} tracks, {modules} modules, {sessions} sessions")
    schedule = cfg.get("schedule", {})
    for weekday in WEEKDAYS:
        slot = schedule.get(weekday)
        if slot is None:
            fix(f"schedule has no {weekday}")
            continue
        for key in slot if isinstance(slot, list) else [slot]:
            if key not in tracks:
                fix(f"schedule.{weekday}: unknown track '{key}'")
    ok("schedule covers every day") if all(d in schedule for d in WEEKDAYS) else None
    name, settings = phase(cfg)
    if name and not settings and name != "long-path":
        fix(f"phase.current = '{name}' but [phase.{name}] has no blocks")
    for key, _ in blocks(cfg):
        if key not in tracks:
            fix(f"phase {name}: block track '{key}' has no tracks/{key}/curriculum.md")
    if blocks(cfg):
        ok(f"phase '{name}': " + " -> ".join(f"{k} {m}m" for k, m in blocks(cfg)))
    for key in cfg.get("tracks", {}).get("weakest_first", []):
        if key not in tracks:
            fix(f"tracks.weakest_first: unknown track '{key}'")
    print()
    print("  All good. Run `today`." if not problems else f"  {len(problems)} thing(s) to fix above.")
    return 1 if problems else 0


# ----------------------------------------------------------------------------------------------------- main

def add_common(parser: argparse.ArgumentParser, top_level: bool) -> None:
    """Flags allowed both before and after the subcommand (argparse needs SUPPRESS on the copies)."""
    hidden = {} if top_level else {"default": argparse.SUPPRESS}
    parser.add_argument("--date", type=dt.date.fromisoformat, help=argparse.SUPPRESS,
                        **({"default": None} if top_level else hidden))
    parser.add_argument("--no-open", action="store_true", help="don't open links or files", **hidden)
    parser.add_argument("--no-sync", action="store_true", help="don't pull from GitHub first", **hidden)


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(errors="replace")  # type: ignore[attr-defined]
        except (AttributeError, ValueError):
            pass
    parser = argparse.ArgumentParser(prog="today", description="Start and close the day's learning.")
    add_common(parser, top_level=True)
    sub = parser.add_subparsers(dest="cmd")
    add_common(sub.add_parser("show", help="today's card (the default)"), top_level=False)
    done = sub.add_parser("done", help="close the day: log, tick, commit, push")
    add_common(done, top_level=False)
    done.add_argument("--track", help="close a different track than today's")
    done.add_argument("--minutes", type=int)
    done.add_argument("--did")
    done.add_argument("--note")
    done.add_argument("--artifact")
    done.add_argument("--score", help="hit/asked, e.g. 2/3 (problems unaided, rubric points, clean answers)")
    done.add_argument("--partial", action="store_true", help="session not finished - keep it for next time")
    done.add_argument("--no-deck", action="store_true", help="Anki reviews skipped today")
    done.add_argument("-y", "--yes", action="store_true", help="no questions - use the defaults")
    done.add_argument("--dry-run", action="store_true", help="show what would be written; change nothing")
    swap = sub.add_parser("swap", help="study a different track today")
    add_common(swap, top_level=False)
    swap.add_argument("track")
    rate = sub.add_parser("rate", help="confidence 1-5 per module; the weakest is served next")
    add_common(rate, top_level=False)
    rate.add_argument("ratings", nargs="*", help="optional MODULE=N pairs, e.g. CV04=3 CV11=2 (skips the prompts)")
    rate.add_argument("--track", help="rate only this track")
    rate.add_argument("-y", "--yes", action="store_true", help="no questions - keep current ratings")
    rate.add_argument("--dry-run", action="store_true")
    job = sub.add_parser("job", help="count a job-search event: " + ", ".join(JOB_EVENTS))
    add_common(job, top_level=False)
    job.add_argument("event", help=" | ".join(JOB_EVENTS))
    job.add_argument("count", nargs="?", type=int, default=1)
    job.add_argument("--dry-run", action="store_true")
    for name, text in (("more", "a bonus block on your weakest score or most neglected track"),
                       ("week", "this week's review, pre-filled"),
                       ("status", "progress and KPI dashboard; rewrites PROGRESS.md"),
                       ("doctor", "check setup and the curriculum format")):
        add_common(sub.add_parser(name, help=text), top_level=False)
    args = parser.parse_args(argv)
    cfg = load_config()
    args.date = args.date or study_day(cfg)
    handlers = {None: cmd_show, "show": cmd_show, "done": cmd_done, "swap": cmd_swap, "more": cmd_more,
                "rate": cmd_rate, "job": cmd_job, "week": cmd_week, "status": cmd_status, "doctor": cmd_doctor}
    return handlers[args.cmd](args, cfg)


if __name__ == "__main__":
    sys.exit(main())
