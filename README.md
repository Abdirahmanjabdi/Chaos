# Chaos — a decade of deliberate learning, in public

One long-lived repository for going from where I am now to research-level depth across mathematics, computer
science, systems, AI, finance and physics — not in a sprint, but through a small daily habit that compounds for
5–10 years.

**The repo is the credential.** Not certificates or course counts: a decade-deep, public, version-controlled body
of work that *shows* the understanding — derived results, built systems, measured benchmarks, and write-ups of *why*.

> **New here? → [START-HERE.md](START-HERE.md).** Fifteen minutes of setup, then the system runs itself.

---

## The whole method, in three moves

```
today        the card: cue, a 5-10 min warm-up, the exact session, its link opens
(study)      one deep block, 60-90 minutes, phone in another room
today done   log one line, tick the session, streak +1, PROGRESS.md updated, pushed to GitHub
```

You never decide what to study — the curriculum and the weekly schedule already did. On a bad day, the two-minute
version counts. **Never miss twice.** Live progress: **[PROGRESS.md](PROGRESS.md)**.

## The three rules

1. **Artifacts, not exposure.** Every module ends in a committed *gate artifact* — a proof, a program, a benchmark, an
   essay. No artifact, not done.
2. **Consistency over intensity.** 90 minutes a day ≈ 550 hours a year ≈ a graduate education in five. The habit
   *is* the plan. ([HABITS.md](HABITS.md) is how it's designed to stick.)
3. **Depth on a spine, literacy on the rest.** Spine: CS & systems · maths · AI/ML · quant finance — converging on
   low-latency, ML-driven markets. Physics is the disciplined secondary. ([TRAJECTORY.md](TRAJECTORY.md))

## The curriculum

Seven tracks, **114 modules, 807 sessions**, each laddered from foundation to research level
([CURRICULUM.md](CURRICULUM.md)):

| Track | From → to | Modules |
|---|---|---|
| [Mathematics](tracks/math/curriculum.md) | Year 9 → measure theory, stochastic calculus, research | 29 |
| [Systems & Infrastructure](tracks/systems/curriculum.md) | Linux → K8s, AWS, SRE, low latency (= DataPulse) | 15 |
| [Programming & Algorithms](tracks/programming/curriculum.md) | Python properly → C, Rust, SQL, OCaml, C++ | 11 |
| [Computer Science](tracks/cs/curriculum.md) | NAND gates → compilers, OS, Raft, formal methods | 17 |
| [AI & Machine Learning](tracks/ai-ml/curriculum.md) | NumPy → GPT from scratch, RL, diffusion, research | 13 |
| [Finance & Economics](tracks/finance-econ/curriculum.md) | micro/macro → derivatives, quant, microstructure | 12 |
| [Physics](tracks/physics/curriculum.md) | GCSE → Lagrangian, QM, GR, QFT | 17 |

Nearly every resource is free; paid books are marked and optional.

## The documents

| File | What it's for |
|---|---|
| [START-HERE.md](START-HERE.md) | Setup and your first week |
| [HABITS.md](HABITS.md) | The *Atomic Habits* design behind the system — and your commitments |
| [SYSTEM.md](SYSTEM.md) | The daily, weekly, monthly and quarterly loops; the schedule |
| [OPERATIONS.md](OPERATIONS.md) | The playbook: stuck, missed a day, new module, using AI, slumps, new computer |
| [CURRICULUM.md](CURRICULUM.md) | How the tracks, modules, sessions and gates work |
| [TRAJECTORY.md](TRAJECTORY.md) | Where this goes at 1, 3, 5 and 10 years |
| [PROGRESS.md](PROGRESS.md) | The live dashboard (written by `today`) |
| [ROADMAP.md](ROADMAP.md) | DataPulse, the Systems-track flagship project |

## Layout

```
Chaos/
├── start-the-day.cmd       double-click: today's card + a window ready for `today done` (Windows)
├── today.cmd / today.sh    the daily driver (Windows / macOS-Linux) → tools/today.py
├── system/config.toml      your habit settings and the weekly schedule
├── tracks/<track>/         curriculum.md (modules + sessions) and your module notes
├── projects/               flagship projects that cross tracks (DataPulse)
├── logs/                   one file per month, written by `today done` — the evidence
├── review/                 weekly / monthly / quarterly reviews
└── templates/              topic note, ADR, reviews, habit contract
```

Standard-library Python 3.11+ and Git — nothing else to install. Clone it on any computer and `today` just works.
