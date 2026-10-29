# Coding Interviews

The hardest block of the day, so it goes **first**, while your head is freshest. Goal: walk into any coding round —
a LeetCode-style medium, or the practical scripting round most DevOps/SRE loops use — and solve it out loud, cleanly,
in 25–35 minutes.

**How every session works (the method).**
1. **Timer on.** 25 min for a medium, 40 for a hard. No hints before the timer ends.
2. **Out loud, UMPIRE:** Understand (restate it, ask about edge cases) · Match (which pattern?) · Plan (pseudocode and
   Big-O *before* code) · Implement · Review (dry-run one example by hand) · Evaluate (time/space, alternatives).
3. **Stuck at the bell?** Climb the hint ladder one rung at a time: the pattern name → the NeetCode explanation's
   first 3 minutes → the full idea. **Never copy code**: close the tab and write it yourself.
4. **Commit the solution** to `tracks/coding/solutions/<module>/<problem>.py` with a three-line docstring: the
   pattern, *why* it works, the complexity. That's the artifact.
5. **Anything you didn't solve unaided** goes on `tracks/coding/redo.md`. Every module ends with a redo session.
6. **Score** for `today done`: problems solved unaided / attempted (e.g. `2/3`). That's your coding KPI.

Order follows the [NeetCode roadmap](https://neetcode.io/roadmap) — dependencies first (you can't do graphs before
trees, or DP before recursion). Hardest-first lives *in the day*, not in the order.

