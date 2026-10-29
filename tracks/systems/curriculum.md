# Systems & Infrastructure

Linux · networking · Docker · Kubernetes · AWS · observability · SRE · low latency. The most job-ready track — and
most of it *is* the DataPulse flagship (`projects/datapulse`, plan in `ROADMAP.md`): modules S04–S15 are its phases.

**How to use this file.** Strictly top to bottom; `today` shows the first unticked session. A session is one deep block;
lab-style sessions may take two — tick only when done. DataPulse code lives in WSL2 (`~/datapulse`), Linux-first,
because `strace`/`perf`/eBPF need Linux. **Levels:** F · S · U · G · R (see `CURRICULUM.md`).

## S01 · Linux Foundations
<!-- rung: F | prereq: none | feeds: everything in this track -->
**Goal:** Feel at home in a Linux shell — files, permissions, processes, pipes and scripts — without reaching for a GUI.
**Resources:**
- [The Linux Command Line (William Shotts)](https://linuxcommand.org/tlcl.php) — free book
- [OverTheWire Bandit](https://overthewire.org/wargames/bandit/) — a game that teaches the shell
- [Linux Journey](https://labex.io/linuxjourney) — short free lessons
**Sessions:**
- [ ] S01.S01 — Placement & setup: confirm WSL2 Ubuntu works; play [Bandit](https://overthewire.org/wargames/bandit/) levels 0–5; note what was new.
- [ ] S01.S02 — The shell: navigation, files and directories, permissions (TLCL part 1).
- [ ] S01.S03 — Redirection, pipes, expansion and quoting.
- [ ] S01.S04 — Processes and job control; signals (`ps`, `top`, `kill`, `bg`/`fg`).
- [ ] S01.S05 — Text processing: grep, sed, awk, cut, sort, uniq.
- [ ] S01.S06 — Bandit levels 6–15.
- [ ] S01.S07 — Shell scripting: variables, conditionals, loops, functions (TLCL part 4).
- [ ] S01.S08 — Bandit levels 16–25.
- [ ] S01.S09 — Build: a bash script that automates something you do every week (a backup, a report, a cleanup).
**Gate artifact:** Bandit to level 25 + a documented automation script in this repo.
**Anki seeds:** permission bits · redirection operators · signal numbers (HUP, INT, KILL, TERM) · grep/sed/awk idioms

## S02 · Linux Internals & Administration
<!-- rung: U | prereq: S01 | feeds: S10 debugging, SRE -->
**Goal:** Know what the system is doing underneath — boot, services, users, filesystems, `/proc` — and set a machine up from scratch.
**Resources:**
- [Linux Journey](https://labex.io/linuxjourney)
- [Julia Evans' zines](https://wizardzines.com) — the clearest explanations of Linux internals
- `man` pages (`man 7 signal`, `man 5 proc`)
**Sessions:**
- [ ] S02.S01 — The boot process; systemd units and the journal (`systemctl`, `journalctl`).
- [ ] S02.S02 — Users, groups, sudo, file capabilities.
- [ ] S02.S03 — Filesystems, mounts, inodes; finding what's using the disk.
- [ ] S02.S04 — Package management; building software from source.
- [ ] S02.S05 — `/proc` and `/sys`: read a running process's life from the inside (fds, maps, status).
- [ ] S02.S06 — Networking tools: ip, ss, dig, curl, tcpdump.
- [ ] S02.S07 — Build: set up a fresh Ubuntu machine from a written runbook (users, SSH hardening, firewall, updates) — then do it again from the runbook alone.
**Gate artifact:** a server-setup runbook you've executed twice, end to end.

## S03 · Networking for Engineers
<!-- rung: U | prereq: S02 | feeds: everything distributed, low latency -->
**Goal:** Understand the path a request takes — IP, TCP, DNS, HTTP, TLS, load balancers — and where latency hides.
**Resources:**
- [Computer Networks: A Systems Approach](https://book.systemsapproach.org) — free book
- [High Performance Browser Networking (Ilya Grigorik)](https://hpbn.co) — free book
- [Wireshark](https://www.wireshark.org)
**Sessions:**
- [ ] S03.S01 — IP addressing, subnetting and CIDR — work 20 subnetting exercises.
- [ ] S03.S02 — TCP vs UDP; the TCP handshake and teardown — capture one with tcpdump/Wireshark.
- [ ] S03.S03 — DNS from the root down: trace a lookup with `dig +trace`.
- [ ] S03.S04 — HTTP/1.1, HTTP/2, HTTP/3 and the TLS handshake — capture and annotate one.
- [ ] S03.S05 — Routing, NAT, load balancing (L4 vs L7), proxies.
- [ ] S03.S06 — Latency: propagation, queuing, serialisation — measure each on a real request.
**Gate artifact:** an annotated packet capture of a complete HTTPS request + a latency budget for it.

## S04 · Containers & Docker — DataPulse Phase 0
<!-- rung: U | prereq: S02 | feeds: S05 onwards (all of DataPulse) -->
**Goal:** Understand what a container really is, and lay the DataPulse foundation: `make up` from a clean clone, CI green.
**Resources:**
- [Docker — Get started](https://docs.docker.com/get-started/)
- "Containers From Scratch" — Liz Rice's talk (search YouTube)
- `ROADMAP.md` — Phase 0
**Sessions:**
- [ ] S04.S01 — What a container is: namespaces and cgroups. Watch "Containers From Scratch", then make a toy container with `unshare`.
- [ ] S04.S02 — Images and layers; writing a good Dockerfile (multi-stage, non-root, small).
- [ ] S04.S03 — Container networking and volumes.
- [ ] S04.S04 — Docker Compose: multi-service apps, healthchecks, startup order.
- [ ] S04.S05 — DataPulse Phase 0: scaffold `~/datapulse` in WSL2 — uv, ruff, mypy --strict, pytest, pre-commit.
- [ ] S04.S06 — DataPulse Phase 0: Compose stack (api + ingestor + postgres) and a Makefile — `make up` works from a clean clone.
- [ ] S04.S07 — DataPulse Phase 0: GitHub Actions CI green; write ADR-0001 (the stack choice).
**Gate artifact:** DataPulse Phase 0 exit — `make up` from a clean clone, CI green, ADR-0001 written.

## S05 · The App: Ingest & Serve — DataPulse Phase 1
<!-- rung: U | prereq: S04, programming G01 | feeds: S06–S15 -->
**Goal:** A real market-data pipeline — WebSocket ingest, batched writes, an API — and a defended answer to backpressure.
**Resources:**
- `ROADMAP.md` — Phase 1
- [FastAPI docs](https://fastapi.tiangolo.com)
- [asyncio docs](https://docs.python.org/3/library/asyncio.html)
**Sessions:**
- [ ] S05.S01 — Ingestor: a WebSocket client to a public exchange feed; parse trades.
- [ ] S05.S02 — Bounded `asyncio.Queue` → batch writer into Postgres.
- [ ] S05.S03 — Reconnect with exponential backoff and jitter; gap detection.
- [ ] S05.S04 — Store the exchange timestamp *and* the receive timestamp; compute ingest lag.
- [ ] S05.S05 — API: latest price and OHLCV candles (1m / 5m / 1h).
- [ ] S05.S06 — API: historical range queries and a WebSocket stream to clients.
- [ ] S05.S07 — A synthetic feed generator that replays at 10× / 100×.
- [ ] S05.S08 — ADR: backpressure — drop, block or buffer? Decide and defend it.
**Gate artifact:** Phase 1 exit — explain on a whiteboard what happens when Postgres is slower than the feed + the backpressure ADR.

## S06 · Observability — DataPulse Phase 2
<!-- rung: U | prereq: S05 | feeds: S07, S08, every incident you'll ever debug -->
**Goal:** See inside the system: metrics, traces and logs, linked — so a slow request can be explained in under a minute.
**Resources:**
- [OpenTelemetry docs](https://opentelemetry.io/docs/)
- [Prometheus docs](https://prometheus.io/docs/)
- [Google SRE books](https://sre.google/books/) — free; "Monitoring Distributed Systems"
**Sessions:**
- [ ] S06.S01 — Metrics: the Prometheus client and RED metrics for the API.
- [ ] S06.S02 — Ingestor metrics: queue depth, batch size, an ingest-lag histogram.
- [ ] S06.S03 — Tracing: OpenTelemetry auto-instrumentation plus manual spans in the ingestor.
- [ ] S06.S04 — Structured JSON logs into Loki, with `trace_id` on every line.
- [ ] S06.S05 — Grafana: one dashboard per service and one "is the product working?" dashboard.
- [ ] S06.S06 — The drill: from one slow request → its trace → its logs → the metric that warned you, in under 60 seconds.
**Gate artifact:** Phase 2 exit — the 60-second drill, written up step by step.

## S07 · SLOs & Incident Practice — DataPulse Phase 3
<!-- rung: U | prereq: S06 | feeds: on-call, every reliability conversation -->
**Goal:** Define "working" in numbers, alert only on what users would feel, and have a runbook for every alert.
**Resources:**
- [Google SRE Book & Workbook](https://sre.google/books/) — free; the Workbook's SLO and alerting chapters
**Sessions:**
- [ ] S07.S01 — SLIs: availability, p99 latency and data freshness (the one that matters for market data).
- [ ] S07.S02 — SLO targets and error budgets; write `docs/slo.md`.
- [ ] S07.S03 — Multi-window, multi-burn-rate alerts.
- [ ] S07.S04 — Runbooks: one per alert.
- [ ] S07.S05 — Inject a fault, watch an alert fire for the right reason, write a mini-postmortem.
**Gate artifact:** Phase 3 exit — `docs/slo.md`, alerts you've watched fire correctly, and their runbooks.

## S08 · Load Testing & Performance — DataPulse Phase 4
<!-- rung: U | prereq: S07 | feeds: capacity planning, S15 -->
**Goal:** Find the system's limits honestly and explain them — without falling for coordinated omission.
**Resources:**
- [k6 docs](https://grafana.com/docs/k6/latest/)
- [Brendan Gregg's site](https://www.brendangregg.com) — flame graphs and methodology
- "How NOT to Measure Latency" — Gil Tene (search YouTube)
**Sessions:**
- [ ] S08.S01 — Coordinated omission: watch Gil Tene's talk; write why most load-test numbers lie.
- [ ] S08.S02 — k6 scenarios: read-heavy, WebSocket fan-out, ingest burst (synthetic feed at 100×).
- [ ] S08.S03 — Find the knee of the latency/throughput curve.
- [ ] S08.S04 — Profile under load: `py-spy record` flame graphs; `py-spy dump` on a stuck process.
- [ ] S08.S05 — Measure — don't assume — the usual wins: orjson, uvloop, pool sizing, batch size.
- [ ] S08.S06 — Capacity plan: "one replica handles X rps at p99 < Y ms, so N replicas for Z".
**Gate artifact:** Phase 4 exit — `docs/perf/` report with before/after flame graphs and a capacity plan.

## S09 · PostgreSQL in Production — DataPulse Phase 5
<!-- rung: U | prereq: S08, programming G06 | feeds: every data-heavy system -->
**Goal:** Make the database fast on purpose — measure queries, read plans, index and partition, and benchmark writes.
**Resources:**
- [Use The Index, Luke!](https://use-the-index-luke.com) — free
- [PostgreSQL documentation](https://www.postgresql.org/docs/)
**Sessions:**
- [ ] S09.S01 — `pg_stat_statements`: find what actually costs time.
- [ ] S09.S02 — `EXPLAIN (ANALYZE, BUFFERS)` on every hot query; learn to read the plans.
- [ ] S09.S03 — B-tree vs BRIN on time columns; the composite `(symbol, ts)` index; covering indexes.
- [ ] S09.S04 — Declarative partitioning by time; partition pruning.
- [ ] S09.S05 — Benchmark INSERT vs multi-row INSERT vs COPY.
- [ ] S09.S06 — PgBouncer transaction pooling and its prepared-statement gotchas.
**Gate artifact:** Phase 5 exit — a report with before/after query plans and write-throughput numbers.

## S10 · Linux Debugging & eBPF — DataPulse Phase 6
<!-- rung: G | prereq: S09, S02 | feeds: the most interview-valuable artifacts you'll have -->
**Goal:** Debug live systems from evidence — syscalls, CPU, scheduling, I/O and TCP — and write it up like a detective.
**Resources:**
- [Brendan Gregg's site](https://www.brendangregg.com) — free; *Systems Performance* and *BPF Performance Tools* (paid)
- [bpftrace](https://github.com/bpftrace/bpftrace)
**Sessions:**
- [ ] S10.S01 — `strace -c` and `strace -f -T` against the running services.
- [ ] S10.S02 — `perf top` / `perf record`; CPU flame graphs.
- [ ] S10.S03 — `ss -tni`: read the TCP internals of live connections.
- [ ] S10.S04 — bpftrace and BCC: runqlat, offcputime, biolatency, tcplife, tcpretrans.
- [ ] S10.S05 — Field notes 1 & 2: symptom → hypothesis → tool → evidence → conclusion.
- [ ] S10.S06 — Field notes 3 & 4.
- [ ] S10.S07 — Field note 5.
**Gate artifact:** Phase 6 exit — `docs/field-notes/` with five investigations.

## S11 · Infrastructure as Code & AWS
<!-- rung: U | prereq: S04, S03 | feeds: S12, every cloud job -->
**Goal:** Build cloud infrastructure from code — reproducible, reviewable, and torn down when you're done.
**Resources:**
- [Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials)
- [AWS Skill Builder](https://skillbuilder.aws) — free courses
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
**Sessions:**
- [ ] S11.S01 — Terraform basics: providers, resources, state, plan and apply.
- [ ] S11.S02 — Modules, variables and remote state.
- [ ] S11.S03 — AWS core: IAM and least privilege, regions and AZs — and set up a billing alarm *first*.
- [ ] S11.S04 — AWS networking: VPC, subnets, route tables, security groups, NAT, the ALB.
- [ ] S11.S05 — AWS compute and storage: EC2, ECS/Fargate, S3, EBS, RDS.
- [ ] S11.S06 — Deploy DataPulse to AWS with Terraform (free tier where possible) — then destroy it.
- [ ] S11.S07 — Review it against the Well-Architected pillars, with a cost estimate.
**Gate artifact:** DataPulse deployed to AWS via Terraform, destroyed, and written up with cost and architecture. (Optional credential: AWS Solutions Architect – Associate.)

## S12 · Kubernetes, HA & DR — DataPulse Phase 7
<!-- rung: G | prereq: S11, S09 | feeds: S13, S14 -->
**Goal:** Run DataPulse on Kubernetes with real high availability — and prove recovery by killing things and restoring from backup.
**Resources:**
- [Kubernetes docs](https://kubernetes.io/docs/home/)
- [Kubernetes the Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way)
- [CloudNativePG](https://cloudnative-pg.io)
- `ROADMAP.md` — Phase 7
**Sessions:**
- [ ] S12.S01 — Core objects on `kind`: pods, deployments, services, configmaps, secrets.
- [ ] S12.S02 — Kubernetes the Hard Way, part 1: certificates, kubeconfigs, etcd.
- [ ] S12.S03 — Kubernetes the Hard Way, part 2: control plane, workers, networking, smoke test.
- [ ] S12.S04 — DataPulse on kind with Helm or Kustomize; GitOps with ArgoCD.
- [ ] S12.S05 — Probes (liveness vs readiness vs startup), PodDisruptionBudgets, anti-affinity, HPA on a custom metric.
- [ ] S12.S06 — Postgres HA with CloudNativePG: replicas, automatic failover, backups to MinIO, point-in-time recovery.
- [ ] S12.S07 — The ingestor singleton: Lease-based leader election or idempotent writes — write the ADR.
- [ ] S12.S08 — Kill the primary under load; measure real RTO/RPO; restore from backup into a fresh cluster.
**Gate artifact:** Phase 7 exit — measured RTO/RPO + a successful full restore. (Optional credential: CKA.)

## S13 · Security & Compliance — DataPulse Phase 8
<!-- rung: G | prereq: S12 | feeds: every production system -->
**Goal:** Make security a property of the pipeline — scanning, signing, least privilege, secrets — and model the threats.
**Resources:**
- [OWASP Top 10](https://top10.owasp.org/)
- [Kubernetes security docs](https://kubernetes.io/docs/concepts/security/)
- `ROADMAP.md` — Phase 8
**Sessions:**
- [ ] S13.S01 — CI gates: Semgrep and Bandit (SAST), pip-audit.
- [ ] S13.S02 — Trivy (image + IaC), Syft SBOM, cosign image signing.
- [ ] S13.S03 — Kubernetes: least-privilege RBAC, default-deny NetworkPolicies.
- [ ] S13.S04 — Pod Security Standard "restricted": non-root distroless images, read-only root filesystem.
- [ ] S13.S05 — Secrets with SOPS or External Secrets — never in git.
- [ ] S13.S06 — A lightweight STRIDE threat model.
**Gate artifact:** Phase 8 exit — `docs/security/threat-model.md` + CI that fails on a planted vulnerable dependency.

## S14 · Chaos Engineering — DataPulse Phase 9
<!-- rung: G | prereq: S12, S07 | feeds: postmortem skill, resilience design -->
**Goal:** Break the system on purpose, with a hypothesis, and turn each failure into a blameless postmortem and a better runbook.
**Resources:**
- [Chaos Mesh](https://chaos-mesh.org)
- [Google SRE Book](https://sre.google/books/) — "Postmortem Culture"
**Sessions:**
- [ ] S14.S01 — Game day 1: network latency and packet loss between api and DB.
- [ ] S14.S02 — Game day 2: a partition between ingestor and DB.
- [ ] S14.S03 — Game day 3: exchange-feed disconnect and a reconnect storm.
- [ ] S14.S04 — Game day 4: pod kills during deploys.
- [ ] S14.S05 — Game day 5: pick one — disk filling on Postgres, clock skew, DNS failure, or CPU throttling from tight limits.
**Gate artifact:** Phase 9 exit — five blameless postmortems in `docs/postmortems/` with runbooks updated.

## S15 · Low-Latency Systems — DataPulse Phase 10
<!-- rung: G | prereq: S08, programming G05, cs C13 | feeds: the fintech differentiator, finance E10 -->
**Goal:** Be honest that Python/K8s is the wrong stack for low latency — then build and measure the right one.
**Resources:**
- [Mechanical Sympathy (Martin Thompson)](https://mechanical-sympathy.blogspot.com)
- [LMAX Disruptor](https://lmax-exchange.github.io/disruptor/)
- [HdrHistogram](https://hdrhistogram.github.io/HdrHistogram/)
**Sessions:**
- [ ] S15.S01 — Write the honest analysis: why Python, the GIL, GC, Kubernetes and the cloud add jitter.
- [ ] S15.S02 — Rewrite the ingest hot path in Rust (tokio): decode → normalise → publish.
- [ ] S15.S03 — Measure with HdrHistogram: p50 / p99 / p99.9 / max — never averages.
- [ ] S15.S04 — Lock-free SPSC ring buffer between decode and publish (from cs C13); no allocation on the hot path.
- [ ] S15.S05 — Host tuning: CPU pinning, isolcpus, IRQ affinity, busy polling, THP off, the performance governor.
- [ ] S15.S06 — Kernel bypass: what DPDK, Onload and AF_XDP are, and when trading firms use them.
**Gate artifact:** Phase 10 exit — `docs/perf/python-vs-rust.md` comparing tail-latency distributions and explaining every difference.
