# DataPulse — Roadmap

A real-time market-data ingestion API, built as a vehicle for learning performance engineering, Linux debugging, observability, SRE, and low-latency systems.

The app is the excuse. **The written artifacts are the deliverable**: benchmarks, field notes, postmortems, ADRs. Anyone can deploy Prometheus. What makes someone senior is that they can tell you *why* the p99 doubled and prove it.

---

## Ground rules

1. **Every phase ends with a written artifact.** If it isn't written down with numbers, it didn't happen.
2. **Build it naive first, then measure, then fix.** Each optimisation should come with a before/after number. Don't pre-optimise; you'd lose the lesson.
3. **Let problems pull tools in.** Don't add Redis/Kafka/NATS because a diagram has them. Add one when you hit a wall, and write an ADR explaining which wall.
4. **ADRs for every real decision** (`docs/adr/NNNN-title.md`: context → options → decision → consequences). This is how you practise having opinions and defending them.
5. **Linux-first.** Develop inside WSL2 (`~/datapulse`), not on the Windows filesystem and not in OneDrive. strace/perf/eBPF only exist on Linux, and OneDrive syncing a `.venv` and `.git` will hurt you.

---

## Architecture (v1, deliberately simple)

```
 Coinbase/Binance WS ─┐
                      ├─► ingestor ──(batched writes)──► PostgreSQL ◄── api (FastAPI) ◄── clients (REST + WS)
 synthetic feed ──────┘   (asyncio queue)                                   │
                                                                            └─► /metrics, traces, logs
```

