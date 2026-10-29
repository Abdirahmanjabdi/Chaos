# System Design

The second block of the day. Goal: take any "design X" prompt — a classic product system *or* the infrastructure
questions DevOps/platform loops ask — and run a calm, structured 45 minutes that ends in a design that works, with the
trade-offs said out loud.

**How every design session works.**
1. **45-minute timer**, a blank [Excalidraw](https://excalidraw.com) board, talking out loud as if to an interviewer.
2. Follow the framework: **requirements** (functional, then non-functional *with numbers*) → **estimates** → **API
   and data model** → **high-level design** → **deep dives** (bottlenecks, failure modes, trade-offs).
3. *Then* read the reference answer and mark yourself on the five-point rubric below.
4. Commit the diagram (an `.excalidraw` or exported `.png`) plus a one-page write-up to
   `tracks/design/designs/<session>.md`: the design, the trade-offs, and what the reference had that you missed.

**The rubric — one point each.** Score `x/5` at `today done`; that's your design KPI.
1. **Scope:** asked the right questions; functional *and* non-functional requirements with numbers.
2. **Estimates:** QPS, storage and bandwidth, roughly right, and actually used to make a decision.
3. **Interface:** a clean API and data model.
4. **Works end to end:** a request can be traced through every box on the diagram.
5. **Depth:** at least one deep dive with a real trade-off and a named failure mode.

Concept sessions (no single design) are scored on whether you can explain each idea out loud from memory:
`ideas explained / ideas in the session`.

## SD01 · Foundations & the Framework
<!-- rung: S | prereq: none | feeds: every design round -->
**Goal:** Have a repeatable 45-minute structure and the core vocabulary — latency, throughput, availability, consistency — at your fingertips.
**Resources:**
- [The System Design Primer](https://github.com/donnemartin/system-design-primer) — free, the classic overview
- [Hello Interview — System Design in a Hurry](https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction) — free; the delivery framework
- Alex Xu — *System Design Interview, Vol. 1 & 2* (paid, optional; the best worked examples)
**Sessions:**
- [ ] SD01.S01 — Baseline: design a URL shortener cold, in 45 minutes, recorded. Score it on the rubric. Don't read anything first — this is where you start from.
- [ ] SD01.S02 — The framework: read the Hello Interview delivery framework; write your own one-page checklist of questions to ask in the first five minutes.
- [ ] SD01.S03 — Numbers and estimates: latency numbers every engineer should know; five back-of-envelope drills (QPS from daily users, storage for five years, bandwidth).
- [ ] SD01.S04 — Scaling basics: vertical vs horizontal, stateless services, L4 vs L7 load balancing — tie each to the ALB and NGINX Ingress you've actually run.
- [ ] SD01.S05 — CAP and PACELC, consistency models (strong, eventual, read-your-writes), and availability maths: what 99.9% vs 99.99% allows per month.
**Gate artifact:** your framework checklist + the baseline design, kept so you can compare against it later.

## SD02 · Building Blocks
<!-- rung: S | prereq: SD01 | feeds: every design -->
**Goal:** Know each standard component — what it's for, how it fails, what it costs — well enough to defend picking it.
**Resources:**
- [The System Design Primer](https://github.com/donnemartin/system-design-primer)
- [Hello Interview — core concepts](https://www.hellointerview.com/learn/system-design/in-a-hurry/core-concepts)
- Kleppmann — *Designing Data-Intensive Applications* (paid; the deep reference, chapters 5–9 especially)
**Sessions:**
- [ ] SD02.S01 — Caching: cache-aside, write-through, write-back; eviction; invalidation; stampedes. Redis as you used it on ElastiCache.
- [ ] SD02.S02 — Databases: SQL vs NoSQL, indexes (B-tree vs LSM), replication (leader–follower, multi-leader, leaderless), read replicas on RDS.
- [ ] SD02.S03 — Partitioning and sharding: range vs hash, hot keys, re-sharding; consistent hashing (you built one in LC18.S08).
- [ ] SD02.S04 — Queues and streams: SQS/SNS, Amazon MQ, Kafka; at-least-once delivery, idempotency, ordering, dead-letter queues, back-pressure.
- [ ] SD02.S05 — Blob storage and CDNs: S3 design, pre-signed URLs, CloudFront, cache headers.
- [ ] SD02.S06 — API design: REST vs gRPC vs WebSockets; pagination; idempotency keys; authentication (OAuth 2, JWT) at the edge.
- [ ] SD02.S07 — IDs, time and coordination: Snowflake IDs, clock skew, distributed locks, leader election (and why you'd reach for etcd or ZooKeeper).
- [ ] SD02.S08 — Search: inverted indexes, Elasticsearch/OpenSearch basics, when a DB `LIKE` stops being enough.
**Gate artifact:** a one-page "component card" for each of the eight — what it's for, how it fails, what it costs.

## SD03 · Classic Designs I
<!-- rung: U | prereq: SD02 | feeds: the most-asked prompts -->
**Goal:** Deliver the five most common prompts end to end, inside 45 minutes, scoring 4/5 or better.
**Resources:**
- [Hello Interview — problem breakdowns](https://www.hellointerview.com/learn/system-design/in-a-hurry/problem-breakdowns) — free worked answers
- [The System Design Primer — solutions](https://github.com/donnemartin/system-design-primer#system-design-interview-questions-with-solutions)
**Sessions:**
- [ ] SD03.S01 — URL shortener, again. Compare it with your SD01 baseline — that's your first visible progress.
- [ ] SD03.S02 — A distributed rate limiter (token bucket in Redis; where it lives — gateway or sidecar; behaviour when Redis is down).
- [ ] SD03.S03 — A key-value store (Dynamo-style: partitioning, replication, quorums, hinted handoff).
- [ ] SD03.S04 — A unique ID generator · a web crawler (politeness, dedupe, frontier queue).
- [ ] SD03.S05 — A notification system (push, SMS and email; fan-out; retries; user preferences; rate limits).
**Gate artifact:** five designs in `designs/`, each scored, at least three at 4/5 or better.

## SD04 · Classic Designs II
<!-- rung: U | prereq: SD03 | feeds: product-company loops -->
**Goal:** Handle the heavier prompts: fan-out, real-time, large files, contention and money.
**Resources:**
- [Hello Interview — problem breakdowns](https://www.hellointerview.com/learn/system-design/in-a-hurry/problem-breakdowns)
- [ByteByteGo blog](https://blog.bytebytego.com) — free articles and diagrams
**Sessions:**
- [ ] SD04.S01 — News feed / timeline: fan-out on write vs on read, the celebrity problem.
- [ ] SD04.S02 — Chat (WhatsApp-style): WebSockets, presence, message ordering, offline delivery.
- [ ] SD04.S03 — Search autocomplete: a trie or a top-k index, updates, caching at the edge.
- [ ] SD04.S04 — Video streaming (YouTube-style): upload pipeline, transcoding, adaptive bitrate, CDN.
- [ ] SD04.S05 — File sync (Dropbox-style): chunking, dedupe, metadata service, conflict handling.
- [ ] SD04.S06 — Ticket booking (Ticketmaster-style): seat contention, holds with TTLs, locking vs optimistic concurrency.
- [ ] SD04.S07 — A payment system and ledger: idempotency, double-entry, exactly-once *effects*, reconciliation — the fintech classic.
**Gate artifact:** seven designs in `designs/`, scored.

## SD05 · Infrastructure & Platform Design
<!-- rung: U | prereq: SD02 | feeds: DevOps / platform / SRE loops — your edge, straight off your CV -->
**Goal:** Answer the infra-flavoured prompts DevOps and platform interviews actually ask, drawing on what you've built.
**Resources:**
- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — free
- [AWS Architecture Center](https://aws.amazon.com/architecture/) — free reference architectures
- [Kubernetes documentation](https://kubernetes.io/docs/home/)
**Sessions:**
- [ ] SD05.S01 — A CI/CD platform for 200 microservices: runners, caching, artifacts, environment promotion, GitOps with ArgoCD, rollback.
- [ ] SD05.S02 — A multi-account AWS landing zone: accounts and OUs, SCPs, networking (Transit Gateway), IAM Identity Center, and the Terraform state layout.
- [ ] SD05.S03 — Multi-AZ to multi-region: active–passive vs active–active, RTO/RPO, Route53 failover, data replication choices.
- [ ] SD05.S04 — An observability platform at scale: metrics (Prometheus plus Thanos or Mimir), logs (Loki), traces (OpenTelemetry), cardinality and cost.
- [ ] SD05.S05 — Secrets management for a whole company: Vault, dynamic credentials, rotation, IRSA / Pod Identity, break-glass access.
- [ ] SD05.S06 — A multi-tenant Kubernetes platform: namespaces, quotas, NetworkPolicies, HPA plus Karpenter, upgrades without downtime.
- [ ] SD05.S07 — Deployment strategies: rolling, blue/green, canary with Argo Rollouts, feature flags, automated rollback on SLO breach.
- [ ] SD05.S08 — A log-ingestion pipeline: agents → Kinesis or Kafka → S3 → Athena; back-pressure and retention.
**Gate artifact:** eight infra designs in `designs/` — your strongest interview material, since each one connects to something on your CV.

## SD06 · Reliability & SRE Design
<!-- rung: U | prereq: SD05 | feeds: SRE loops, "tell me about an incident" -->
**Goal:** Design for failure, and talk through incidents like someone who has been on call.
**Resources:**
- [Google SRE books](https://sre.google/books/) — *SRE* and *The Site Reliability Workbook*, free online
- [AWS Builders' Library](https://builder.aws.com/learn/topics/builders-library) — free; timeouts, retries, backoff, load shedding
**Sessions:**
- [ ] SD06.S01 — SLIs, SLOs and error budgets; multi-window burn-rate alerting (SRE Workbook, "Alerting on SLOs").
- [ ] SD06.S02 — Resilience patterns: timeouts, retries with jitter, circuit breakers, bulkheads, load shedding, the thundering herd.
- [ ] SD06.S03 — A mock incident, out loud: "p99 latency tripled ten minutes ago" — triage, mitigate, find the root cause, communicate.
- [ ] SD06.S04 — Capacity planning and load testing: from a traffic forecast to node counts, with headroom and cost.
- [ ] SD06.S05 — Disaster recovery and a game-day plan; cost-aware design (the FinOps thinking from your internship ADRs).
**Gate artifact:** an SLO doc for an imaginary service + a written mock-incident timeline and postmortem.

## SD07 · Low-Latency & Market Data
<!-- rung: G | prereq: SD04 | feeds: fintech and trading-firm loops — the direction you're heading -->
**Goal:** Design the systems trading firms ask about, where microseconds and ordering matter.
**Resources:**
- [Mechanical Sympathy blog](https://mechanical-sympathy.blogspot.com) — free; the LMAX mindset
- [LMAX Disruptor — technical paper](https://lmax-exchange.github.io/disruptor/disruptor.html) — free
**Sessions:**
- [ ] SD07.S01 — A market-data fan-out service: feed handlers, snapshot plus deltas, pub/sub, slow consumers.
- [ ] SD07.S02 — An order-matching engine: an in-memory order book, a single-threaded sequencer, journaling and replay.
- [ ] SD07.S03 — A real-time risk engine — connect it to Sentinel Trading and say what you'd change at 100× the scale.
**Gate artifact:** three designs in `designs/` — talking points for every fintech interview.

## SD08 · Mocks & Articulation
<!-- rung: G | prereq: SD03 (start mocks early) | feeds: offers -->
**Goal:** Perform under pressure: draw fast, keep time, and lead the conversation.
**Resources:**
- [Excalidraw](https://excalidraw.com) — free whiteboard
- [Pramp](https://www.pramp.com) — free peer mocks, system design included
- [interviewing.io — system design mocks](https://interviewing.io) — anonymous mocks; free recordings to learn from
**Sessions:**
- [ ] SD08.S01 — Speed drawing: sketch five standard diagrams (3-tier, queue-based, CQRS, multi-region, GitOps) in 3 minutes each.
- [ ] SD08.S02 — Mock 1 (a classic prompt) with a peer, or an AI acting as interviewer; record it, score it.
- [ ] SD08.S03 — Mock 2 (an infra prompt from SD05).
- [ ] SD08.S04 — Portfolio: polish your three best designs into one-page write-ups worth linking from your CV.
- [ ] SD08.S05 — Mock 3 and Mock 4 in the same week — both 4/5 or better.
**Gate artifact:** four scored mocks + three polished write-ups.
