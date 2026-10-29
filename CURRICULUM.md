# CURRICULUM — the ladders

Ten tracks: three for **Phase 1, landing the role**, and seven ladders for **the long path**. Every module ends in a
**gate artifact**, the committed thing that proves you cleared it. Which tracks run, and how fast, is set by the
phase in `system/config.toml`. See [SYSTEM.md](SYSTEM.md), [JOB-HUNT.md](JOB-HUNT.md) and [TRAJECTORY.md](TRAJECTORY.md).

**Levels:** **F** foundation (KS3–GCSE) · **S** school-leaving (A-level + Further) · **U** undergraduate · **G** graduate ·
**R** research edge.

## Phase 1 — land the role (every day, hardest first)

| Track | Modules | Sessions | Score | Flagship gates along the way |
|---|---|---|---|---|
| [Coding Interviews](tracks/coding/curriculum.md) | 19 | 89 | unaided / attempted | NeetCode 150 with "why" docstrings · LRU cache by hand · 8 tested DevOps scripts · 3 passed mocks |
| [System Design](tracks/design/curriculum.md) | 8 | 46 | rubric / 5 | framework checklist · 20+ scored designs · 8 infra/platform designs · matching engine · 4 mocks |
| [The CV Stack](tracks/stack/curriculum.md) | 14 | 94 | clean answers / asked | a question bank per tool at 8/10 · labs rebuilding every CV claim · pitch + 8 STAR stories |

The CV stack is **weakest first**: `today rate` scores each module 1–5 and the lowest comes next. The coding track
overlaps the long-path programming G03 module, and the CV stack overlaps systems S01–S13, so both give you a head
start on the long path.

## The long path — the ladders

| Track | Rungs | Modules | Sessions | Flagship gates along the way |
|---|---|---|---|---|
| [Mathematics](tracks/math/curriculum.md) | F → R | 29 | 218 | grade-9 GCSE · Euler's formula from series · NumPy linalg library · Itô's lemma & Black–Scholes PDE |
| [Systems & Infrastructure](tracks/systems/curriculum.md) | F → G | 15 | 99 | DataPulse phases 0–10: CI, SLOs, perf report, field notes, RTO/RPO, Rust tail latency |
| [Programming & Algorithms](tracks/programming/curriculum.md) | F → G | 11 | 79 | typed CLI tool · NeetCode 150 · C library · tokio client · order book in C++ vs Rust |
| [Computer Science](tracks/cs/curriculum.md) | F → R | 17 | 130 | a computer from NAND · TCP · a database · clox · Raft · a TLA+ spec |
| [AI & Machine Learning](tracks/ai-ml/curriculum.md) | F → R | 13 | 88 | ML from scratch · micrograd · your own GPT · LoRA fine-tune · DDPM · honest market signal study |
| [Finance & Economics](tracks/finance-econ/curriculum.md) | F → R | 12 | 75 | DCF valuation · three-way option pricer · pricing library · VaR report · honest backtest |
| [Physics](tracks/physics/curriculum.md) | F → R | 17 | 118 | pendulum experiment · double-pendulum chaos · Schrödinger solver · Ising phase transition |

**Long path: 114 modules, 807 sessions. With Phase 1: 155 modules, 1,036 sessions.** At roughly one session per study day — some take two blocks, graduate ones take
more — that's the five-to-ten-year arc in [TRAJECTORY.md](TRAJECTORY.md). The research rungs (R) are open-ended by design.

## How a module is built

Every module in every `tracks/<track>/curriculum.md` follows the same shape (so `today` can read it):

```markdown
## M14 · Linear Algebra I (computational)
<!-- rung: U | prereq: M12 | feeds: ML (heavily), physics, CS -->
**Goal:** what you'll be able to *do* when it's finished
**Resources:**
- [the primary resource](https://...) — free unless marked (paid)
**Sessions:**
- [ ] M14.S01 — one deep block's worth of work, specific enough to start without thinking
- [x] M14.S02 — a finished session is ticked and dated by `today done` (2026-11-03)
**Gate artifact:** the committed proof that you cleared it
**Anki seeds:** optional — flashcard ideas, if you ever want them
```

- **Work top to bottom.** `today` serves the first unticked session; you never choose. (The exception is tracks
  in `weakest_first`, which serve your lowest-rated module next.)
- **Placement first.** Each rung opens with a placement session — tick what you already own, append `(placed out)`.
- **Prerequisites cross tracks.** The comment line says which modules (in any track) a module builds on — e.g. AI/ML
  leans on maths M14–M16. If you hit a module before its prereq, `today swap` to the prerequisite first.
- **It's yours to edit.** Add, split, reorder or replace modules as you learn what you need; run `today doctor`
  afterwards to validate the format. Rules in [OPERATIONS.md → Editing the curriculum](OPERATIONS.md#editing-the-curriculum).

## The overlaps — why the spine makes the breadth cheap

These aren't seven islands. Deliberately climb the rungs that pay off in several tracks at once:

- **Linear algebra** (M14, M17) → ML, quantum mechanics, graphics, data.
- **Probability & statistics** (M16, M20) → ML, quant, statistical mechanics, experiment design.
- **Stochastic calculus** (M26) → derivatives pricing (E08) *and* diffusion models (A10).
- **Optimisation** (M22) → training neural networks, portfolio construction.
- **Rust, concurrency, networking** (G05, C13, C07) → SRE, low-latency trading, ML serving.
- **Writing clearly** → every track; it *is* the deliverable.

When you don't know what to push on a bonus block, push the rung that cashes out in the most tracks.

## Cost

Everything needed to *start* every module is free: MIT OpenCourseWare, Harvard Stat 110, Axler, OSTEP, Nand2Tetris,
Crafting Interpreters, the Rust Book, Karpathy, fast.ai, ISLP, Sutton & Barto, Tong's notes, the Feynman Lectures,
OpenStax, Isaac Physics, Dr Frost, Corbettmaths, and more. Books marked **(paid)** are optional — buy one only when you
actually reach it, and only if the free resource isn't enough.
