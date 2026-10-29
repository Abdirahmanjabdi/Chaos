# CURRICULUM — the ladders

Seven tracks. Each is a **ladder**: rungs from a stated starting level up to research-level, every rung ending in a
**gate artifact** — the committed thing that proves you actually cleared it, not just read about it. Pace is set by
[TRAJECTORY](TRAJECTORY.md) and the spine chosen there; you do not climb all seven at the same speed.

Levels used across tracks: **F** foundation · **S** school-leaving (A-level) · **U** undergraduate · **G** graduate ·
**R** research edge.

> Calibration needed: your true current rung on each ladder. The placements below are *defaults* — we correct them
> in the first weekly review. Tell me where you actually are and I'll move the marker.

---

## 1. Mathematics — the language everything else is written in
*Start: ~Year 9. This track is load-bearing for physics, ML, quant, CS. Prioritise it early; it pays compound interest.*

- **F · School algebra→GCSE** — algebra, functions, geometry, trig, coordinate geometry, probability. *Gate:* a clean
  problem set + a "why does the quadratic formula work" derivation.
- **S · A-level core** — differential & integral calculus, sequences/series, vectors, complex numbers, intro proof,
  mechanics & statistics. *Gate:* derive the derivatives of the standard functions from first principles; a proof portfolio.
- **U1 · Rigour begins** — linear algebra (vectors→spaces→eigenstuff, *do it properly*: Axler), real analysis
  (limits, continuity, ε–δ: Abbott/Rudin), multivariable calculus. *Gate:* prove a handful of core theorems yourself; a
  `numpy` linear-algebra mini-library.
- **U2 · The working toolkit** — probability & statistics (to random variables, distributions, CLT), ODEs & PDEs,
  numerical methods, intro optimization. *Gate:* a numerical ODE solver + an honest statistics write-up.
- **G · Depth for the spine** — measure-theoretic probability, **stochastic calculus** (Brownian motion, Itô — the
  gateway to quant & diffusion models), functional analysis, optimization/convexity. *Gate:* derive Itô's lemma; solve the
  Black–Scholes PDE two ways.
- **R** — a chosen specialization (e.g. stochastic processes / high-dimensional probability / optimization) read at paper level.

*Tools:* pen & paper (primary), LaTeX for write-ups, Python (SymPy/NumPy) to check and visualise, Anki for theorems.
*Spine texts:* Spivak/Abbott, Axler, Rudin, Ross/Blitzstein (prob), Shreve II (stochastic calc).

## 2. Physics — the best training in mathematical modelling of the real world
*Start: ~GCSE. How far this goes depends on whether it's your spine or your disciplined secondary (see TRAJECTORY).*

- **F · GCSE** — mechanics, electricity, waves, energy. *Gate:* derive the kinematics equations; a measurement write-up.
- **S · A-level** — fields (gravitational/electric/magnetic), thermodynamics, oscillations, intro quantum & nuclear.
  *Gate:* a projectile/orbit simulation with the physics explained.
- **U1 · Classical core** — Newtonian→**Lagrangian & Hamiltonian** mechanics (Taylor), electromagnetism (Griffiths),
  special relativity. *Gate:* derive Lagrange's equations; simulate a double pendulum and explain the chaos.
- **U2 · The modern pillars** — quantum mechanics (Griffiths/Shankar), statistical mechanics, intro general
  relativity. *Gate:* solve the infinite well & harmonic oscillator; an Ising-model Monte-Carlo simulation.
- **G · Specialism** — QFT or condensed matter or astrophysics (pick one), advanced stat mech. *Gate:* a graduate
  problem set + a derivation essay.
- **R** — reading and reproducing results in the chosen area.

*Tools:* the maths track is the prerequisite; Python for simulation; LaTeX. *Spine texts:* Feynman Lectures (companion),
Kleppner, Taylor, Griffiths (E&M + QM), Blundell (stat mech).

## 3. Computer Science — deep, not bootcamp
*Start: working programmer. Goal: understand the machine from transistors to distributed consensus.*

- **F · How a computer actually works** — binary/logic, architecture, memory. *Gate:* **Nand2Tetris** — build a CPU &
  assembler from NAND gates.
- **U1 · The core four** — data structures & algorithms (CLRS, with real complexity analysis), discrete maths, theory of
  computation (automata, computability, P/NP), systems programming in C (CSAPP). *Gate:* implement the classic DS/algos
  with benchmarks; a small C program that explains the memory hierarchy.
- **U2 · Systems** — operating systems (xv6), networking (TCP/IP from the socket up), databases (storage, indexing,
  transactions), compilers. *Gate:* **Crafting Interpreters** (build a language); a toy DB or a working TCP service.
- **G · Distributed & advanced** — concurrency, distributed systems (MIT 6.824), consensus (**Raft**), programming
  language theory & type systems, formal methods. *Gate:* implement Raft; a type-checker.
- **R** — read SOSP/OSDI-level papers; reproduce one.

*Tools:* C & Rust, Linux, Git, gdb. *Spine:* Nand2Tetris, CSAPP, CLRS, SICP, Crafting Interpreters, MIT 6.824.

## 4. Programming & Algorithms — the craft
*Start: Python-fluent. Goal: multi-paradigm fluency + algorithmic sharpness.*

