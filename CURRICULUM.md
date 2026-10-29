# CURRICULUM — the ladders

Seven tracks. Each is a **ladder** of modules from a stated starting level to research level. Every module ends in a
**gate artifact** — the committed thing that proves you cleared it. How fast each ladder is climbed is set by the
weekly schedule in [SYSTEM.md](SYSTEM.md) and the spine in [TRAJECTORY.md](TRAJECTORY.md).

**Levels:** **F** foundation (KS3–GCSE) · **S** school-leaving (A-level + Further) · **U** undergraduate · **G** graduate ·
**R** research edge.

## The tracks

| Track | Rungs | Modules | Sessions | Flagship gates along the way |
|---|---|---|---|---|
| [Mathematics](tracks/math/curriculum.md) | F → R | 29 | 218 | grade-9 GCSE · Euler's formula from series · NumPy linalg library · Itô's lemma & Black–Scholes PDE |
| [Systems & Infrastructure](tracks/systems/curriculum.md) | F → G | 15 | 99 | DataPulse phases 0–10: CI, SLOs, perf report, field notes, RTO/RPO, Rust tail latency |
| [Programming & Algorithms](tracks/programming/curriculum.md) | F → G | 11 | 79 | typed CLI tool · NeetCode 150 · C library · tokio client · order book in C++ vs Rust |
| [Computer Science](tracks/cs/curriculum.md) | F → R | 17 | 130 | a computer from NAND · TCP · a database · clox · Raft · a TLA+ spec |
| [AI & Machine Learning](tracks/ai-ml/curriculum.md) | F → R | 13 | 88 | ML from scratch · micrograd · your own GPT · LoRA fine-tune · DDPM · honest market signal study |
| [Finance & Economics](tracks/finance-econ/curriculum.md) | F → R | 12 | 75 | DCF valuation · three-way option pricer · pricing library · VaR report · honest backtest |
| [Physics](tracks/physics/curriculum.md) | F → R | 17 | 118 | pendulum experiment · double-pendulum chaos · Schrödinger solver · Ising phase transition |

**Total: 114 modules, 807 sessions.** At roughly one session per study day — some take two blocks, graduate ones take
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
**Anki seeds:** what's worth putting in the deck
```

- **Work strictly top to bottom.** `today` serves the first unticked session; you never choose.
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
