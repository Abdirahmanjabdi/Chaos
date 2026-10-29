# SYSTEM — the engine that makes a decade compound

A ten-year goal is reached by a small loop you run almost every day, protected from your moods, with feedback often
enough to steer. This file is that loop. [HABITS.md](HABITS.md) explains why it's designed the way it is;
[OPERATIONS.md](OPERATIONS.md) says what to do when anything goes sideways.

It rests on three well-evidenced ideas: **deliberate practice** (work at the edge of your ability, with feedback),
**measurement** (score every block, so feedback is a number, not a feeling), and **artifacts** (externalise
understanding so it's testable and visible).

---

## Phases

The system runs one phase at a time (`system/config.toml` → `[phase] current`):

- **`job-hunt` — now.** Every day is the same three blocks, hardest first: coding (60) → system design (45) → the CV
  stack (45, weakest skill first). Finish line and KPIs: [JOB-HUNT.md](JOB-HUNT.md).
- **`long-path` — after the role.** One deep block a day, the track picked by weekday (below), across the seven
  long-path tracks in [TRAJECTORY.md](TRAJECTORY.md).

## The daily loop

| Step | Time | What | Tool |
|---|---|---|---|
| Cue | — | your time, your place, after your anchor habit | `system/config.toml` |
| Blocks | 60 / 45 / 45 min | hardest first; produce, don't just read; first link already open | `today` |
| Close each block | 2 min | log, **score**, tick, streak, KPIs, commit, push; names the next block | `today done` |

**Floor, not ceiling.** The two-minute version (open the link, do one problem) counts on a bad day. **Never miss
twice**: one miss is noise, two is a new habit. The card warns you the day after a miss.

## The feedback loop: KPIs

Every block ends with a score (hit/asked). `today status`, `PROGRESS.md` and the weekly review turn that into a
KPI table: last 7 days vs the 7 before, against your targets. The card names the KPI furthest behind. Each Sunday:
**one KPI, one change to the system, one week**, then look again. That's how the system keeps improving rather
than just running.

## The weekly schedule (long-path phase)

In the long path, `today` picks the track by weekday, so there's nothing to decide. Lists alternate week by week.

| Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|---|---|---|---|---|---|---|
| Maths | Systems | Programming / CS | Maths | AI/ML | Systems / Finance | Finance / Physics |

Why this shape: maths is the bottleneck for AI, quant and physics, so it gets two days; Systems (DataPulse) is the
fastest route to a senior role; programming gets daily reps through the Tuesday/Thursday Exercism warm-up as well as
its own slot. A different subject most days keeps boredom away. **Re-weight it every quarter** at the gate check as
the trajectory moves on. Want something else today? `today swap TRACK`. Bonus energy? `today more`.

Each warm-up snack is matched to the day: Corbettmaths 5-a-day (Mon/Wed/Fri), Exercism (Tue/Thu), a Bandit level
(Sat), an Isaac Physics problem (Sun) — small enough that starting is effortless.

## The weekly loop — steering (Sunday, 30–45 min)

Run `today week`: it creates `review/weekly/YYYY-Www.md` pre-filled with days studied, hours, the KPI table,
sessions completed and the takeaways you logged. You add: what landed, what didn't, the **Goldilocks check**,
the week's artifact, **one system change** for the KPI furthest behind, and an if-then plan for the likely obstacle.
In the job hunt, finish with `today rate`.

## The monthly and quarterly loops — altitude

- **Monthly** (`review/monthly/`): did the spine actually advance? Push a flagship project forward. One curiosity
  block with no curriculum. Optional public progress post.
- **Quarterly** (`review/quarterly/`): the **gate check** — which modules were completed, with their gate artifacts?
  Is the pace matching [TRAJECTORY.md](TRAJECTORY.md)? Edit the trajectory honestly, re-weight the schedule, renew the
  habit contract. A plan you never revise is decoration.
- **Yearly:** a one-page "year in learning", published.

## How the curriculum is consumed

Each track's `curriculum.md` is a list of **modules**, each a list of **sessions** sized for one deep block, ending
in a **gate artifact**. `today` always serves the first unticked session, top to bottom, so you're never
choosing. The one exception is the CV stack, which is **weakest first**: it finishes the module you've started, then
moves to the one you rated lowest. A session that takes two blocks just stays on the card until you tick it.
Placement sessions at the start of each rung let you tick off what you already own. See [CURRICULUM.md](CURRICULUM.md).

## Methods, matched to the material

| Material | Method | Where |
|---|---|---|
| Skills — solving, proving, coding, debugging | **Deliberate practice** at the edge, timed, scored | the blocks |
| Things you got wrong | **Retrieval & redo** — re-solve from blank days later | `redo.md`, the redo sessions, question banks |
| Understanding — does it connect? can I explain it? | **The Feynman test** — explain it to a novice | module notes |
| Synthesis — does it all work together? | **Projects** | gate artifacts, `projects/` |
| Why a decision was made | **ADRs & postmortems** | `templates/adr.md` |

**Build naive first, then measure, then improve** — and keep the before/after numbers.

## Tooling

- **`today`** (`tools/today.py`) — the daily driver. Standard-library Python, reads only the markdown; no database.
- **Git + GitHub** — the progress ledger and the sync between computers. Every study day is a commit.
- **Markdown + LaTeX** — notes and write-ups; `$...$` maths renders on GitHub.

## Guardrails — how ten-year plans die, and the defence

| Failure mode | Defence |
|---|---|
| Tutorial hell, passive watching | the artifact rule — no artifact, not done |
| Decision fatigue ("what should I study?") | the schedule + strictly-ordered sessions; `today` decides |
| Shiny-topic drift | fixed schedule; breadth goes in `today more` and curiosity blocks |
| Over-ambition → burnout | 90 min is the target, two minutes is the floor; never the reverse |
| Silent forgetting | redo sessions, question banks re-answered cold, weekly re-rating |
| Busy but not better | a score on every block; the KPI furthest behind gets one system change a week |
| Invisible progress → lost motivation | streak, compounding number, KPI trends, PROGRESS.md bars, green squares |
| Boredom (the real killer) | variety by weekday, the Goldilocks check, play built into the curriculum |

> The goal of this file is to make the right action the default action, on a bad day, with no willpower left.
> If a week is hard, shrink the block — never the streak.