- **Language ladder:** deepen **Python** (idioms, async, performance) → **C** (memory, pointers, the machine) →
  **Rust** (ownership, safety, low-latency — your fintech edge) → **SQL** (thinking in sets) → one **functional**
  language (Haskell/OCaml) for the ideas. *Gate per language:* a small but real library or tool, with tests.
- **Algorithms:** CLRS as theory + deliberate pattern practice (arrays→graphs→DP→greedy). Tie every pattern to *why*,
  not memorised templates. *Gate:* a solved-problems folder with written reasoning, not just green checkmarks.
- **Craft:** testing, debugging, profiling, reading others' code, clean design. *Gate:* contribute a PR to an open-source project.

*Tools:* the languages above, pytest/cargo-test, profilers, Git. *Spine:* CLRS, "The Rust Book", Fluent Python, a Haskell intro.

## 5. Systems & Infrastructure — the job-ready track (and where DataPulse lives)
*Start: some Linux. Goal: run reliable systems and reason about performance — the SRE/platform spine.*

- **Linux fluency** — shell, processes, files/permissions, systemd, the `/proc` world, the debugging tools
  (`strace`, `perf`, `ss`, bpftrace). *Gate:* the DataPulse field-notes (symptom→tool→evidence→conclusion).
- **Containers & orchestration** — Docker (images, networking, volumes), then Kubernetes (pods→deployments→services,
  probes, HPA, HA). *Gate:* DataPulse on a local `kind` cluster; kill the DB pod and measure recovery.
- **Cloud & networking** — AWS core (compute/storage/VPC/IAM), DNS, load balancing, TLS; networking deep (TCP, congestion,
  observability). *Gate:* an IaC (Terraform) deploy + a networking investigation write-up.
- **SRE** — SLOs/error budgets, observability (Prometheus/Grafana/OpenTelemetry), load testing, chaos engineering.
  *Gate:* the DataPulse SLO doc, perf report, and blameless postmortems.

*This track is almost entirely the **DataPulse** project (`projects/datapulse/`, see ROADMAP.md).* It's the most
directly employable and the fastest path to a senior fintech/SRE role. *Tools:* Docker, kind/kubectl, Terraform,
Prometheus/Grafana, k6, the Linux toolchain.

## 6. AI & Machine Learning — built from scratch, not imported
*Start: needs the maths track (linear algebra, probability, calculus, optimization) in parallel.*

- **F · Classical ML** — regression, classification, trees/forests, SVMs, clustering, the bias/variance story,
  evaluation done honestly. *Gate:* implement linear/logistic regression & a decision tree from scratch (NumPy only).
- **U · Deep learning from first principles** — backprop by hand, MLPs, CNNs, RNNs, then **transformers**. Follow
  Karpathy: micrograd → makemore → **build GPT**. *Gate:* a working autograd engine and a small GPT you trained.
- **G · Modern** — LLMs (tokenisation→attention→training→fine-tuning/RAG), reinforcement learning, diffusion. *Gate:*
  reproduce a paper's core result; fine-tune/serve a model.
- **Applied/MLOps** — serving, evaluation, drift, cost — ties straight into the Systems track. *Gate:* a deployed, monitored model.
- **R** — read and reproduce current papers in a chosen area (e.g. efficient inference, RL, time-series — ties to quant).

*Tools:* Python, NumPy, PyTorch; local models (`ai-local/`); papers (arXiv). *Spine:* Andrew Ng → ISLR/ESL →
Karpathy "Zero to Hero" → d2l.ai → papers.

## 7. Finance & Economics — the application domain (and the quant edge)
*Start: active trader already (VoidCodex / MT5). Goal: turn intuition into rigorous, quantitative finance.*

- **F · Economics** — micro (incentives, markets, equilibrium) & macro (growth, money, policy); accounting basics.
  *Gate:* an essay modelling a real market with supply/demand, honestly caveated.
- **U · Finance core** — time value of money, portfolio theory & CAPM, fixed income, **derivatives** (Hull). *Gate:* a
  portfolio optimiser; price an option three ways (binomial, Black–Scholes, Monte Carlo).
- **G · Quant** — stochastic calculus (shared with maths G), risk (VaR/ES), the pricing & hedging framework,
  time-series econometrics. *Gate:* a derivatives pricing library; a risk report on a real book.
- **Applied · Microstructure & systematic trading** — order books, execution, latency, backtesting *without* lying to
  yourself (look-ahead, survivorship, coordinated omission). Ties to the Systems/low-latency track. *Gate:* a
  backtest with honest statistics and a written critique of its own flaws.

*Tools:* Python (pandas/NumPy), your MT5 data, LaTeX. *Spine:* Mankiw (econ), Hull (derivatives), Shreve (stochastic
calc), Lopez de Prado (realistic quant).

---

## The overlaps — why the spine makes the breadth cheap

These are not seven islands. Deliberately climb where rungs serve several tracks at once:

- **Linear algebra** → ML, physics (QM), CS (graphics/compression), data.
- **Probability & statistics** → ML, quant, physics (stat mech), experiment design.
- **Stochastic calculus** → quant pricing *and* diffusion models.
- **Optimization** → ML training, portfolio theory, operations research.
- **Rust / systems / networking** → SRE, low-latency trading, ML serving.
- **Writing clearly** → every track; it *is* the deliverable.

When you don't know what to climb next, climb the rung that cashes out in the most tracks.
