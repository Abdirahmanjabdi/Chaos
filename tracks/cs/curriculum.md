# Computer Science

From NAND gates to distributed consensus — deep, build-it-yourself CS. You have a degree; this is the version where
you build every layer with your own hands, so nothing above it is magic any more.

**How to use this file.** Strictly top to bottom; `today` shows the first unticked session. Most sessions are a
project or lab — they may take two blocks; tick only when done. Discrete maths lives in the maths track (M13) — do it
there. **Levels:** F · S · U · G · R (see `CURRICULUM.md`).

## C01 · How a Computer Works: Nand2Tetris I
<!-- rung: F | prereq: none | feeds: everything in CS -->
**Goal:** Build a working computer from a single NAND gate — logic, arithmetic, memory, CPU and assembler — so hardware stops being a black box.
**Resources:**
- [Nand2Tetris](https://www.nand2tetris.org) — the book *The Elements of Computing Systems*, free software and projects
**Sessions:**
- [ ] C01.S01 — Orientation: install the [Nand2Tetris](https://www.nand2tetris.org) software; write down your current mental model of "what a computer is" (you'll revisit it).
- [ ] C01.S02 — Project 1, Boolean logic: Not, And, Or, Xor, Mux, DMux and their multi-bit versions — from Nand.
- [ ] C01.S03 — Project 2, Boolean arithmetic: half and full adders, Add16, Inc16, the ALU.
- [ ] C01.S04 — Project 3, memory: DFF → Bit → Register → RAM8 … RAM16K, and the program counter.
- [ ] C01.S05 — Project 4, machine language: write Hack assembly (Mult, Fill).
- [ ] C01.S06 — Project 5, computer architecture: Memory, CPU, Computer.
- [ ] C01.S07 — Project 6, the assembler — write it in Python.
- [ ] C01.S08 — Write-up: revisit your S01 mental model. What changed?
**Gate artifact:** a working Hack computer + your Python assembler (tested on the course programs) + the mental-model write-up.

## C02 · Nand2Tetris II: VM, Compiler & OS
<!-- rung: F | prereq: C01 | feeds: C10, compilers, systems -->
**Goal:** Build the software stack on your computer — a VM, a compiler and an operating system — up to running your own game.
**Resources:**
- [Nand2Tetris](https://www.nand2tetris.org) — part II
**Sessions:**
- [ ] C02.S01 — Project 7, VM I: stack arithmetic and memory access.
- [ ] C02.S02 — Project 8, VM II: program flow and function calls.
- [ ] C02.S03 — Project 9, the high-level language: write a small Jack game.
- [ ] C02.S04 — Project 10, compiler I: tokenizer and parser.
- [ ] C02.S05 — Project 11, compiler II: code generation.
- [ ] C02.S06 — Project 12, the operating system: Math, String, Array, Output, Screen, Keyboard, Memory, Sys.
**Gate artifact:** a complete Jack → VM → Hack toolchain you wrote, running your own game.

## C03 · Data Structures & Algorithms I
<!-- rung: U | prereq: C01, programming G01 | feeds: everything; pair with programming G03 -->
**Goal:** The core structures and algorithms — implemented, analysed and *measured*, so complexity is something you've seen, not memorised.
**Resources:**
- [MIT 6.006 Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/)
- [Erickson — Algorithms](https://jeffe.cs.illinois.edu/teaching/algorithms/) — free textbook
- Cormen et al. — *Introduction to Algorithms* (CLRS, paid reference)
**Sessions:**
- [ ] C03.S01 — Algorithms and computation; asymptotic notation; models of computation.
- [ ] C03.S02 — Data structures and dynamic arrays; amortised analysis.
- [ ] C03.S03 — Sorting: insertion, merge, heap — implement and benchmark.
- [ ] C03.S04 — Hashing: hash tables, collisions, universal hashing.
- [ ] C03.S05 — Linear-time sorting (counting, radix) and the comparison lower bound.
- [ ] C03.S06 — Binary trees, BSTs, AVL balancing.
- [ ] C03.S07 — Binary heaps and priority queues.
- [ ] C03.S08 — Graphs: BFS and DFS; topological sort.
- [ ] C03.S09 — Shortest paths: Bellman–Ford and Dijkstra.
- [ ] C03.S10 — Benchmark write-up: predicted vs measured complexity for everything you built.
**Gate artifact:** a tested DS&A library + a benchmark report comparing asymptotic predictions with measurements.

## C04 · Algorithms II: Design & Analysis
<!-- rung: U | prereq: C03, math M13 | feeds: research, hard interviews, optimisation -->
**Goal:** Design algorithms, not just recall them — and prove they're correct.
**Resources:**
- [MIT 6.046J Design and Analysis of Algorithms](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/)
- [Erickson — Algorithms](https://jeffe.cs.illinois.edu/teaching/algorithms/)
**Sessions:**
- [ ] C04.S01 — Divide and conquer; the master theorem; FFT intuition.
- [ ] C04.S02 — Dynamic programming I: memoisation and the recipe (subproblems, recurrence, order).
- [ ] C04.S03 — Dynamic programming II: sequence alignment, knapsack, shortest paths again.
- [ ] C04.S04 — Greedy algorithms and exchange arguments; minimum spanning trees.
- [ ] C04.S05 — Network flow: max-flow min-cut, Ford–Fulkerson, applications.
- [ ] C04.S06 — Randomised algorithms; union–find; amortisation revisited.
- [ ] C04.S07 — NP-completeness: reductions and Cook–Levin intuition.
- [ ] C04.S08 — Approximation algorithms.
**Gate artifact:** correctness proofs for five algorithms you implemented + one NP-completeness reduction, written up.

## C05 · Computer Systems: A Programmer's Perspective
<!-- rung: U | prereq: C02, programming G04 | feeds: C06, performance, security -->
**Goal:** See what your programs really become — machine code, the memory hierarchy, linking, processes, virtual memory.
**Resources:**
- [CMU 15-213 Introduction to Computer Systems](https://www.cs.cmu.edu/~213/) — lectures (also on YouTube)
- [CS:APP self-study labs](https://csapp.cs.cmu.edu/3e/labs.html) — free handouts
- Bryant & O'Hallaron — *Computer Systems: A Programmer's Perspective* (paid)
**Sessions:**
- [ ] C05.S01 — Bits, bytes and integers; two's complement — Data Lab.
- [ ] C05.S02 — Floating point; machine-level programs (x86-64 basics).
- [ ] C05.S03 — Control, procedures and data in assembly — Bomb Lab (defuse it with gdb).
- [ ] C05.S04 — Buffer overflows and security — Attack Lab.
- [ ] C05.S05 — The memory hierarchy and caches — Cache Lab.
- [ ] C05.S06 — Linking; exceptional control flow; processes and signals — Shell Lab.
- [ ] C05.S07 — Virtual memory; dynamic memory allocation — Malloc Lab.
- [ ] C05.S08 — System I/O and network programming — Proxy Lab.
- [ ] C05.S09 — Concurrent programming with threads.
**Gate artifact:** Bomb Lab defused + your malloc implementation with throughput and utilisation numbers.

## C06 · Operating Systems
<!-- rung: U | prereq: C05 | feeds: systems S02/S10, concurrency C13 -->
**Goal:** How an OS virtualises the CPU and memory, coordinates concurrency, and persists data — then change a real kernel.
**Resources:**
- [OSTEP — Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) — free book
- [MIT 6.1810 Operating System Engineering (xv6)](https://pdos.csail.mit.edu/6.1810/) — labs
**Sessions:**
- [ ] C06.S01 — Virtualisation: processes, the process API, limited direct execution.
- [ ] C06.S02 — Scheduling: MLFQ, lottery, multiprocessor.
- [ ] C06.S03 — Memory: address spaces, translation, segmentation, free-space management.
- [ ] C06.S04 — Paging, TLBs, multi-level page tables, swapping.
- [ ] C06.S05 — xv6 lab: utilities and system calls.
- [ ] C06.S06 — Concurrency: threads, locks, lock-based data structures.
- [ ] C06.S07 — Condition variables, semaphores, common concurrency bugs.
- [ ] C06.S08 — xv6 lab: page tables / copy-on-write fork.
- [ ] C06.S09 — Persistence: I/O devices, disks, RAID, files and directories.
- [ ] C06.S10 — File-system implementation; crash consistency and journaling.
**Gate artifact:** xv6 labs (system calls + COW fork) passing + a write-up of a concurrency bug you reproduced and fixed.

## C07 · Computer Networking
<!-- rung: U | prereq: C05, systems S03 | feeds: C14, low latency -->
**Goal:** Build TCP yourself, so the network becomes something you understand rather than something that "just works".
**Resources:**
- [Computer Networks: A Systems Approach](https://book.systemsapproach.org) — free
- [Stanford CS144 Introduction to Computer Networking](https://cs144.github.io) — build TCP in C++
**Sessions:**
- [ ] C07.S01 — The layered model and sockets; a TCP client (the CS144 warm-up).
- [ ] C07.S02 — A reliable in-memory byte stream.
- [ ] C07.S03 — Reassembling out-of-order segments.
- [ ] C07.S04 — The TCP receiver: sequence numbers, windows, acknowledgements.
- [ ] C07.S05 — The TCP sender: retransmission timers, flow control.
- [ ] C07.S06 — The network layer: IP, ARP, routing (the CS144 network interface and router).
- [ ] C07.S07 — Congestion control, DNS, HTTP and TLS from the wire up.
**Gate artifact:** your TCP implementation passing the CS144 tests + a packet-capture write-up of your stack talking to the real internet.

## C08 · Databases
<!-- rung: U | prereq: C06, programming G06 | feeds: systems S09, every backend -->
**Goal:** How a database engine stores, indexes, executes, isolates and recovers — by building its pieces.
**Resources:**
- [CMU 15-445/645 Database Systems](https://15445.courses.cs.cmu.edu) — lectures + the BusTub projects
**Sessions:**
- [ ] C08.S01 — The relational model and SQL, revisited.
- [ ] C08.S02 — Storage: pages, heap files, tuple layout; buffer pool management.
- [ ] C08.S03 — BusTub project: the buffer pool manager.
- [ ] C08.S04 — Indexes: hash tables and B+trees.
- [ ] C08.S05 — BusTub project: a B+tree (or hash) index.
- [ ] C08.S06 — Query processing: sorting, joins, execution models.
- [ ] C08.S07 — Concurrency control: two-phase locking and MVCC.
- [ ] C08.S08 — Logging and recovery (ARIES).
**Gate artifact:** BusTub buffer pool + index passing the tests + an essay on how Postgres implements MVCC (ties to DataPulse).

## C09 · Theory of Computation
<!-- rung: U | prereq: math M13, C04 | feeds: C12, the limits of what's computable -->
**Goal:** What can be computed at all, and what can be computed efficiently — automata, Turing machines, decidability, complexity.
**Resources:**
- [MIT 18.404J Theory of Computation](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/) — Michael Sipser's own lectures
- Sipser — *Introduction to the Theory of Computation* (paid)
**Sessions:**
- [ ] C09.S01 — Finite automata and regular languages; DFA–NFA equivalence.
- [ ] C09.S02 — Regular expressions; the pumping lemma.
- [ ] C09.S03 — Context-free grammars and pushdown automata.
- [ ] C09.S04 — Turing machines; the Church–Turing thesis.
- [ ] C09.S05 — Decidability; the halting problem; reductions.
- [ ] C09.S06 — Time complexity: P, NP, NP-completeness.
- [ ] C09.S07 — Space complexity; PSPACE.
- [ ] C09.S08 — Build: a regex → NFA → DFA engine in Python.
**Gate artifact:** the regex engine (Thompson + subset construction) + the halting problem's undecidability proved in your own words.

## C10 · Interpreters & Compilers
<!-- rung: U | prereq: C02, programming G04 | feeds: C12, understanding every language you use -->
**Goal:** Build a real programming language twice — a tree-walking interpreter, then a bytecode VM with a garbage collector.
**Resources:**
- [Crafting Interpreters (Robert Nystrom)](https://craftinginterpreters.com) — free online
**Sessions:**
- [ ] C10.S01 — Part I: a map of the territory; the Lox language.
- [ ] C10.S02 — jlox: scanning.
- [ ] C10.S03 — jlox: representing code; parsing expressions.
- [ ] C10.S04 — jlox: evaluating expressions; statements and state.
- [ ] C10.S05 — jlox: control flow and functions.
- [ ] C10.S06 — jlox: resolving and binding; classes and inheritance.
- [ ] C10.S07 — clox: chunks of bytecode and a virtual machine.
- [ ] C10.S08 — clox: scanning on demand, compiling expressions, value types, strings.
- [ ] C10.S09 — clox: hash tables, global and local variables, jumps.
- [ ] C10.S10 — clox: calls, functions and closures.
- [ ] C10.S11 — clox: garbage collection.
- [ ] C10.S12 — clox: classes, methods, superclasses; optimisation.
**Gate artifact:** a complete clox (in C — or ported to Rust) + one language feature you designed and added yourself.

## C11 · Security & Cryptography
<!-- rung: U | prereq: math M13, C05 | feeds: systems S13, every system that touches money -->
**Goal:** How cryptography actually protects data — and how it breaks when it's used wrongly.
**Resources:**
- [Dan Boneh — Cryptography I](https://www.coursera.org/learn/crypto) — free to audit
- [Cryptopals crypto challenges](https://cryptopals.com)
**Sessions:**
- [ ] C11.S01 — Stream ciphers, the one-time pad, semantic security.
- [ ] C11.S02 — Block ciphers and modes of operation.
- [ ] C11.S03 — MACs, hash functions, authenticated encryption.
- [ ] C11.S04 — Public-key cryptography: Diffie–Hellman, RSA (revisit math M13), signatures.
- [ ] C11.S05 — Cryptopals set 1.
- [ ] C11.S06 — Cryptopals set 2.
- [ ] C11.S07 — Cryptopals set 3.
- [ ] C11.S08 — Cryptopals set 4.
**Gate artifact:** Cryptopals sets 1–4 solved, with write-ups of each attack.

## C12 · Programming Languages & Type Systems
<!-- rung: G | prereq: C10, C09, programming G07 | feeds: compilers, formal methods -->
**Goal:** The theory under every language — semantics, lambda calculus, type soundness, type inference.
**Resources:**
- [PLAI — Programming Languages: Application and Interpretation](https://www.plai.org) — free
- [Software Foundations](https://softwarefoundations.cis.upenn.edu) — free, in Coq
- Pierce — *Types and Programming Languages* (paid)
**Sessions:**
- [ ] C12.S01 — Interpreters as definitions; environments and closures (PLAI).
- [ ] C12.S02 — The lambda calculus; substitution; evaluation strategies.
- [ ] C12.S03 — The simply typed lambda calculus; type soundness (progress and preservation).
- [ ] C12.S04 — Type inference (Hindley–Milner) — implement unification.
- [ ] C12.S05 — Software Foundations: the opening chapters of *Logical Foundations* in Coq.
- [ ] C12.S06 — Polymorphism, subtyping and effects — an overview.
**Gate artifact:** a type checker with Hindley–Milner inference for a small language, with tests.

## C13 · Concurrency & Parallelism
<!-- rung: G | prereq: C06, programming G05 | feeds: systems S15, programming G10 -->
**Goal:** Correct and fast concurrent code — atomics, memory ordering, lock-free structures — measured, not guessed.
**Resources:**
- [Mara Bos — Rust Atomics and Locks](https://marabos.nl/atomics/) — free online
- [Paul McKenney — Is Parallel Programming Hard, And If So, What Can You Do About It?](https://mirrors.edge.kernel.org/pub/linux/kernel/people/paulmck/perfbook/perfbook.html) — free
- [MIT 6.172 Performance Engineering](https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/)
**Sessions:**
- [ ] C13.S01 — Threads, data races, and why concurrency is hard.
- [ ] C13.S02 — Atomics and memory ordering: Relaxed, Acquire/Release, SeqCst.
- [ ] C13.S03 — Build a spin lock, a mutex and a condition variable.
- [ ] C13.S04 — Channels and message passing.
- [ ] C13.S05 — Lock-free data structures; the ABA problem.
- [ ] C13.S06 — Build: a lock-free single-producer/single-consumer ring buffer with cache-line padding — benchmark it.
- [ ] C13.S07 — Parallel algorithms and work stealing (6.172).
**Gate artifact:** the SPSC ring buffer with latency histograms (it feeds DataPulse Phase 10, systems S15).

## C14 · Distributed Systems
<!-- rung: G | prereq: C07, C13 | feeds: systems S12, research -->
**Goal:** Build fault-tolerant systems out of unreliable machines — RPC, replication and Raft consensus.
**Resources:**
- [MIT 6.5840 Distributed Systems](https://pdos.csail.mit.edu/6.824/) — lectures + Go labs
- Kleppmann — *Designing Data-Intensive Applications* (paid, the best companion)
**Sessions:**
- [ ] C14.S01 — Why distributed; RPC and threads in Go (do a Go crash course first).
- [ ] C14.S02 — Lab: MapReduce.
- [ ] C14.S03 — Lab: a key/value server with linearizability.
- [ ] C14.S04 — Raft: leader election.
- [ ] C14.S05 — Raft: log replication.
- [ ] C14.S06 — Raft: persistence.
- [ ] C14.S07 — Raft: log compaction and snapshots.
- [ ] C14.S08 — A fault-tolerant key/value service on Raft.
- [ ] C14.S09 — Consistency models, CAP, and consensus in practice (the Spanner and ZooKeeper papers).
**Gate artifact:** Raft passing every 6.5840 test (run them 100 times to shake out races) + a design write-up.

## C15 · Computer Architecture & Performance Engineering
<!-- rung: G | prereq: C05, C13 | feeds: systems S15, low latency -->
**Goal:** Know what the CPU is doing — pipelines, caches, branch prediction, SIMD — and use it to make code fast.
**Resources:**
- [MIT 6.172 Performance Engineering of Software Systems](https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/)
- Onur Mutlu's computer-architecture lectures (YouTube, free)
- Hennessy & Patterson — *Computer Architecture: A Quantitative Approach* (paid)
**Sessions:**
- [ ] C15.S01 — Pipelining and hazards.
- [ ] C15.S02 — Caches in depth; cache-oblivious algorithms.
- [ ] C15.S03 — Branch prediction and out-of-order execution.
- [ ] C15.S04 — SIMD and vectorisation.
- [ ] C15.S05 — Measuring: hardware counters, flame graphs, the roofline model.
- [ ] C15.S06 — Case study: speed a real program up 10× and explain every step.
**Gate artifact:** a performance case study with before/after numbers and hardware-counter evidence.

## C16 · Formal Methods
<!-- rung: G | prereq: C14 | feeds: correctness of anything that matters -->
**Goal:** Specify systems precisely and let a model checker find the bugs your tests can't.
**Resources:**
- [Learn TLA+](https://learntla.com)
- Leslie Lamport's TLA+ video course (free)
- [Software Foundations](https://softwarefoundations.cis.upenn.edu)
**Sessions:**
- [ ] C16.S01 — Why specify: TLA+ basics; model checking with TLC.
- [ ] C16.S02 — Specify a simple concurrent algorithm and find a bug with the model checker.
- [ ] C16.S03 — Specify the DataPulse ingest/reconnect protocol.
- [ ] C16.S04 — Specify (a simplified) Raft and check its safety properties.
**Gate artifact:** a TLA+ spec of a real protocol, with a model-checker-found bug documented.

## C17 · Research: Systems Papers
<!-- rung: R | prereq: C14 | feeds: your niche -->
**Goal:** Read systems research critically and reproduce it.
**Resources:**
- SOSP / OSDI / NSDI / EuroSys proceedings (open access)
- [The Morning Paper archive](https://blog.acolyer.org) — paper summaries
**Sessions:**
- [ ] C17.S01 — Read three classics (MapReduce, GFS, Dynamo); a one-page summary of each.
- [ ] C17.S02 — Read three recent papers in your niche (low latency, storage or distributed systems).
- [ ] C17.S03 — Reproduce one paper's key experiment.
- [ ] C17.S04 — Write it up as a short reproduction report.
**Gate artifact:** a published reproduction report.
