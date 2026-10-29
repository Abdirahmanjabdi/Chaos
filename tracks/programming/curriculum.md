# Programming & Algorithms

The craft: writing code fluently, in several paradigms, with algorithmic sharpness. You said writing code is the weak
spot — so this track gets help from everywhere: the Tuesday/Thursday warm-up is a daily Exercism rep, DataPulse is
real code every week, and AI/ML is built from scratch rather than imported.

**How to use this file.** Strictly top to bottom; `today` shows the first unticked session. Attempt before you look
anything up; when you do look, close the tab and rewrite it yourself. **Levels:** F · S · U · G · R (see `CURRICULUM.md`).

## G01 · Python, Properly
<!-- rung: F | prereq: none | feeds: DataPulse, AI/ML, every script you write -->
**Goal:** Go from "I can make Python work" to writing idiomatic, typed, tested Python you'd be happy to show a senior engineer.
**Resources:**
- [Exercism — Python track](https://exercism.org/tracks/python) — free, with human mentors
- [The Python Tutorial](https://docs.python.org/3/tutorial/) — the official one; better than it looks
- Ramalho — *Fluent Python* (paid, the best book once you're past basics)
**Sessions:**
- [ ] G01.S01 — Placement: solve five [Exercism Python](https://exercism.org/tracks/python) exercises; note what felt slow or unfamiliar; reread `practice/01_candles` with fresh eyes.
- [ ] G01.S02 — The data model: dunder methods, the iteration protocol, comprehensions.
- [ ] G01.S03 — Functions as objects: closures, decorators, `functools`.
- [ ] G01.S04 — Iterators and generators; `itertools`; lazy pipelines.
- [ ] G01.S05 — Typing: type hints, `mypy --strict`, dataclasses, Protocols.
- [ ] G01.S06 — Errors and context managers; testing with pytest (fixtures, parametrize).
- [ ] G01.S07 — Tooling: uv, ruff, `pyproject.toml` — a project set up the modern way.
- [ ] G01.S08 — asyncio fundamentals (you'll need them for DataPulse).
- [ ] G01.S09 — Build: a typed, tested CLI tool — e.g. a trade-journal analyser — ruff and mypy clean.
**Gate artifact:** the CLI tool (typed, tested, linted) + 25 Exercism exercises, with mentor feedback requested on 3.
**Anki seeds:** the iteration protocol · decorator skeleton · generator vs list · common `itertools` · pytest fixtures

## G02 · The Missing Semester: Tools of the Trade
<!-- rung: F | prereq: G01 | feeds: everything — this is daily friction removed -->
**Goal:** Remove friction from everything else by mastering the shell, an editor, git and debugging tools.
**Resources:**
- [MIT — The Missing Semester of Your CS Education](https://missing.csail.mit.edu)
- [Pro Git](https://git-scm.com/book) — free book
**Sessions:**
- [ ] G02.S01 — The shell and shell tools.
- [ ] G02.S02 — Editors (pick one and learn it deeply) and data wrangling (grep, sed, awk, jq).
- [ ] G02.S03 — The command-line environment: job control, tmux, dotfiles, SSH.
- [ ] G02.S04 — Version control: git's data model — blobs, trees, commits, refs (Pro Git ch. 10 for the internals).
- [ ] G02.S05 — Debugging and profiling.
- [ ] G02.S06 — Metaprogramming (build systems, CI) and security/cryptography basics.
**Gate artifact:** a public dotfiles repo + a write-up "how git actually stores my work", with diagrams.

## G03 · Algorithmic Problem Solving
<!-- rung: U | prereq: G01, cs C03 in parallel | feeds: interviews, clean thinking -->
**Goal:** Pattern fluency — recognise the shape of a problem and reach for the right technique, with the reasoning written down.
**Resources:**
- [NeetCode roadmap](https://neetcode.io/roadmap) — the curated 150, with video explanations
- [LeetCode](https://leetcode.com)
- [Erickson — Algorithms](https://jeffe.cs.illinois.edu/teaching/algorithms/) — free, for the theory
**Sessions:**
- [ ] G03.S01 — Arrays and hashing: 5–6 problems, each with a written "why this approach".
- [ ] G03.S02 — Two pointers and sliding window.
- [ ] G03.S03 — Stack and binary search.
- [ ] G03.S04 — Linked lists and trees.
- [ ] G03.S05 — Tries and heaps.
- [ ] G03.S06 — Backtracking.
- [ ] G03.S07 — Graphs: BFS, DFS, union–find, topological sort.
- [ ] G03.S08 — 1-D dynamic programming.
- [ ] G03.S09 — 2-D dynamic programming.
- [ ] G03.S10 — Greedy and intervals.
- [ ] G03.S11 — Bit manipulation and maths.
- [ ] G03.S12 — Mock interviews: two timed problems, explaining aloud as you go.
**Gate artifact:** the NeetCode 150 solved, each with a short "why this approach" note — repeat sessions until each pattern feels obvious.

## G04 · C: Close to the Machine
<!-- rung: U | prereq: G02 | feeds: cs C05/C06, systems, everything low-level -->
**Goal:** Manage memory yourself — pointers, allocation, undefined behaviour — and understand what higher-level languages hide.
**Resources:**
- [Beej's Guide to C Programming](https://beej.us/guide/bgc/) — free
- [Exercism — C track](https://exercism.org/tracks/c)
- Kernighan & Ritchie — *The C Programming Language* (paid, short and classic)
**Sessions:**
- [ ] G04.S01 — The toolchain: gcc/clang, make, the compile and link stages.
- [ ] G04.S02 — Types, operators, control flow — and undefined behaviour.
- [ ] G04.S03 — Pointers and arrays; pointer arithmetic.
- [ ] G04.S04 — Strings and memory: malloc/free; valgrind and AddressSanitizer.
- [ ] G04.S05 — Structs, unions, function pointers.
- [ ] G04.S06 — Build: a dynamic array and a hash map, with tests.
- [ ] G04.S07 — Build: an arena allocator; benchmark it against malloc.
- [ ] G04.S08 — Debugging with gdb; writing a Makefile properly.
**Gate artifact:** a small C library (dynamic array, hash map, arena) — sanitizer-clean, tested and benchmarked.

## G05 · Rust: Safety and Speed
<!-- rung: U | prereq: G04 | feeds: systems S15, the low-latency edge, finance E10 -->
**Goal:** Write fast, safe systems code — ownership, traits, concurrency, async — the language of your low-latency work.
**Resources:**
- [The Rust Programming Language (the Book)](https://doc.rust-lang.org/book/)
- [Rustlings](https://github.com/rust-lang/rustlings) — small exercises alongside the Book
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
**Sessions:**
- [ ] G05.S01 — Getting started, the guessing game, common concepts (the Book's opening chapters).
- [ ] G05.S02 — Ownership, borrowing and slices — plus the matching Rustlings.
- [ ] G05.S03 — Structs, enums and pattern matching.
- [ ] G05.S04 — Modules, collections, error handling with `Result` and `?`.
- [ ] G05.S05 — Generics, traits and lifetimes.
- [ ] G05.S06 — Testing; the Book's command-line project (minigrep).
- [ ] G05.S07 — Closures and iterators; smart pointers (Box, Rc, RefCell).
- [ ] G05.S08 — Fearless concurrency: threads, channels, Mutex, Arc.
- [ ] G05.S09 — Async Rust with tokio.
- [ ] G05.S10 — Build: a tokio WebSocket market-data client (the seed of DataPulse's Rust ingest path).
**Gate artifact:** Rustlings complete + the tokio market-data client, tested.
**Anki seeds:** the three ownership rules · borrow rules · when to use Box/Rc/RefCell/Arc · `?` desugaring

## G06 · SQL & Data Modelling
<!-- rung: U | prereq: G01 | feeds: systems S09, finance, every backend -->
**Goal:** Think in sets — joins, window functions, indexes — and model data so queries stay simple.
**Resources:**
- [SQLBolt](https://sqlbolt.com) — interactive lessons
- [Use The Index, Luke!](https://use-the-index-luke.com) — free
- [PostgreSQL documentation](https://www.postgresql.org/docs/)
**Sessions:**
- [ ] G06.S01 — SELECT, filtering and sorting ([SQLBolt](https://sqlbolt.com) lessons).
- [ ] G06.S02 — Joins of every kind.
- [ ] G06.S03 — Aggregation, GROUP BY, HAVING.
- [ ] G06.S04 — Subqueries and CTEs.
- [ ] G06.S05 — Window functions (essential for market data: running totals, lags, ranks).
- [ ] G06.S06 — Indexing: how B-trees serve queries (Use The Index, Luke).
- [ ] G06.S07 — Schema design, normalisation and constraints.
- [ ] G06.S08 — Build: load your trade history into Postgres and answer ten real questions in SQL.
**Gate artifact:** a SQL analytics pack over your own trading data, with EXPLAIN plans for the slowest queries.

## G07 · Functional Programming (OCaml)
<!-- rung: U | prereq: G03 | feeds: cs C12, clearer code in every language -->
**Goal:** Think in values, types and recursion — a paradigm that permanently improves how you write Python and Rust.
**Resources:**
- [OCaml Programming: Correct + Efficient + Beautiful (Cornell CS 3110)](https://cs3110.github.io/textbook/) — free, with videos
**Sessions:**
- [ ] G07.S01 — Basics: expressions, functions, the toplevel.
- [ ] G07.S02 — Data and types: lists, variants, records, pattern matching.
- [ ] G07.S03 — Higher-order programming: map, fold, filter.
- [ ] G07.S04 — Modules and functors.
- [ ] G07.S05 — Correctness: specifications, testing, proof.
- [ ] G07.S06 — Mutability, laziness, efficiency.
- [ ] G07.S07 — Build: the textbook's interpreter case study.
**Gate artifact:** the interpreter + an essay on what functional programming changed in how you write Python and Rust.

## G08 · Software Design & Testing
<!-- rung: U | prereq: G01, G05 | feeds: everything you'll maintain -->
**Goal:** Write code that stays easy to change — deep modules, honest names, tests that catch real bugs.
**Resources:**
- Ousterhout — *A Philosophy of Software Design* (paid, short)
- [Hypothesis — property-based testing](https://hypothesis.readthedocs.io)
**Sessions:**
- [ ] G08.S01 — Complexity: what actually makes code hard to change.
- [ ] G08.S02 — Deep vs shallow modules; information hiding.
- [ ] G08.S03 — Errors, naming, and comments that earn their place.
- [ ] G08.S04 — Testing strategy: unit, integration, property-based (Hypothesis).
- [ ] G08.S05 — Refactor an old project of yours and measure before/after (size, test time, complexity).
**Gate artifact:** a refactoring write-up with before/after numbers + a property-based test that found a real bug.

## G09 · Open-Source Contribution
<!-- rung: U | prereq: G08 | feeds: reputation, reading other people's code -->
**Goal:** Ship code into projects other people depend on — reading large codebases, following conventions, taking review.
**Resources:**
- GitHub "good first issue" labels in projects you use (FastAPI, polars, tokio, Prometheus, …)
- Each project's CONTRIBUTING guide
**Sessions:**
- [ ] G09.S01 — Choose a project you use; read CONTRIBUTING; build it locally; run its tests.
- [ ] G09.S02 — Find and claim a small issue (documentation or a bug).
- [ ] G09.S03 — Make the change, open the PR, respond to review.
- [ ] G09.S04 — A second contribution, a little bigger.
- [ ] G09.S05 — A third contribution.
**Gate artifact:** three merged pull requests in projects you depend on.

## G10 · C++ for Low Latency
<!-- rung: G | prereq: G05, cs C13 | feeds: finance E10, the trading-systems job market -->
**Goal:** The language most trading firms still run on — modern C++, memory, templates, and the memory model.
**Resources:**
- [learncpp.com](https://www.learncpp.com) — free and thorough
- CppCon talks (YouTube) — especially the low-latency ones
- Stroustrup — *A Tour of C++* (paid)
**Sessions:**
- [ ] G10.S01 — Modern C++ basics: types, references, RAII.
- [ ] G10.S02 — Classes, move semantics, the rule of zero/five.
- [ ] G10.S03 — Templates and the STL: containers, iterators, algorithms.
- [ ] G10.S04 — Memory: smart pointers, allocators, keeping the heap off the hot path.
- [ ] G10.S05 — Concurrency: `std::thread`, atomics, the memory model (compare with cs C13).
- [ ] G10.S06 — Build: a limit order book in C++; benchmark it against a Rust version.
**Gate artifact:** an order book in C++ and in Rust with a latency comparison (feeds finance E10).

## G11 · Craft Rituals
<!-- rung: U | prereq: G03 | feeds: fun, consistency, a public trail -->
**Goal:** Keep the craft playful with yearly rituals — the kind of practice you look forward to.
**Resources:**
- [Advent of Code](https://adventofcode.com) — every December
- [Project Euler](https://projecteuler.net) — maths + programming puzzles
**Sessions:**
- [ ] G11.S01 — Project Euler problems 1–25 (in Rust or Python).
- [ ] G11.S02 — Project Euler problems 26–50.
- [ ] G11.S03 — Advent of Code (December) in Rust — use bonus blocks; one star a day.
**Gate artifact:** a public Advent of Code repo for the year + your Euler solutions with notes.
