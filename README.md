# Chaos — a decade of deliberate learning, in public

This is a single, long-lived repository for going from where I am now to research-level depth across
computing, mathematics, physics, finance, and AI — not in a weekend, but over 5–10 years of compounding daily work.

**The repo is the credential.** Not a certificate, not a course count — a decade-deep, public, version-controlled
body of work that *shows* the understanding. Anyone can watch a lecture. What this repo proves is that I can derive
the result, build the thing, measure it, and write up *why*.

---

## The three rules that make it work

1. **Artifacts, not exposure.** "I studied X" means nothing. Every topic ends in something committed: a worked
   proof, a solved problem set, a built program, a benchmark with numbers, an essay that explains the hard part. If
   it isn't written down, it didn't happen. (This rule is borrowed from the DataPulse roadmap and now governs
   everything.)
2. **Consistency over intensity.** A 90-minute block every day beats a 10-hour Sunday. 90 min/day is ~550 hours a
   year; in five years that is a graduate education. The [SYSTEM](SYSTEM.md) exists to protect the daily block and
   let it compound. Missing a day is allowed; missing two in a row is the thing to never do.
3. **Depth on a spine, literacy on the rest.** Trying to reach PhD level in six fields at once guarantees shallow
   everywhere. Pick a spine, go deep, and let the overlaps carry the breadth — linear algebra pays off in ML,
   physics, and graphics; stochastic calculus serves both quant finance and diffusion models; Rust serves systems,
   low-latency, and the fintech edge. See [TRAJECTORY](TRAJECTORY.md) for the chosen spine.

---

## How the repo is organised

```
chaos/
├── README.md         ← you are here: the mission
├── SYSTEM.md         ← the daily/weekly/quarterly engine (read this second)
├── CURRICULUM.md     ← every subject, its ladder from my start level to research level, tools, gate artifacts
├── TRAJECTORY.md     ← 1 / 3 / 5 / 10-year milestones tied to who I want to become
├── logs/             ← the daily log (one file per month) + the streak. Evidence of the habit.
├── review/           ← weekly / monthly / quarterly retrospectives
├── templates/        ← reusable skeletons: daily log entry, topic note, ADR, artifact write-up
├── tracks/           ← one folder per domain; each has a README with its ladder + my current rung
│   ├── math/         ← Year 9 → PhD-level
│   ├── physics/      ← GCSE → PhD-level
│   ├── cs/           ← computer science, deep (architecture → distributed systems → PL/theory)
│   ├── programming/  ← languages + algorithms as a craft (Python, C, Rust, SQL, a functional one)
│   ├── systems/      ← Linux, Docker, K8s, AWS, cloud, networking, SRE
│   ├── ai-ml/        ← classical ML → deep learning → modern (LLMs/RL), built from scratch
│   └── finance-econ/ ← economics → finance → quant (stochastic calculus, pricing, microstructure)
└── projects/         ← flagship projects that cross tracks and prove it all works together
    └── datapulse/    ← the applied SRE / low-latency flagship (see ROADMAP.md)
```

Each `tracks/<name>/` folder holds one subfolder per topic, following `templates/topic.md`: what I set out to learn,
the artifact I produced, and the open questions I left. The git history across these folders *is* the progress bar.

---

## How to use it day to day

Open [SYSTEM.md](SYSTEM.md) and run the daily loop. That's the whole method: show up, do one focused block on the
current spine topic, review the deck, log one line, commit. The curriculum tells you *what*; the system makes you
*keep doing it*; the trajectory tells you *why* and *where it goes*.

> Status: **Day 0.** Foundations being laid. The first real entry in `logs/` is the first day this becomes true.
