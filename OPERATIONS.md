# OPERATIONS — the playbook

Every situation you'll hit over ten years, with exactly what to do. When something feels off, find it here instead
of improvising. Each operation is short on purpose.

**Contents:** [Start the day](#start-the-day) · [Close the day](#close-the-day) · [The two-minute day](#the-two-minute-day)
· [Restart after missed days](#restart) · [Swap or bonus](#swap-or-bonus) · [Module kickoff](#module-kickoff)
· [Module close-out](#module-close-out) · [When you're stuck](#when-youre-stuck) · [Using AI without cheating yourself](#using-ai-without-cheating-yourself)
· [Making Anki cards](#making-anki-cards) · [Weekly review](#weekly-review) · [Monthly review](#monthly-review)
· [Quarterly gate](#quarterly-gate) · [Annual review](#annual-review) · [Placement](#placement)
· [Editing the curriculum](#editing-the-curriculum) · [Slumps and burnout](#slumps-and-burnout)
· [Travel, illness, busy weeks](#travel-illness-busy-weeks) · [New computer](#new-computer)

---

## Start the day
1. Cue fires (alarm / coffee / desk). Phone goes in another room.
2. Run `today` (or double-click **Start the day**). It syncs from GitHub and opens today's link.
3. Warm-up: clear Anki, then the snack on the card. 5–10 minutes.
4. Deep block on the session shown. Produce something — notes in your own words, solved problems, code.

## Close the day
1. Run `today done` and answer four questions (minutes, what you did, one takeaway, any artifact).
2. Say **No** to "Finished?" if the session isn't done — it stays as next time's session. Never tick unfinished work.
3. It logs, ticks, updates the streak and `PROGRESS.md`, commits and pushes. Read the "next time" line — that's
   tomorrow's priming.

## The two-minute day
Ill, exhausted, chaotic day? Run `today`, open the link, do **one** problem (or read one page), then `today done`
with honest minutes. You kept the chain and the identity. That's a full win on a day like that.

## Restart
Missed a day: the card warns you — today matters most. **Never miss twice.**
Missed several: no guilt, no "catching up" (that's how people burn out on day one back). Warm-up + 30 minutes today,
full block tomorrow. The streak resets; the *never-missed-twice* run and your total days don't care — keep building.

## Swap or bonus
- `today swap TRACK` — study something else today. Fine any time; choice keeps this enjoyable. It's logged.
- `today more` — after your block, an optional extra on your most neglected track. Bonuses are where physics, CS and
  programming catch up. Never let a bonus replace the next day's block.

## Module kickoff
The first session of a module (the card says "New"). Spend two minutes before starting:
1. Read the module's **Goal** and **Gate artifact** — know what "done" will look like.
2. Glance at the prerequisites in the comment line; if one isn't done, consider `today swap` to it first.
3. Open the first resource and bookmark it. Create `tracks/<track>/<module-id>/` from `templates/topic.md` for notes.

## Module close-out
When `today done` says MODULE COMPLETE:
1. Produce the **gate artifact** (if it isn't already) and commit it into the module folder.
2. Write the topic note: what you can now do, the hard part explained simply (the Feynman test), open questions.
3. Make Anki cards for anything you want to keep from the module.
4. Take the reward from your list in HABITS.md. Celebrate properly — this is a real milestone.

## When you're stuck
Work down the ladder; stop as soon as you're moving again:
1. **Re-read slowly** and work a simpler example by hand.
2. **Try a different explanation** — another resource on the same topic (3Blue1Brown, Khan, StatQuest, a different text).
3. **Shrink the problem** — what's the smallest piece you *can* do?
4. **Search** the exact question; read two answers.
5. **Ask** — a community, a mentor, or an AI tutor (see below).
6. **Flag and move on** — write the question under "Open questions", tick nothing, and continue next block. Being
   stuck for one session is normal; being stuck for a week is a signal to step back a rung (say so in the weekly review).

## Using AI without cheating yourself
AI is a superb tutor and a terrible substitute for thinking. Rules:
1. **Attempt first.** At least 15–20 honest minutes before asking.
2. **Ask for hints, not answers.** "Give me a hint, not the solution." "What concept am I missing?"
3. **Use it to check, explain and quiz** — "explain why my proof fails", "quiz me on this chapter".
4. **Never let it produce a gate artifact.** The artifact is the proof that *you* can do it.
5. **Re-derive anything it shows you**, from a blank page, without looking.

## Making Anki cards
- **One fact per card.** Small and atomic beats big and vague.
- **Understand before you memorise.** Cards are for keeping what you understood, not for skipping understanding.
- **Prefer cloze deletions** for definitions and formulas; use LaTeX for maths.
- **Make your own cards** — writing them is half the learning. Use the module's "Anki seeds" as a starting list.
- **Do reviews daily** (it's the warm-up) and **delete cards you hate** — a deck you resent is a deck you'll abandon.

## Weekly review
Sunday, 30–45 minutes. Run `today week` — it creates `review/weekly/YYYY-Www.md` pre-filled with the week's days,
hours, completed sessions and your logged takeaways. Fill in: what landed, what didn't, the **Goldilocks check**
(too easy / right / too hard), the week's artifact, next week's intention, and "if ___ happens, I will ___".

## Monthly review
First Sunday of the month, in `review/monthly/YYYY-MM.md` (template in `templates/`). Skim the month's logs. Did the
spine advance? Advance a flagship project at least a little. One **curiosity block** this month with no curriculum.
Write a short public progress post if you're doing one.

## Quarterly gate
Every three months, in `review/quarterly/YYYY-Qn.md` (template in `templates/`):
1. Which modules finished, with their gate artifacts?
2. Is the pace matching [TRAJECTORY.md](TRAJECTORY.md)? Edit the trajectory honestly — slide dates, don't fake them.
3. **Re-weight the schedule** in `system/config.toml` for the next quarter (e.g. less maths once foundations are done,
   more AI/ML or quant).
4. Re-read HABITS.md. Renew or adjust the habit contract.

## Annual review
Once a year: read the whole year's reviews. Write a one-page "year in learning" — what you can now do that you
couldn't, the best artifacts, what you'd change. Publish it. Update TRAJECTORY.md for the next year.

## Placement
The first session of each rung is a placement. Do it honestly under real conditions, then tick sessions you already
own and append `(placed out)` — e.g. `- [x] M02.S03 — … (placed out)`. If you're unsure whether you own something,
**don't** place out: a quick review is cheap, a hidden gap is expensive. You can always do a session fast.

## Editing the curriculum
The curriculum is yours — change it as you learn more about what you need. Format rules (so `today` can read it):
- A module is `## <ID> · <Title>` (IDs like `M14`, `C03`), then a comment `<!-- rung: U | prereq: … | feeds: … -->`.
- Then `**Goal:**`, `**Resources:**` (a bullet list), `**Sessions:**`, `**Gate artifact:**`, optional `**Anki seeds:**`.
- A session is `- [ ] <ModuleID>.S<NN> — <what to do>`. IDs must be unique. Work goes strictly top to bottom.
- Run `today doctor` after editing — it validates every module and session.
When a link dies, search the resource by name, replace the link, commit. When you finish a track's last module,
write the next rung — that's research-level planning, and it's part of the work.

## Slumps and burnout
Signs: dreading the block, three weeks of "in progress", resenting the deck. Response:
1. **Shrink, don't stop.** Two weeks of two-minute days is far better than quitting.
2. **Check the Goldilocks zone** — slumps are often boredom (too easy) or overwhelm (too hard). Adjust the rung.
3. **Add play:** a week of Project Euler, Bandit, a Kaggle competition, a fun build.
4. **Prune the deck** ruthlessly.
5. **Re-read TRAJECTORY.md** — reconnect to why.
6. Sleep, exercise and food beat any study technique. Protect them.

## Travel, illness, busy weeks
- Plan it in the weekly review: "Next week is travel → two-minute days, Anki on my phone."
- Anki on the phone keeps memory alive anywhere. Reading a resource on the phone counts as a block.
- The rule still holds: never miss twice. The minimum is always enough.

## New computer
1. Install Git and Python 3.11+.
2. `git clone https://github.com/Abdirahmanjabdi/Chaos.git` into a normal folder (not OneDrive/iCloud/Dropbox).
3. `git config --global user.name "…"` and `user.email "…"` if they aren't set.
4. Run `today doctor` (Windows) or `./today.sh doctor` (macOS/Linux). Fix anything marked FIX.
5. Sign into Anki/AnkiWeb so the deck syncs. You're done — `today` will pull the latest progress each time.
