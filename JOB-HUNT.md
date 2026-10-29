# Phase 1 — Land the role

Right now one thing matters most: a DevOps / cloud-platform role. So, until the finish line below is ticked (or an
offer is in hand), the system narrows to the three things that decide interviews — and the decade plan waits.

| What decides the interview | Track | Block | How it's scored |
|---|---|---|---|
| Can you code under pressure? | [Coding Interviews](tracks/coding/curriculum.md) — NeetCode 150 + practical DevOps scripting | **1st · 60 min** | problems solved unaided / attempted |
| Can you design a system? | [System Design](tracks/design/curriculum.md) — classic + infra/platform + SRE + low-latency | **2nd · 45 min** | rubric points / 5 |
| Can you defend every line of your CV? | [The CV Stack](tracks/stack/curriculum.md) — Linux → AWS → K8s → Terraform → GitOps → Vault → Prometheus | **3rd · 45 min** | questions answered cleanly / asked |

**Hardest first, every day.** Coding is your hardest, so it gets your freshest 60 minutes. Design comes second. The
CV stack is the tools you already use, so it comes last, and inside it your **weakest-rated skill** always
comes next. Same order every day: nothing to decide, just get cracking.

---

## The day — 2½ hours, three blocks

```
today            the card: all three blocks, hardest first; block 1's link is already open
  block 1        coding, 60 min — timer on, out loud, UMPIRE        → today done  (score 2/3)
  5 min away from the screen
  block 2        design, 45 min — one design, scored on the rubric  → today done  (score 3/5)
  5 min away
  block 3        CV stack, 45 min — your weakest skill               → today done  (score 7/10)
today job applied 2      whenever you send applications (counts only)
```

**Bad day?** Block 1 only, or its two-minute version — it still counts, and the streak holds. **Never miss twice.**

## The week

| When | What | Command |
|---|---|---|
| Every day | three blocks, hardest first | `today` · `today done` ×3 |
| Whenever it happens | applications, screens, interviews, offers | `today job applied 3` |
| After every interview, same day | add every question you were asked to the question banks; re-rate | `today rate` |
| Sunday, 30 min | weekly review: KPIs, **one system change** for the KPI furthest behind; re-rate | `today week` · `today rate` |

## The KPIs — what gets measured gets improved

`today status` (and `PROGRESS.md`) shows the last 7 days against the 7 before, each against a target in
`system/config.toml`:

- **Showing up:** days, blocks, hours.
- **Throughput:** sessions finished per track.
- **Quality:** score per track. This is the one that tells you you're getting *better*, not just busier.
- **Pipeline:** applications sent, screens and interviews.
- **Weakest skill:** your lowest-rated CV-stack modules.

The card names the KPI that's **furthest behind** every day. On Sunday you change one thing in the *system* for it,
not "try harder". Raise a target once you've hit it three weeks running.

## The finish line — when the phase is done

Shown in `PROGRESS.md`, checked over the last 28 days:

- [ ] Coding Interviews curriculum complete (the NeetCode 150 + the practical DevOps rounds + mocks)
- [ ] Coding score ≥ 80% unaided
- [ ] System Design score ≥ 80% on the rubric
- [ ] Every CV-stack module rated 4+ ("I can build it and debug it")
- [ ] …**or an offer in hand.**

Then set `phase.current = "long-path"` in `system/config.toml`. The decade plan in
[TRAJECTORY.md](TRAJECTORY.md) takes over: maths, the systems track (DataPulse), CS, AI/ML, quant finance and physics.
Nothing you did here is wasted. The systems track builds on the CV stack, and the coding track is the
programming track's algorithms module done early.

## How this phase uses your CV

Everything in the CV-stack track comes from your CV's skills and experience lines. Every module ends with
**"defend the bullet"**: say the line in STAR form, with its numbers (90+ resources, 392 → 41 MB, 9 SLIs), and answer
the follow-ups cold. CV14 builds the story itself: the two-minute pitch, eight STAR stories, and the Sentinel
Trading and LivestockChain walk-throughs.

## Privacy — the repo is public

- `today job` stores **counts only**. Keep company names, recruiters, salaries and notes in a private tracker.
- Your CV (with phone and email) **stays out of the repo**.
- Labs: never commit credentials, `*.tfstate`, `*.tfvars` or kubeconfigs (`.gitignore` blocks them; check
  `git status` anyway).
