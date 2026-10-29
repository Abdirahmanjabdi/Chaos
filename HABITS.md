# HABITS — designing a learning habit you'll keep for ten years

A decade of study isn't won by motivation. Motivation is a weather system: it comes and goes. What lasts is a habit
designed so well that doing it is easier than not doing it — on a tired Tuesday, with no willpower left.

This file applies the framework from James Clear's *Atomic Habits* to this mission, and every idea below is wired
into the repo itself — the `today` command, the config, the templates — so it isn't just advice you have to remember.
Read it once properly, fill in **[Your commitments](#your-commitments)** at the bottom, and re-read it whenever the
habit wobbles.

---

## The four ideas underneath everything

**1. Systems beat goals.** "Reach PhD-level maths" is a goal; it tells you nothing about what to do after Isha tonight.
Winners and losers often have the *same* goals — what differs is the system. Your system is the daily loop in
[SYSTEM.md](SYSTEM.md). Fall in love with running it, and the goals take care of themselves.

**2. Tiny improvements compound.** Getting 1% better each day is invisible on day 10 and enormous by year 5
(1.01³⁶⁵ ≈ 37.8). That's why `today` prints the compounding number on your card — so you can *see* something that
otherwise only shows up in hindsight.

**3. Expect the plateau.** For weeks — sometimes months — effort will seem to produce nothing. That is the work
being stored, not wasted: understanding is quietly accumulating below the surface until it breaks through all at
once. Most people quit in this valley. Knowing it's coming is half of getting through it.

**4. Change who you are, not just what you do.** The deepest lever is identity. "I'm trying to study more" is
fragile; "I am a researcher. I show up every day and do the hard thing first" is durable, because people act in line with
who they believe they are. **Every session you complete is a vote for that identity.** You don't need a unanimous
vote — just a majority, day after day. Your identity line sits at the top of every `today` card.

---

## The four laws, built into this repo

Every habit runs on a loop: **cue → craving → response → reward**. Make each stage work for you:

### Law 1 — Make it obvious (the cue)

You can't skip a habit you can't miss. Remove every decision about *whether* and *what*.

- **Implementation intention.** Not "I'll study more" but: *"I will run `today` at 22:00 at my bedroom desk."*
  Vague intentions fail; a specific time and place make it nearly automatic. → `system/config.toml` →
  `[habit] time / place`.
- **Habit stack.** Attach the new habit to one you already do without fail: *"After I pray Isha, I run `today`."*
  The old habit becomes the trigger for the new one — and prayer is the strongest anchor there is, because it
  already happens at a fixed point every single day. Isha moves with the seasons; the habit moves with it. →
  `[habit] after`.
- **Late night, done right.** The block is after Isha, so guard it: sit upright at the desk, never study in bed, and
  do the hard part first while you're still sharp. Closing after midnight is fine — anything before 04:00 counts
  for the night before (`[habit] day_starts`), so the streak never breaks on a technicality.
- **No decisions.** The card tells you the *exact* session, opens its link, and shows the goal. You never decide what
  to study — the curriculum and the schedule already did. Decision fatigue is where habits go to die.
- **Design the environment.** A desktop shortcut called *Start the day*. Notebook and pen left on the desk before you
  pray. Tonight's session is visible in `PROGRESS.md` ("Up next"), so you can glance at it during the day and arrive
  primed.
- **A real-world cue too.** Set a daily phone alarm at your time, labelled `today`.

### Law 2 — Make it attractive (the craving)

We do what we look forward to. Make the session something you anticipate, not endure.

- **Temptation bundling.** Pair the block with something you love that you *only* get during the block — the good
  coffee, a particular playlist, the nice desk light. Want the treat? Do the block.
- **Join a culture where this is normal.** We absorb the habits of the people around us. Public repo with a growing
  contribution graph; Exercism mentors; Isaac Physics; a study Discord or r/learnmath; one friend who follows your
  progress. Surround yourself with people for whom "studied today" is ordinary.
- **A motivation ritual.** Do the same two-minute routine before every block — water, phone into another room, timer
  set, `today` run. Repeated often enough, the ritual itself starts to switch your brain into focus mode.
- **Reframe.** Not "I have to do maths" but "I *get* to build the skill that most people never will." Same task,
  different story.
- **Variety.** A different subject most days (see the schedule) is a deliberate antidote to boredom.

### Law 3 — Make it easy (the response)

The habit that's easiest to start wins. Reduce friction for the good habit; add it to the bad ones.

- **The two-minute rule.** Every habit has a version that takes two minutes. Yours is printed on the card:
  *open the first link and do ONE problem.* On a terrible day, that **counts**. You'll usually keep going — but even
  if you don't, you've kept the identity and the chain. Master the art of showing up before you optimise anything.
- **One command.** `today` opens the day; `today done` closes it — log, tick, streak, commit, push. Nothing to set up,
  nothing to remember.
- **Free resources, ready everywhere.** Nearly every session links to a free resource, and the whole repo is on
  GitHub, so any computer is a study computer.
- **Standardise before you optimise.** For the first two weeks, success is *just showing up* — block 1 plus whatever
  else you manage. All three blocks come once the cue → action link is automatic.
- **Prepare the environment the night before.** Close every tab, leave the notebook open, glance at "Up next".
- **Make the bad habits hard.** Phone in another room during the block. Log out of social apps on the study machine,
  or use a site blocker for the block's duration. Friction is a tool: add it where you want less behaviour.

### Law 4 — Make it satisfying (the reward)

What gets rewarded gets repeated — and the reward has to come *now*, not in five years.

- **Immediate satisfaction.** Ticking the box, the commit, the streak going up by one, a new green square on GitHub —
  `today done` gives you all of them in one go.
- **Track it — and never miss twice.** The streak, the longest streak and the *never-missed-twice run* are computed
  from your logs and shown every day. Missing once is an accident; missing twice is the start of a new (bad) habit.
  The card warns you on the day after a miss, so the second miss is never silent.
- **Celebrate milestones.** Finishing a module is a real event: `today done` announces it, and you collect a reward
  you chose in advance (write your reward list below).
- **A habit contract.** Write down the commitment and a small cost for breaking it, and have someone sign it with you.
  → `templates/habit-contract.md`.
- **Make progress visible.** `PROGRESS.md` shows every track's bar filling up. Look at it on your phone on a bad day.

### The inversions — making distraction lose

| To make the habit lose… | …do the opposite of the law |
|---|---|
| Make distraction **invisible** | Phone in another room; no notifications during the block |
| Make it **unattractive** | Remind yourself what an hour of scrolling actually gave you |
| Make it **difficult** | Log out; site blocker on; apps off the study machine |
| Make it **unsatisfying** | The contract: a missed-twice cost someone else will hold you to |

---

## Staying in love with it (years 2–10)

The real threat to a ten-year habit isn't failure — it's **boredom**. Professionals keep the schedule when it isn't
exciting; that's most of what separates them from amateurs. But you can also *design* against boredom:

- **The Goldilocks zone.** Motivation peaks on tasks at the edge of your ability — not too easy, not impossible. If a
  session is boring, it's probably too easy: go faster, or add a harder problem. If it's crushing you, step back a
  rung. Say so in the weekly review and adjust.
- **Autonomy.** You're never trapped: `today swap TRACK` lets you choose a different subject on any day, and the
  schedule is yours to change in the config. Choosing keeps it yours.
- **Mastery made visible.** Progress bars, gate artifacts, a repo that keeps getting more impressive.
- **Purpose.** Re-read [TRAJECTORY.md](TRAJECTORY.md) every quarter. Remember who this is turning you into.
- **Play.** Advent of Code in December, Project Euler, Bandit levels, Kaggle — built into the curriculum on purpose.
- **Curiosity time.** One block a month with *no curriculum* — follow whatever rabbit hole you want. Log it anyway.
- **Show your work.** A short monthly progress post (LinkedIn, a blog, the repo README). Teaching others is the
  fastest way to learn, and an audience makes it more fun.
- **Review honestly.** The weekly review asks what's working. Keep what is; change what isn't.

---

## Your commitments

Fill these in (here *and* in `system/config.toml`). Make them true for your actual life — a plan you can't keep isn't
a plan.

- **Identity:** I am a researcher. I show up every day and do the hard thing first.
- **Implementation intention:** I will run `today` at 22:00 at my bedroom desk.
- **Habit stack:** After I pray Isha, I run `today`.
- **Two-minute version:** open the first link and do ONE problem — that counts as showing up.
- **Temptation bundle:** I only get ______________________ during the block.
- **Environment:** before I pray Isha, I ______________________________ (laptop open, notebook out).
- **Distraction friction:** during the block, my phone is ______________ and ______________ is blocked.
- **Module reward list:** when I finish a module I get ______________________.
- **Accountability partner:** ______________ (see `templates/habit-contract.md`).

> The goal is the direction; the system is what actually carries you. As Clear puts it, you "fall to the level of
> your systems." Build a good one, and keep falling into it.
