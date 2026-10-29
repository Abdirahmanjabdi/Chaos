# Project: DataPulse

The applied flagship for the **Systems** track (and later the low-latency finance edge): a real-time market-data
ingestion API wrapped in a full SRE stack, built as a vehicle for performance engineering, Linux debugging,
observability, and reliability.

- **The plan:** [`../../ROADMAP.md`](../../ROADMAP.md) — 10 phases, each ending in a written artifact.
- **Status:** Phase 0 (Foundation). `uv` installed; repo scaffold is the next deep-block work.
- **Dev environment:** WSL2 (Linux-first — `strace`/`perf`/eBPF need it); code lives here, not synced via OneDrive's
  `.git`/`.venv`.

This project is where several tracks cash out at once: Systems, Programming (Rust ingest path in Phase 10),
Finance (market data), and later AI/ML (signal/serving).