- **ingestor** and **api** are separate processes from day one. They scale differently and fail differently.
- **Data source:** public crypto trade streams (no API key, and markets run 24/7, so there's always load).
- **Synthetic feed generator:** required. You can't load-test or chaos-test against a real exchange, and replaying recorded data at 10×/100× speed is how you find limits deterministically.

Known problems this design will hit on purpose. Don't solve them early.
- Row-per-tick `INSERT`s will collapse at high rates → batching, `COPY`, partitioning
- WebSocket fan-out across multiple api replicas → needs pub/sub (ADR time)
- Two ingestor replicas = duplicate ticks → leader election or idempotent writes
- Feed disconnects → gap detection, reconnect with backoff, backfill

---

## Phases

Rough pace: 10–15 hrs/week, about 4 months. Phase 6 (Linux) runs alongside 4 and 5.

### Phase 0: Foundation
uv, ruff, mypy (strict), pytest, pre-commit, Docker Compose (api + ingestor + postgres), GitHub Actions CI, Makefile.
**Exit:** `make up` brings the stack up from a clean clone. CI is green. ADR-0001 records the stack choice.

### Phase 1: The app
- Ingestor: WS client → bounded `asyncio.Queue` → batch writer. Reconnects with exponential backoff and jitter.
- API: latest price, OHLCV candles (1m/5m/1h), historical range query, WebSocket stream to clients.
- Store the **exchange timestamp and the receive timestamp** on every tick. Ingest lag is your most important number.

**Exit:** you can explain on a whiteboard what happens when Postgres is slower than the feed (backpressure: drop, block, or buffer? Each one has a cost). ADR on it.

### Phase 2: Observability
- OpenTelemetry traces (FastAPI + asyncpg auto-instrumentation, plus manual spans in the ingestor)
- Prometheus: RED metrics for the api; queue depth, batch size, ingest lag histogram for the ingestor
- Structured JSON logs → Loki, with `trace_id` in every line
- Grafana: one dashboard per service plus one "is the product working" dashboard

**Exit:** starting from one slow request, you can go trace → its logs → the metric that would have warned you, in under 60 seconds.

### Phase 3: SLOs
- SLIs: API availability, API p99 latency, **data freshness** (time since last tick per symbol; this is the one that matters for market data)
- SLO targets, error budgets, multi-window multi-burn-rate alerts (Google SRE Workbook ch. 5)
- First runbooks: one per alert

**Exit:** `docs/slo.md`, plus alerts you've watched fire for the right reasons.

### Phase 4: Load testing and Python performance
- k6 (or Locust) scenarios: read-heavy, WS fan-out heavy, ingest burst (synthetic feed at 100×)
- Find the knee of the latency/throughput curve
- Profile under load: `py-spy record` (flamegraphs), `py-spy dump` on a stuck process, cProfile for offline
- Typical wins to *measure* rather than assume: orjson, uvloop, pool sizing, batch size, avoiding per-request allocation, moving CPU work off the event loop
- Learn **coordinated omission** and why most load-test numbers are lies

**Exit:** `docs/perf/` benchmark report with before/after flamegraphs and numbers, and a capacity plan ("1 replica handles X rps at p99 < Y ms, so N replicas for Z").

### Phase 5: PostgreSQL
- `pg_stat_statements` to find what actually costs time
- `EXPLAIN (ANALYZE, BUFFERS)` on every hot query
- B-tree vs BRIN on time columns; composite index `(symbol, ts)`; covering indexes
- Declarative partitioning by time, and partition pruning. TimescaleDB as an ADR candidate.
- `INSERT` vs multi-row `INSERT` vs `COPY` benchmark
- PgBouncer: transaction pooling and its gotchas with prepared statements

**Exit:** report with query plans before/after and write throughput numbers.

### Phase 6: Linux debugging (alongside 4 and 5)
Tools: `ss -tni`, `strace -c` / `strace -f -T`, `perf top` / `perf record`, bpftrace and bcc (`runqlat`, `offcputime`, `biolatency`, `tcplife`, `tcpretrans`), `/proc/<pid>/`.

**Exit:** `docs/field-notes/` with at least 5 investigations, each written as *symptom → hypothesis → tool → evidence → conclusion*. This is the most interview-valuable thing in the repo.

### Phase 7: Kubernetes, HA, and DR
- kind multi-node cluster, Helm or Kustomize, ArgoCD (GitOps)
- Probes: liveness vs readiness vs startup, and why a liveness probe that checks the DB is a classic outage cause
- PodDisruptionBudgets, anti-affinity, HPA on a custom metric (queue depth or rps)
- Postgres HA with CloudNativePG: streaming replicas, automatic failover, backups to MinIO (S3), point-in-time recovery
- Ingestor singleton: Lease-based leader election *or* idempotent writes (ADR)

**Exit:** kill the primary DB pod under load and measure real RTO/RPO. Do a full restore from backup into a fresh cluster. A backup you've never restored is not a backup.

### Phase 8: Security and compliance
- CI gates: Semgrep and Bandit (SAST), pip-audit, Trivy (image + IaC), Syft SBOM, cosign image signing
- K8s: least-privilege RBAC, default-deny NetworkPolicies, Pod Security Standard `restricted`, non-root distroless images, read-only root fs
- Secrets: SOPS or External Secrets, never in git
- A lightweight STRIDE threat model

**Exit:** `docs/security/threat-model.md`, and CI fails on a planted vulnerable dependency.

### Phase 9: Chaos engineering
Chaos Mesh game days. Each one: hypothesis → inject → observe → postmortem.
- Network latency/loss between api and DB
- Network partition between ingestor and DB
- Exchange feed disconnect and reconnect storm
- Pod kills during deploys
- Disk filling on Postgres
- Clock skew (watch what it does to your ingest-lag metric)
- DNS failure
- CPU throttling from too-tight limits (a very common real-world p99 killer)

**Exit:** at least 5 blameless postmortems in `docs/postmortems/`, with runbooks updated from what you learned.

### Phase 10: Low-latency track (the fintech differentiator)
Python + FastAPI + Postgres + K8s is a fine SRE stack and the **wrong** stack for low latency. Be honest about that, then do something about it:
- Rewrite the ingest hot path (WS decode → normalise → publish) in **Rust** (tokio) or C++
- Measure with HdrHistogram: p50/p99/p99.9/max, not averages
- Lock-free SPSC ring buffer between decode and publish; cache-line padding; avoid allocation on the hot path
- Host tuning: CPU pinning, `isolcpus`, IRQ affinity, busy polling, `SO_BUSY_POLL`, THP off, the performance governor
- Why K8s, GC, the GIL, and the cloud add jitter. Learn what kernel bypass (DPDK, Onload, AF_XDP) is and when firms use it.

**Exit:** `docs/perf/python-vs-rust.md` comparing tail latency distributions, with an explanation of *every* difference.

---

## Repo layout

```
datapulse/
├── services/
│   ├── api/            # FastAPI
│   ├── ingestor/       # feed client + batch writer
│   └── feedgen/        # synthetic/replay feed
├── deploy/
│   ├── compose/
│   ├── k8s/            # base + overlays, or helm charts
│   └── terraform/
├── loadtest/           # k6 scripts
├── chaos/              # Chaos Mesh experiments
├── docs/
│   ├── adr/
│   ├── perf/
│   ├── field-notes/
│   ├── postmortems/
│   ├── runbooks/
│   └── slo.md
└── .github/workflows/
```

---

## Local environment (this machine)

| Tool | Status |
|---|---|
| WSL2 Ubuntu | installed, use it as the primary dev env |
| Docker Desktop | installed, not running; enable WSL integration |
| Python | 3.11 on Windows; use 3.12+ via `uv` inside WSL |
| kind / kubectl / terraform | installed on Windows; install inside WSL too |

eBPF in WSL2 mostly works, but kernel headers can be a fight. If it blocks you, a ~€5/month Linux VM is a reasonable spend for Phases 6 and 10, since you want real hardware counters for `perf` anyway.
