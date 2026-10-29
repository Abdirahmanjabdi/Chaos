#!/usr/bin/env python3
"""today - the daily driver for the Chaos learning repo.

One command starts the day; one command closes it. The right action should be the easy action.

    today              today's card: cue, warm-up, the exact session and its links (opens the first link)
    today done         close the day: log it, tick the session, refresh PROGRESS.md, commit and push
    today swap TRACK   study a different track today (it's logged - choosing keeps this enjoyable)
    today more         a bonus block, aimed at your most neglected track
    today week         this week's review, pre-filled from your logs
    today status       the progress dashboard (also rewrites PROGRESS.md)
    today doctor       check this computer's setup and the curriculum files' format

Standard library only (Python 3.11+). Every number is derived from the markdown - the curriculum checkboxes and
the logs - so there is no hidden state to drift between computers. Git is the sync.
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

    @property
    def sessions(self) -> list[Session]:
        return [s for m in self.modules for s in m.sessions]

    def current(self) -> tuple[Module | None, Session | None]:
        """The first module with an unticked session, and that session. Work is strictly top to bottom."""
        for module in self.modules:
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
    return {k: parse_track(found[k]) for k in order}


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


def choose_track(cfg: dict, day: dt.date, override: str | None = None) -> tuple[str, str]:
    if override:
        return override, "your choice"
    state = read_state(day)
    if state.get("track"):
        return state["track"], state.get("why", "your choice")
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


# ----------------------------------------------------------------------------------------------------- the card

def deep_block(track: Track, minutes: int, reason: str) -> tuple[list[str], list[str]]:
    module, session = track.current()
    if module is None or session is None:
        return wrap(f"{track.title}: every session is ticked. Design the next rung "
                    "(OPERATIONS.md, 'Editing the curriculum').", "  "), []
    done = sum(s.done for s in module.sessions)
    lines = [f"  2) DEEP BLOCK  {minutes} min  |  {plain(track.title).upper()}  ({reason})"]
    lines += labelled("Module", f"{module.mid} {module.title}  [rung {module.meta.get('rung', '?')}]  session "
                                f"{done + 1} of {len(module.sessions)}  |  track {track.percent():.0%} done")
    if module.goal:
        lines += labelled("Goal", module.goal)
    lines += labelled("TODAY", f"{session.sid} - {session.text}")
    links = links_in(session.text) or [url for r in module.resources for url in links_in(r)][:3]
    for i, url in enumerate(links):
        lines.append(f"  {'Links' if i == 0 else '':<8}{url}")
    if module.gate:
        lines += labelled("Gate", module.gate)
    if done == 0:
        lines += labelled("New", "First session of this module: do the 2-minute module kickoff "
                                 "(OPERATIONS.md) before you start.")
    return lines, links


def build_card(cfg: dict, track: Track, st: Stats, day: dt.date, reason: str) -> tuple[list[str], list[str]]:
    habit = cfg.get("habit", {})
    day_no = st.days + (0 if st.today_done else 1)
    rule = "=" * WIDTH
    out = [rule, f"  CHAOS  |  {day:%a %d %b %Y}  |  Day {day_no}  |  streak {st.current} (best {st.longest})", rule]
    if habit.get("identity"):
        out += wrap(habit["identity"], "  ")
    out.append("")
    if st.today_done:
        out += wrap("Today's block is logged - well done. Another? `today more` picks your most neglected track. "
                    "Or rest: recovery is part of the system.", "  ")
        out.append("")
    elif st.gap == 2:
        out += wrap("You missed yesterday. Never miss twice: today is the day that counts - even the "
                    "two-minute version keeps the chain alive.", "  ! ", "    ")
        out.append("")
    elif st.gap is not None and st.gap > 2:
        out += wrap(f"Welcome back after {st.gap - 1} days. No guilt, no catching up: warm-up plus 30 minutes "
                    "today, full block tomorrow (OPERATIONS.md, 'Restart').", "  ! ", "    ")
        out.append("")
    cue = f"{habit.get('time', '')} {habit.get('place', '')}".strip()
    if habit.get("after"):
        cue += f", after {habit['after']}"
    if cue:
        out += labelled("CUE", cue + ".")
        out.append("")
    out.append("  1) WARM-UP  5-10 min  (the two-minute rule lives here)")
    warm = cfg.get("warmup", {})
    if warm.get("anki"):
        out += bullet(warm["anki"])
    snack = warm.get("snack", {}).get(WEEKDAYS[day.weekday()], "")
    if snack:
        name, _, url = snack.partition("|")
        out += bullet(name.strip())
        if url.strip():
            out.append(f"      {url.strip()}")
    out.append("")
    block, links = deep_block(track, int(habit.get("block_minutes", 75)), reason)
    out += block
    out.append("")
    if habit.get("minimum"):
        out += wrap(f"Bad day? Two-minute version: {habit['minimum']}.", "  ")
        out.append("")
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
    lines = ["# Progress", "",
             f"_Written by `today` on {day.isoformat()}. Regenerated every time you close a day - don't edit by hand._",
             ""]
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
    key, reason = choose_track(cfg, args.date)
    track = get_track(tracks, key)
    st = stats(parse_logs(), args.date)
    lines, links = build_card(cfg, track, st, args.date, reason)
    if note:
        lines.insert(3, f"  ({note})")
    print("\n".join(lines))
    if links and not args.no_open and not st.today_done and cfg.get("open", {}).get("first_link", True):
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
    key, _ = choose_track(cfg, day, args.track)
    track = get_track(tracks, key)
    module, session = track.current()
    st = stats(parse_logs(), day)
    day_no = st.days + (0 if st.today_done else 1)
    habit = cfg.get("habit", {})
    quick = args.yes or not interactive()

    print(f"\n  Closing Day {day_no} - {plain(track.title)}" + (f" - {session.sid}" if session else ""))

    def value(given: str | None, prompt: str, default: str = "") -> str:
        if given is not None:
            return given
        return default if quick else ask(prompt, default)

    raw_minutes = value(None if args.minutes is None else str(args.minutes), "Minutes in the deep block",
                        str(habit.get("block_minutes", 75)))
    digits = re.match(r"\d+", raw_minutes)
    minutes = int(digits.group()) if digits else 0
    did = value(args.did, "What did you do? (one line)")
    note = value(args.note, "One thing you understood - or where you got stuck")
    artifact = value(args.artifact, "Artifact produced (path/link, Enter for none)")
    if session is None or args.partial:
        finished = False
    elif quick:
        finished = True
    else:
        finished = ask_yes(f"Finished {session.sid}? (No keeps it as next time's session)", True)
    deck_ok = (not args.no_deck) if quick else ask_yes("Anki reviews done?", True)

    topic = key
    if session is not None:
        topic += f" · {session.sid} — {LINK_RE.sub(lambda m: m.group(1), session.text)}"
        topic += "" if finished else " (in progress)"
    entry = [f"### {day.isoformat()} · Day {day_no}" + (" · bonus" if st.today_done else ""),
             f"- **Track / topic:** {topic}",
             f"- **Block (min):** {minutes}",
             f"- **Did:** {did or '—'}",
             f"- **Understood / stuck:** {note or '—'}",
             f"- **Deck:** {'reviewed' if deck_ok else 'skipped'}",
             f"- **Artifact:** {artifact or '—'}"]
    message = f"Day {day_no}: {key}" + (f" {session.sid}" if session else "") + ("" if finished else " (in progress)")

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
    print(f"  Logged Day {day_no}. Streak {after.current} (best {after.longest})  |  never-missed-twice run "
          f"{after.resilient} days  |  {after.hours:.1f} h total")
    if module_finished and module is not None:
        print()
        print("\n".join(wrap(f"MODULE COMPLETE: {module.mid} {module.title}. Produce the gate artifact, run the "
                             "module close-out (OPERATIONS.md), and collect the reward you promised yourself.",
                             "  * ", "    ")))
    _, upcoming = tracks[key].current()
    if upcoming:
        print("\n".join(wrap(f"Next time on {tracks[key].title}: {upcoming.sid} - {upcoming.text}", "  ", "    ")))
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
    studied_today = {e.track for e in entries if e.date == day}
    last = last_studied(entries)
    spine = set(cfg.get("tracks", {}).get("spine", list(tracks)))
    candidates = [k for k, t in tracks.items() if t.current()[1] is not None and k not in studied_today]
    if not candidates:
        print("  Every track is covered today. Rest - you've earned it.")
        return 0
    candidates.sort(key=lambda k: (last.get(k, dt.date.min), k not in spine))
    key = candidates[0]
    reason = "bonus - your most neglected track"
    write_state(day, track=key, why=reason)
    block, links = deep_block(tracks[key], int(cfg.get("habit", {}).get("block_minutes", 75)), reason)
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
        entries = [e for e in parse_logs() if monday <= e.date <= sunday]
        days = sorted({e.date for e in entries})
        rows = [f"- **{t.title}** — `{s.sid}` {cell(s.text)}"
                for t in load_tracks(cfg).values() for s in t.sessions
                if s.done and s.done_on and monday <= s.done_on <= sunday]
        numbers = "\n".join([
            f"- Days studied: **{len(days)}/7** ({', '.join(d.strftime('%a') for d in days) or 'none'})",
            f"- Deep-block time: **{sum(e.minutes for e in entries) / 60:.1f} h**",
            f"- Sessions completed: **{len(rows)}**"])
        notes = "\n".join(f"- {e.date:%a}: {e.fields.get('Understood / stuck', '—')}" for e in entries)
        template_path = TEMPLATES_DIR / "weekly-review.md"
        template = read(template_path) if template_path.exists() else "# Weekly review — {{WEEK}}\n\n{{STATS}}\n"
        text = (template.replace("{{WEEK}}", f"{year}-W{week:02d} ({monday:%d %b} – {sunday:%d %b %Y})")
                .replace("{{STATS}}", numbers)
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
    for t in tracks.values():
        module, _ = t.current()
        name = plain(t.title)[:24]
        print(f"  {name:<24} {bar(t.percent(), 24)} {t.percent():>4.0%}   "
              f"{module.mid + ' ' + plain(module.title)[:22] if module else 'complete'}")
    print(rule)
    print("  PROGRESS.md updated.")
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
    done.add_argument("--partial", action="store_true", help="session not finished - keep it for next time")
    done.add_argument("--no-deck", action="store_true", help="Anki reviews skipped today")
    done.add_argument("-y", "--yes", action="store_true", help="no questions - use the defaults")
    done.add_argument("--dry-run", action="store_true", help="show what would be written; change nothing")
    swap = sub.add_parser("swap", help="study a different track today")
    add_common(swap, top_level=False)
    swap.add_argument("track")
    for name, text in (("more", "a bonus block on your most neglected track"),
                       ("week", "this week's review, pre-filled"),
                       ("status", "progress dashboard; rewrites PROGRESS.md"),
                       ("doctor", "check setup and the curriculum format")):
        add_common(sub.add_parser(name, help=text), top_level=False)
    args = parser.parse_args(argv)
    cfg = load_config()
    args.date = args.date or study_day(cfg)
    handlers = {None: cmd_show, "show": cmd_show, "done": cmd_done, "swap": cmd_swap, "more": cmd_more,
                "week": cmd_week, "status": cmd_status, "doctor": cmd_doctor}
    return handlers[args.cmd](args, cfg)


if __name__ == "__main__":
    sys.exit(main())
