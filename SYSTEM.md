# SYSTEM — the engine that makes a decade compound

A ten-year goal is not reached by motivation. It is reached by a small loop you run almost every day, protected from
your own moods, with feedback often enough to correct course. This file is that loop. If you only ever read one page
of this repo, read this one.

The design borrows from three well-evidenced ideas: **spaced repetition** (fight forgetting), **deliberate practice**
(work at the edge of ability, with feedback, not comfortable repetition), and **artifacts** (externalise understanding
so it's testable and visible). Everything below is in service of those.

---

## The daily loop (the non-negotiable core)

Every day, in this order, ~90 minutes minimum:

1. **Review (10 min).** Run the spaced-repetition deck (Anki). Definitions, theorems, formulas, syntax, vocab —
   anything memory-heavy from any track. This is what stops last month's work from evaporating.
2. **Deep block (60–90 min).** One topic, from the current spine. Phone in another room. This is *deliberate*
   practice: do problems, derive, build, debug — produce, don't just read. If you're comfortable, you're wasting it;
   move to the edge.
3. **Log (2 min).** One line in `logs/YYYY-MM.md`: what you did, and the single thing you understood or got stuck on.
   Then `git commit`. The commit is the proof the day happened.

That's it. Review, block, log, commit. Three bad days of *just* this still move you forward. The streak is the asset;
`logs/streak.md` tracks it. **Rule: never miss two days in a row.** One miss is noise; two is the start of a stop.

---

## The weekly loop (steering)

Once a week (~45 min), in `review/weekly/YYYY-Www.md`:

- **What landed / what didn't.** Honest. Where did the deep blocks actually go?
- **Produce one real artifact** from the week's work — a write-up, a proof set, a working program, a benchmark. This
  is the week's deliverable; the daily blocks are the means to it.
- **Pick next week's focus:** the one topic on the one track that gets the deep blocks. One. Not five.
- **Deck hygiene:** add cards for what you want to retain; delete cards you've learned past or that are low value.

---

## The monthly & quarterly loops (altitude)

- **Monthly** (`review/monthly/YYYY-MM.md`): skim the month's logs. Did the spine actually advance, or did shiny
  side-topics eat it? Advance a flagship project (`projects/`) at least a little. Re-read the current quarter's goal.
- **Quarterly** (`review/quarterly/YYYY-Qn.md`): the **gate check**. Each track has gates in [CURRICULUM.md](CURRICULUM.md)
  (e.g. "can derive Lagrange's equations and simulate a double pendulum"). Did you pass this quarter's gate and
  produce its artifact? If yes, advance a rung. If no, why — too ambitious, too little time, wrong order? Adjust the
  trajectory. A plan you never revise is a plan you're not really using.

---

## The methods, matched to the material

Different knowledge needs different tools. Don't use one for all:

| Material | Method | In this repo |
|---|---|---|
| Facts, definitions, theorems, formulas, syntax, vocab | **Spaced repetition** (Anki, daily) | cards tagged by track |
| Skills — solving, proving, coding, debugging | **Deliberate practice** (problem sets at the edge, with feedback) | `tracks/*/*/problems/` |
| Understanding — does it connect, can I explain it | **The Feynman test** (write the explanation for a novice) | topic `notes.md`, essays |
| Synthesis — does it all work together | **Projects** (build something that forces many pieces) | `projects/` |
| Retention of the *why* behind a decision | **ADRs & postmortems** (context → options → decision → consequence) | `templates/adr.md` |

**Build naive first, then measure, then improve** — and keep the before/after number. Pre-optimising or
pre-abstracting robs you of the lesson. (Straight from the DataPulse rules; it generalises.)

---

## Tooling for the system itself

- **Anki** — the spaced-repetition deck. One deck, subdecks per track. 10 minutes, every day.
- **Git** — the progress ledger. Commit every study day. `git log` is your real transcript.
- **Markdown + LaTeX** — notes and write-ups; LaTeX (`$...$`) for all maths so it renders on GitHub.
- **A timer** — one honest 60–90 min block beats three distracted hours. Track where the time really goes.
- **The repo** — single source of truth. Not scattered notebooks, not OneNote, not your head.

---

## Guardrails against the ways this dies

- **Tutorial hell / passive consumption** → the artifact rule. No commit, didn't happen.
- **Shiny-topic drift** → the weekly "one focus" and the quarterly gate. Breadth is scheduled, not impulsive.
- **Over-ambition burning you out** → 90 min is the floor and the win. More is a bonus, never the expectation.
- **Silent forgetting** → the daily deck. The most expensive mistake is relearning what you already paid for.
- **Invisible progress killing motivation** → the streak, the green commit squares, the growing `projects/`. Make the
  compounding *visible* so you feel it before you can measure it.

> The goal of this file is to make the right action the default action, on a bad day, with no willpower left.
> If a week feels hard, shrink the block, never the streak.
