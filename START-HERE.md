# START HERE

Fifteen minutes of setup today, then the system runs itself. You never need to plan a study day again.

---

## 1. One-time setup (15 minutes)

- [ ] **Make the habit yours.** Open `system/config.toml` and set `identity`, `time`, `place` and `after` (your
      habit stack) so they're *true for your life*. Then fill in "Your commitments" at the bottom of
      [HABITS.md](HABITS.md).
- [ ] **Install Anki** (free, [apps.ankiweb.net](https://apps.ankiweb.net)) and create an AnkiWeb account so your deck
      syncs between this computer, any other computer, and your phone (AnkiDroid is free; AnkiMobile on iOS is paid).
      Make one deck called `Chaos` with a subdeck per track.
- [ ] **Sign a habit contract.** Copy `templates/habit-contract.md` to `review/contract.md`, fill it in, and ideally
      get someone to sign it with you.
- [ ] **Set a daily phone alarm** at your study time, labelled `today`.
- [ ] **Check the computer:** in this folder run `today doctor` — every line should say `ok`.
- [ ] There's a **"Start the day"** shortcut on your desktop. Double-click it at your cue time.

## 2. How every day works — three moves

```
today        →  the card: your cue, a 5-10 min warm-up, the exact session, its link opens
(study)      →  one deep block, 60-90 min, phone in another room
today done   →  log one line, tick the session, streak +1, progress updated, pushed to GitHub
```

That's the whole method. Bad day? Do the **two-minute version** on the card — open the link, do one problem. It
counts. **Never miss two days in a row.**

Useful extras: `today swap math` (do a different track today) · `today more` (a bonus block on your most neglected
track) · `today week` (Sunday review) · `today status` (progress dashboard).

## 3. Your first week — install the habit, not the knowledge

Week one has one goal: **show up every day**. The sessions you'll get are deliberately placements and orientations —
each track's first session works out where you already are, so you can tick off what you know and start at the
right rung.

| Day | What you'll get | What success looks like |
|---|---|---|
| Thu | Maths M01.S01 — a GCSE placement paper | You know where you stand in maths |
| Fri | AI/ML A01.S01 — setup & orientation | A working notebook environment |
| Sat | Systems S01.S01 — Linux + Bandit levels 0–5 | The shell feels a bit less foreign |
| Sun | Finance E01.S01 — the economic way of thinking | First weekly review (`today week`) |
| Mon | Maths M01.S02 — calculator placement | Tick off the topics you already own |
| Tue | Systems S01.S02 — the shell, properly | Two Linux sessions down |
| Wed | CS C01.S01 — Nand2Tetris orientation | Seven days, seven blocks. The chain is real. |

Keep the blocks short this week if you need to — 30 minutes is fine. **Standardise before you optimise.**

## 4. On another computer

```
git clone https://github.com/Abdirahmanjabdi/Chaos.git
cd Chaos
today doctor          # Windows (needs Python 3.11+ and Git)
./today.sh doctor     # macOS / Linux
```

Clone into a normal folder — **not** into OneDrive/iCloud/Dropbox (two sync systems fighting over `.git` is how
repos get corrupted). Your progress lives in git: `today` pulls the latest when you start, `today done` pushes when
you finish, so every machine is always up to date.

## 5. Where everything is

- [README.md](README.md) — the mission and the map
- [HABITS.md](HABITS.md) — why this works, and your commitments
- [SYSTEM.md](SYSTEM.md) — the daily / weekly / monthly / quarterly loops and the schedule
- [OPERATIONS.md](OPERATIONS.md) — what to do in every situation (stuck, missed a day, new module, using AI…)
- [CURRICULUM.md](CURRICULUM.md) — the seven tracks and how modules work
- [TRAJECTORY.md](TRAJECTORY.md) — where this goes in 1, 3, 5 and 10 years
- [PROGRESS.md](PROGRESS.md) — your live dashboard (auto-generated)
