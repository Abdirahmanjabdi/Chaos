# Writing Code: From Reader to Writer

## The diagnosis

Reading code is **recognition**. Writing code is **recall plus decomposition**. They're different skills, the same way understanding Italian is different from speaking it. Five years of reading built a big recognition vocabulary. That's a real asset, but it never trained the two things a blank file demands:

1. **Decomposition:** turning a vague goal into small, concrete steps
2. **Recall:** producing syntax and idioms from memory, not just recognising them

The blank-file freeze is almost always a decomposition problem pretending to be a syntax problem. You don't know what to type because you haven't decided what the *first small step* is.

---

## The method: never start with code

Use this every time, for every file, until it's automatic.

### Step 1: Write examples (input → output)
Before any code, write 2–3 concrete examples by hand:
```
trades = [(0, 100.0, 1), (30, 101.0, 2), (65, 99.0, 1)]
→ minute 0: open 100, high 101, low 100, close 101, volume 3
→ minute 1: open 99, high 99, low 99, close 99, volume 1
```
If you can't write the examples, you don't understand the problem yet, and no amount of typing will fix that.

### Step 2: Write the steps as comments, in plain English
```python
def build_candles(trades):
    # group trades by which minute they fall in
    # for each minute, in order:
    #     open = first price, close = last price
    #     high = max price, low = min price
    #     volume = sum of qty
    # return the candles in time order
```
The blank page is gone. Now you're translating English to Python, which is a much smaller problem.

### Step 3: Write the ugliest version that works
Fill in each comment with the dumbest code that works: nested loops, prints everywhere, no cleverness. **Make it run within 10 minutes**, even if it only handles one case.

### Step 4: Make the tests pass, one at a time
Run, read the error, fix *one* thing, run again. Short loops. Errors are information, not failure.

### Step 5: Then refactor
Only once it works: better names, extract functions, remove duplication, think about efficiency. Tests protect you while you clean up.

> Rule of thumb: **working → right → fast**, in that order, never skipping ahead.

---

## Daily practice (45–60 min/day)

Pick **Python** for all of this. Java and JS spread you thin, and Python is the DataPulse language. Rust comes later, in Phase 10.

**Turn off AI autocomplete (Copilot etc.) during practice.** It does the exact recall work you need to build. Use it on real work later, once you can write without it.

| Block | Time | What |
|---|---|---|
| Recall drill | 10 min | Write a common task from memory, no looking things up first (list below). Look up only after you're stuck for 3 minutes. |
| Main exercise | 30–40 min | One exercise from `practice/`, using the 5-step method |
| Rewrite | 10 min | Take any function you *read* today (work, GitHub, docs) and rewrite it from memory in a blank file. This turns your reading strength into writing reps. |

### Recall drill list (repeat until boring)
Read a file line by line · parse JSON and pull out nested fields · count things with a dict, then with `Counter` · sort a list of dicts by a key · group items by key with `defaultdict` · make an HTTP GET and handle errors · write a CLI with `argparse` · a class with `__init__`, `__repr__`, and a method · a dataclass · read/write CSV · a generator function · a decorator that times a function · `try/except/finally` with a custom exception · an `async` function that awaits two things concurrently · a regex that pulls numbers out of a string · run a shell command with `subprocess` and capture its output

### Algorithms: patterns, not grinding
Most interview and real-world algorithm problems are ~15 patterns. Learn them as patterns:

1. Hash map lookups and counting
2. Two pointers
3. Sliding window
4. Prefix sums
5. Binary search (including "search on the answer")
6. Stack (monotonic stack)
7. Queue / BFS
8. DFS / recursion / backtracking
9. Heaps (top-k, merging sorted streams)
10. Intervals (merge, overlap)
11. Linked list manipulation
12. Trees (traversals, recursion on subtrees)
13. Graphs (topological sort, union-find, shortest path)
14. Dynamic programming (1D first, then 2D)
15. Greedy

Use the **NeetCode 150** list, grouped by pattern. Loop for each problem:
1. Attempt for 25 minutes using the 5-step method
2. Stuck? Read the solution and understand *why* it works
3. **Close it. Rewrite from scratch** without looking
4. Re-solve it from blank **3 days later**, then **a week later**. If you can't, it wasn't learned.

Many of these patterns are exactly what trading systems use: heaps for order books and merging feeds, sliding windows for moving averages and rate limits, prefix sums for VWAP, binary search over sorted ticks.

### Code quality
- Read *A Philosophy of Software Design* (Ousterhout). It's short, and the best book on "what makes code good."
- Every exercise gets a refactor pass (Step 5).
- Send me finished exercises for review. I'll review them like a senior engineer would.

---

## Progression

| Weeks | Focus | Scaffolding |
|---|---|---|
| 1–2 | Small, domain-flavoured exercises | I give the tests and function signature |
| 3–4 | Same, plus algorithm patterns 1–5 | I give the tests only. You design the function. |
| 5–6 | Scripting real tools (CLI, file processing, HTTP) | I give a one-paragraph spec. You write the tests too. |
| 7+ | DataPulse Phase 0–1, written by you | Only the roadmap |

By week 7 a blank file should feel like the start of Step 1, not a wall.