## LC01 · Placement & the Method
<!-- rung: S | prereq: none | feeds: every coding round -->
**Goal:** Know exactly which patterns you already own, and make the UMPIRE routine automatic before the real work starts.
**Resources:**
- [NeetCode roadmap](https://neetcode.io/roadmap) — the 150, with free video explanations
- [LeetCode](https://leetcode.com) — where you solve them
- [Tech Interview Handbook — coding interview prep](https://www.techinterviewhandbook.org/coding-interview-prep/) — free, the meta-skills
**Sessions:**
- [ ] LC01.S01 — Set up: LeetCode account, a `solutions/` folder, a Python template file. Solve Two Sum, Valid Anagram and Contains Duplicate *out loud* with UMPIRE.
- [ ] LC01.S02 — Placement: one medium from four patterns, timed — Top K Frequent Elements, Longest Substring Without Repeating Characters, Number of Islands, Climbing Stairs. Note which you got unaided; that's your baseline.
- [ ] LC01.S03 — Big-O and Python's real costs: list/dict/set/deque/heapq/bisect/sorted. Write the complexity of every solution so far; make a one-page cheat sheet.
**Gate artifact:** `solutions/LC01/` (7 problems with docstrings) + `tracks/coding/baseline.md` — patterns owned vs not.

## LC02 · Arrays & Hashing
<!-- rung: S | prereq: LC01 | feeds: almost every other pattern -->
**Goal:** Reach for a hash map or set by reflex whenever you need "have I seen this?" or "how many of these?".
**Resources:**
- [NeetCode roadmap](https://neetcode.io/roadmap) — Arrays & Hashing
- [Python docs — collections](https://docs.python.org/3/library/collections.html) — Counter, defaultdict
**Sessions:**
- [ ] LC02.S01 — Group Anagrams · Top K Frequent Elements (do it twice: heap, then bucket sort).
- [ ] LC02.S02 — Product of Array Except Self · Valid Sudoku.
- [ ] LC02.S03 — Encode and Decode Strings · Longest Consecutive Sequence.
- [ ] LC02.S04 — Redo: re-solve from blank everything on `redo.md` for this module, timed.
**Gate artifact:** `solutions/LC02/` + every problem re-solved unaided at least once.

## LC03 · Two Pointers
<!-- rung: S | prereq: LC02 | feeds: sliding window, linked lists -->
**Goal:** Spot when a sorted array (or two ends moving inward) turns O(n²) into O(n).
**Resources:**
- [NeetCode roadmap](https://neetcode.io/roadmap) — Two Pointers
**Sessions:**
- [ ] LC03.S01 — Valid Palindrome · Two Sum II.
- [ ] LC03.S02 — 3Sum · Container With Most Water.
- [ ] LC03.S03 — Trapping Rain Water (your first hard: 40 min, then the two-pointer proof in your own words).
- [ ] LC03.S04 — Redo session + a half-page note: "when two pointers works, and why".
**Gate artifact:** `solutions/LC03/` + the "when it works" note.

## LC04 · Sliding Window
<!-- rung: S | prereq: LC03 | feeds: streaming problems, rate limiters -->
**Goal:** Grow and shrink a window with an invariant you can say out loud.
**Resources:**
- [NeetCode roadmap](https://neetcode.io/roadmap) — Sliding Window
**Sessions:**
- [ ] LC04.S01 — Best Time to Buy and Sell Stock · Longest Substring Without Repeating Characters.
- [ ] LC04.S02 — Longest Repeating Character Replacement · Permutation in String.
- [ ] LC04.S03 — Minimum Window Substring (hard).
- [ ] LC04.S04 — Sliding Window Maximum (monotonic deque) + redo.
**Gate artifact:** `solutions/LC04/` + a reusable window template in your cheat sheet.

## LC05 · Stack
<!-- rung: S | prereq: LC02 | feeds: parsing, monotonic-stack problems -->
**Goal:** Use a stack for matching and "next greater" problems, including the monotonic-stack trick.
**Resources:**
- [NeetCode roadmap](https://neetcode.io/roadmap) — Stack
**Sessions:**
- [ ] LC05.S01 — Valid Parentheses · Min Stack · Evaluate Reverse Polish Notation.
- [ ] LC05.S02 — Daily Temperatures · Car Fleet (monotonic stack).
- [ ] LC05.S03 — Generate Parentheses · Largest Rectangle in Histogram (hard).
- [ ] LC05.S04 — Redo session.
**Gate artifact:** `solutions/LC05/`.

## LC06 · Binary Search
<!-- rung: S | prereq: LC02 | feeds: search-on-the-answer, systems capacity questions -->
**Goal:** Write a bug-free binary search from a stated invariant, and binary-search *the answer* when there's no array.
**Resources:**
- [NeetCode roadmap](https://neetcode.io/roadmap) — Binary Search
- [Python docs — bisect](https://docs.python.org/3/library/bisect.html)
**Sessions:**
- [ ] LC06.S01 — Binary Search · Search a 2D Matrix. Write your one template (lo/hi, the invariant, the exit condition).
- [ ] LC06.S02 — Koko Eating Bananas (search on the answer) · Find Minimum in Rotated Sorted Array.
- [ ] LC06.S03 — Search in Rotated Sorted Array · Time Based Key-Value Store.
- [ ] LC06.S04 — Median of Two Sorted Arrays (hard — stretch) + redo.
**Gate artifact:** `solutions/LC06/` + the template with its invariant written as a comment.

## LC07 · Linked Lists
<!-- rung: S | prereq: LC03 | feeds: LRU cache (asked everywhere), pointer fluency -->
**Goal:** Manipulate pointers without losing nodes; build an LRU cache from scratch in 20 minutes.
**Resources:**
- [NeetCode roadmap](https://neetcode.io/roadmap) — Linked List
**Sessions:**
- [ ] LC07.S01 — Reverse Linked List (iterative *and* recursive) · Merge Two Sorted Lists · Linked List Cycle.
- [ ] LC07.S02 — Reorder List · Remove Nth Node From End of List · Add Two Numbers.
- [ ] LC07.S03 — Copy List with Random Pointer · Find the Duplicate Number.
- [ ] LC07.S04 — LRU Cache — twice: with `OrderedDict`, then with your own hash map + doubly linked list.
- [ ] LC07.S05 — Merge k Sorted Lists · Reverse Nodes in k-Group (hard).
- [ ] LC07.S06 — Redo session.
**Gate artifact:** `solutions/LC07/` + the hand-built LRU cache with tests.

## LC08 · Trees
<!-- rung: U | prereq: LC07 | feeds: tries, heaps, graphs, recursion everywhere -->
**Goal:** Think recursively: "what does each subtree hand back to its parent?", plus clean BFS.
**Resources:**
- [NeetCode roadmap](https://neetcode.io/roadmap) — Trees
**Sessions:**
- [ ] LC08.S01 — Invert Binary Tree · Maximum Depth · Same Tree · Subtree of Another Tree. Write your DFS template.
- [ ] LC08.S02 — Diameter of Binary Tree · Balanced Binary Tree (the "return two things" pattern).
- [ ] LC08.S03 — Binary Tree Level Order Traversal · Right Side View (BFS template with a deque).
- [ ] LC08.S04 — Lowest Common Ancestor of a BST · Validate BST · Kth Smallest Element in a BST.
- [ ] LC08.S05 — Count Good Nodes · Construct Binary Tree from Preorder and Inorder.
- [ ] LC08.S06 — Binary Tree Maximum Path Sum · Serialize and Deserialize Binary Tree (both hard).
- [ ] LC08.S07 — Redo session.
**Gate artifact:** `solutions/LC08/` + DFS and BFS templates in the cheat sheet.

## LC09 · Tries
<!-- rung: U | prereq: LC08 | feeds: autocomplete (a classic system-design question) -->
**Goal:** Build a trie from memory and know when it beats a hash set.
**Resources:**
- [NeetCode roadmap](https://neetcode.io/roadmap) — Tries
**Sessions:**
- [ ] LC09.S01 — Implement Trie · Design Add and Search Words Data Structure.
- [ ] LC09.S02 — Word Search II (hard) + redo.
**Gate artifact:** `solutions/LC09/`.

## LC10 · Heaps & Priority Queues
<!-- rung: U | prereq: LC08 | feeds: Dijkstra, schedulers, top-k systems -->
**Goal:** Use `heapq` fluently (including max-heaps and tuples) for top-k, streaming medians and scheduling.
**Resources:**
- [NeetCode roadmap](https://neetcode.io/roadmap) — Heap / Priority Queue
- [Python docs — heapq](https://docs.python.org/3/library/heapq.html)
**Sessions:**
- [ ] LC10.S01 — Kth Largest Element in a Stream · Last Stone Weight · K Closest Points to Origin.
- [ ] LC10.S02 — Kth Largest Element in an Array (heap vs quickselect) · Task Scheduler.
- [ ] LC10.S03 — Design Twitter · Find Median from Data Stream (two heaps).
- [ ] LC10.S04 — Redo session.
**Gate artifact:** `solutions/LC10/`.

## LC11 · Backtracking
<!-- rung: U | prereq: LC08 | feeds: DP (memoised backtracking is DP) -->
**Goal:** One backtracking template — choose, explore, un-choose — that covers subsets, permutations and searches.
**Resources:**
- [NeetCode roadmap](https://neetcode.io/roadmap) — Backtracking
**Sessions:**
- [ ] LC11.S01 — Subsets · Permutations. Write the template.
- [ ] LC11.S02 — Combination Sum · Combination Sum II · Subsets II (handling duplicates).
- [ ] LC11.S03 — Word Search · Palindrome Partitioning · Letter Combinations of a Phone Number.
- [ ] LC11.S04 — N-Queens (hard) + redo.
**Gate artifact:** `solutions/LC11/` + the template.

## LC12 · Graphs
<!-- rung: U | prereq: LC08 | feeds: dependency resolution (Terraform's graph, K8s controllers), network problems -->
**Goal:** BFS, DFS, topological sort and union-find, chosen by reflex. These map straight onto infra: `terraform
graph` *is* a topological sort.
**Resources:**
- [NeetCode roadmap](https://neetcode.io/roadmap) — Graphs
**Sessions:**
- [ ] LC12.S01 — Number of Islands · Max Area of Island (grid DFS template).
- [ ] LC12.S02 — Clone Graph · Rotting Oranges (multi-source BFS).
- [ ] LC12.S03 — Pacific Atlantic Water Flow · Surrounded Regions.
- [ ] LC12.S04 — Course Schedule I & II (topological sort — then explain how Terraform orders resource creation).
- [ ] LC12.S05 — Union-find: Redundant Connection · Number of Connected Components · Graph Valid Tree.
- [ ] LC12.S06 — Word Ladder (hard) + redo.
**Gate artifact:** `solutions/LC12/` + BFS / DFS / topo-sort / union-find templates.

## LC13 · Advanced Graphs
<!-- rung: G | prereq: LC12, LC10 | feeds: routing, networking questions -->
**Goal:** Shortest paths and minimum spanning trees, implemented from memory.
**Resources:**
- [NeetCode roadmap](https://neetcode.io/roadmap) — Advanced Graphs
**Sessions:**
- [ ] LC13.S01 — Network Delay Time (Dijkstra with a heap).
- [ ] LC13.S02 — Min Cost to Connect All Points (Prim) · Cheapest Flights Within K Stops (Bellman-Ford).
- [ ] LC13.S03 — Reconstruct Itinerary · Swim in Rising Water.
- [ ] LC13.S04 — Alien Dictionary (hard) + redo.
**Gate artifact:** `solutions/LC13/`.

## LC14 · 1-D Dynamic Programming
<!-- rung: G | prereq: LC11 | feeds: 2-D DP, optimisation thinking -->
**Goal:** Go recurrence → memoisation → table → constant space, saying the state and transition out loud.
**Resources:**
- [NeetCode roadmap](https://neetcode.io/roadmap) — 1-D Dynamic Programming
**Sessions:**
- [ ] LC14.S01 — Climbing Stairs · Min Cost Climbing Stairs · House Robber · House Robber II — all four ways (recursion, memo, table, O(1)).
- [ ] LC14.S02 — Longest Palindromic Substring · Palindromic Substrings · Decode Ways.
- [ ] LC14.S03 — Coin Change · Maximum Product Subarray.
- [ ] LC14.S04 — Word Break · Longest Increasing Subsequence · Partition Equal Subset Sum.
- [ ] LC14.S05 — Redo session.
**Gate artifact:** `solutions/LC14/` + for each problem, the state and the transition in one line.

## LC15 · 2-D Dynamic Programming
<!-- rung: G | prereq: LC14 | feeds: string/edit-distance problems -->
**Goal:** Define a 2-D state cleanly and fill the table in the right order.
**Resources:**
- [NeetCode roadmap](https://neetcode.io/roadmap) — 2-D Dynamic Programming
**Sessions:**
- [ ] LC15.S01 — Unique Paths · Longest Common Subsequence.
- [ ] LC15.S02 — Best Time to Buy and Sell Stock with Cooldown · Coin Change II · Target Sum.
- [ ] LC15.S03 — Interleaving String · Longest Increasing Path in a Matrix.
- [ ] LC15.S04 — Edit Distance · Distinct Subsequences.
- [ ] LC15.S05 — Burst Balloons · Regular Expression Matching (stretch) + redo.
**Gate artifact:** `solutions/LC15/`.

## LC16 · Greedy & Intervals
<!-- rung: U | prereq: LC02 | feeds: scheduling and capacity questions -->
**Goal:** Know when the locally best choice is provably safe, and sort-then-sweep for intervals.
**Resources:**
- [NeetCode roadmap](https://neetcode.io/roadmap) — Greedy, Intervals
**Sessions:**
- [ ] LC16.S01 — Maximum Subarray (Kadane) · Jump Game · Jump Game II.
- [ ] LC16.S02 — Gas Station · Hand of Straights · Partition Labels · Valid Parenthesis String.
- [ ] LC16.S03 — Insert Interval · Merge Intervals · Non-overlapping Intervals.
- [ ] LC16.S04 — Meeting Rooms I & II (sweep line / heap) · Minimum Interval to Include Each Query.
- [ ] LC16.S05 — Redo session.
**Gate artifact:** `solutions/LC16/`.

## LC17 · Maths, Matrices & Bits
<!-- rung: U | prereq: LC02 | feeds: the odd question that's "just" arithmetic -->
**Goal:** Clear the small-but-common category so it never costs you a round.
**Resources:**
- [NeetCode roadmap](https://neetcode.io/roadmap) — Math & Geometry, Bit Manipulation
**Sessions:**
- [ ] LC17.S01 — Rotate Image · Spiral Matrix · Set Matrix Zeroes.
- [ ] LC17.S02 — Happy Number · Plus One · Pow(x, n) · Multiply Strings.
- [ ] LC17.S03 — Single Number · Number of 1 Bits · Counting Bits · Reverse Bits · Missing Number · Sum of Two Integers.
**Gate artifact:** `solutions/LC17/` — and the NeetCode 150 is done.

## LC18 · Practical Coding for DevOps & SRE Rounds
<!-- rung: U | prereq: LC02 (can start any time after) | feeds: the "write a script" round most DevOps loops actually use -->
**Goal:** Write the production-flavoured scripts DevOps interviews ask for — parsing, retries, concurrency, AWS
calls — cleanly, with tests, in under 40 minutes.
**Resources:**
- [Python docs — concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)
- [Boto3 documentation](https://docs.aws.amazon.com/boto3/latest/)
- [ShellCheck](https://www.shellcheck.net) — lint every Bash script you write
**Sessions:**
- [ ] LC18.S01 — Log parsing: from an nginx access log, top 10 IPs, status-code counts and p95 latency — in Python, then the same with `awk`/`sort`/`uniq`.
- [ ] LC18.S02 — Rate limiter: token bucket and sliding-window counter classes, with pytest tests (thread-safe version as a stretch).
- [ ] LC18.S03 — An HTTP client with timeouts, retries, exponential backoff with jitter, and idempotency — explain why each matters.
- [ ] LC18.S04 — Concurrency: health-check 100 URLs with `ThreadPoolExecutor`, then `asyncio` with a semaphore; compare.
- [ ] LC18.S05 — System tasks: walk a directory tree for the largest files, rotate logs, run `subprocess` safely (no `shell=True`).
- [ ] LC18.S06 — Bash: a health-check / deploy script with `set -euo pipefail`, `trap`, `getopts` and functions — ShellCheck clean.
- [ ] LC18.S07 — boto3: list every unencrypted S3 bucket and untagged EC2 instance across regions, read-only, with `moto` tests.
- [ ] LC18.S08 — A TTL cache and a consistent-hashing ring — the bridge into system design.
**Gate artifact:** `solutions/LC18/` — eight tested scripts you'd be proud to share in an interview.

## LC19 · Interview Performance & Mocks
<!-- rung: G | prereq: LC08 + LC18 (start mocks early — don't wait for LC17) | feeds: offers -->
**Goal:** Turn knowing into performing: talk while you think, recover when stuck, finish on time.
**Resources:**
- [Pramp](https://www.pramp.com) — free peer mock interviews
- [interviewing.io](https://interviewing.io) — anonymous mocks, recordings to learn from
- [Tech Interview Handbook — mock interviews](https://www.techinterviewhandbook.org/mock-interviews/)
**Sessions:**
- [ ] LC19.S01 — Talk-aloud drill: re-solve two old mediums while recording yourself; watch it back and note every silence longer than 20 s.
- [ ] LC19.S02 — Timed mock: two random mediums in 45 minutes, no pausing.
- [ ] LC19.S03 — Peer mock (Pramp or similar). Score it honestly against the UMPIRE checklist.
- [ ] LC19.S04 — Timed mock: one hard in 45 minutes. Practise saying "here's the brute force; let me improve it".
- [ ] LC19.S05 — Clear the whole `redo.md` list.
- [ ] LC19.S06 — Company-tagged practice for the roles you're interviewing for right now.
- [ ] LC19.S07 — Final: three mocks in one week, all passed. Then repeat this module before every onsite.
**Gate artifact:** three passed mocks logged + an empty `redo.md`.
