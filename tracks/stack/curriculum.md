# The CV Stack

The third block of the day. Your CV names a lot of tools, and an interviewer can point at any line and say "tell me
more". Goal: **defend every line** — explain it from first principles, rebuild it from scratch, and debug it when
it breaks.

**Weakest first.** This track doesn't go top to bottom. `today` serves the module you rated lowest (`today rate`,
1–5), and finishes a module once you've started it. Re-rate every Sunday: what you're worst at is always next.

**How every module works.**
1. **S01 is always the question bank:** write the 10 questions an interviewer is most likely to ask about this tool
   *given your CV*, then answer each out loud, without notes. Save them in `tracks/stack/qbank/<module>.md`.
2. **The middle sessions are labs.** Build it yourself on a free local setup ([kind](https://kind.sigs.k8s.io) for
   Kubernetes, LocalStack or the AWS free tier, `terraform` against a sandbox account), in
   `tracks/stack/labs/<module>/`. **Never commit credentials, state files or kubeconfigs** — `.gitignore` blocks the
   usual ones, but check `git status` anyway.
3. **The last session is "defend the bullet":** say your CV line in STAR form, with its numbers, then re-answer the
   question bank cold.
4. **Score** for `today done`: questions answered cleanly out loud / asked (e.g. `7/10`). For a lab session: lab
   goals hit / goals.

| Rating | Means |
|---|---|
| 1 | I'd struggle to explain what it is |
| 2 | I've used it, but I'd wobble on "why" questions |
| 3 | I can explain it and use it, but I'd fail a deep follow-up |
| 4 | I can explain it, build it from scratch and debug it |
| 5 | I could teach it, and I know the trade-offs and the failure modes |

## CV01 · Linux & Bash
<!-- rung: S | prereq: none | feeds: every troubleshooting question, every on-call story -->
**Goal:** Drive Linux like an admin: processes, services, permissions, disks, and a calm method for "the server is slow".
**Resources:**
- [Brendan Gregg — Linux performance analysis in 60 seconds](https://netflixtechblog.com/linux-performance-analysis-in-60-000-milliseconds-accc10403c55)
- [OverTheWire — Bandit](https://overthewire.org/wargames/bandit/) — free shell practice
- [ShellCheck](https://www.shellcheck.net)
**Sessions:**
- [ ] CV01.S01 — Question bank: 10 likely Linux/Bash questions for your CV; answer each out loud and score.
- [ ] CV01.S02 — Processes and services: `ps`, signals, `kill -9` vs `-15`, systemd units, `journalctl`; write and enable your own unit.
- [ ] CV01.S03 — Permissions and filesystems: users and groups, chmod/chown, setuid, inodes; the "disk full but `df` and `du` disagree" scenario.
- [ ] CV01.S04 — Troubleshooting drill: run the 60-second checklist (`uptime`, `vmstat`, `iostat`, `free`, `ss`, `top`) on a VM under load; explain every column.
- [ ] CV01.S05 — Bash properly: `set -euo pipefail`, `trap`, arrays, `getopts`, functions; a backup script, ShellCheck clean.
- [ ] CV01.S06 — Defend the bullet: "Linux (administration, shell scripting, process management)" — STAR stories plus the question bank, cold.
**Gate artifact:** `qbank/CV01.md` at 8/10 or better + `labs/CV01/` (the unit file, the backup script).

## CV02 · Networking
<!-- rung: S | prereq: none | feeds: VPC, Kubernetes networking, every "why can't it connect?" -->
**Goal:** Explain a packet's whole journey — DNS, TCP, TLS, HTTP, load balancer, VPC — and debug the break.
**Resources:**
- [Julia Evans — networking zines and posts](https://jvns.ca/categories/networking/) — friendly, accurate
- [AWS — VPC user guide](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [High Performance Browser Networking](https://hpbn.co) — free online book (TCP, TLS, HTTP/2)
**Sessions:**
- [ ] CV02.S01 — Question bank: 10 likely networking questions for your CV; answer out loud and score.
- [ ] CV02.S02 — TCP/IP: the 3-way handshake, ports, TCP vs UDP, TIME_WAIT; watch it happen with `tcpdump` and `ss`.
- [ ] CV02.S03 — DNS deep: recursive resolution, record types, TTLs, Route53 routing policies; trace one with `dig +trace`.
- [ ] CV02.S04 — TLS: the handshake, certificates and chains, SNI; ACM; terminating at the ALB vs in the pod — the trade-off.
- [ ] CV02.S05 — HTTP and load balancing: HTTP/1.1 vs 2, keep-alive, L4 vs L7, NGINX Ingress; answer "what happens when you type a URL" in full.
- [ ] CV02.S06 — VPC from memory: CIDR maths, subnets, route tables, IGW vs NAT, security groups vs NACLs, endpoints, peering vs Transit Gateway. Redraw your CV's multi-AZ VPC.
- [ ] CV02.S07 — Defend the bullet: the multi-AZ VPC and micro-segmentation lines, plus a "pod can't reach RDS" troubleshooting walk-through.
**Gate artifact:** `qbank/CV02.md` at 8/10 + your VPC diagram + the troubleshooting walk-through, written up.

## CV03 · Docker & Containers
<!-- rung: S | prereq: CV01 | feeds: Kubernetes, CI/CD, security -->
**Goal:** Know what a container actually *is*, and build small, secure images on purpose.
**Resources:**
- [Docker docs — best practices](https://docs.docker.com/build/building/best-practices/)
- [Liz Rice — Containers from Scratch (talk)](https://www.youtube.com/watch?v=8fi7uSYlOdc)
- [Trivy](https://trivy.dev)
**Sessions:**
- [ ] CV03.S01 — Question bank: 10 likely Docker questions for your CV; answer out loud and score.
- [ ] CV03.S02 — Under the hood: namespaces and cgroups; build a "container" by hand with `unshare` and `chroot` (after the Liz Rice talk).
- [ ] CV03.S03 — Images: layers, the build cache, multi-stage builds. Reproduce your 392 MB → 41 MB result on a demo app and explain every saving.
- [ ] CV03.S04 — Security: non-root users, distroless images, dropped capabilities, read-only filesystems; scan before and after with Trivy.
- [ ] CV03.S05 — Compose, networks and volumes; debugging with `logs`, `exec`, `inspect` and `docker events`.
- [ ] CV03.S06 — Defend the bullet: "non-root multi-stage builds, 89.5% smaller, fewer CVEs" — STAR, the numbers, and why each step works.
**Gate artifact:** `qbank/CV03.md` at 8/10 + `labs/CV03/` (before/after Dockerfiles and Trivy reports).

## CV04 · Kubernetes
<!-- rung: U | prereq: CV03 | feeds: EKS, Helm, ArgoCD, every platform question -->
**Goal:** Explain the control loop, run workloads properly, and debug the five classic failures fast.
**Resources:**
- [Kubernetes documentation](https://kubernetes.io/docs/home/)
- [kind](https://kind.sigs.k8s.io) — free local clusters
- [Kubernetes the Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way) — free; optional, for depth
**Sessions:**
- [ ] CV04.S01 — Question bank: 10 likely Kubernetes questions for your CV; answer out loud and score.
- [ ] CV04.S02 — Architecture: API server, etcd, scheduler, controller manager, kubelet, kube-proxy; the reconcile loop. Stand up a kind cluster.
- [ ] CV04.S03 — Workloads: Pods, Deployments, StatefulSets, DaemonSets, Jobs; rolling updates with `maxSurge` and `maxUnavailable`.
- [ ] CV04.S04 — Networking: Services (ClusterIP, NodePort, LoadBalancer), Ingress, CoreDNS, NetworkPolicies.
- [ ] CV04.S05 — Health and scaling: probes, requests and limits, QoS classes, HPA with metrics-server. Load-test and watch it scale.
- [ ] CV04.S06 — Config and access: ConfigMaps, Secrets, ServiceAccounts, RBAC (Roles, ClusterRoles, bindings).
- [ ] CV04.S07 — Break-and-fix drill: CrashLoopBackOff, ImagePullBackOff, Pending, OOMKilled, a failing readiness probe. Cause each one, then fix it from `kubectl describe` and the events.
- [ ] CV04.S08 — Scheduling: taints and tolerations, affinity, PodDisruptionBudgets, draining a node safely.
- [ ] CV04.S09 — Defend the bullet: the HPA, probes, rolling updates and zero-downtime lines, plus RBAC.
**Gate artifact:** `qbank/CV04.md` at 8/10 + `labs/CV04/` (manifests and the break-and-fix notes).

## CV05 · Helm
<!-- rung: U | prereq: CV04 | feeds: ArgoCD, platform design -->
**Goal:** Write a chart from scratch and explain releases, upgrades and rollbacks.
**Resources:**
- [Helm documentation](https://helm.sh/docs/)
- [Helm — chart best practices](https://helm.sh/docs/chart_best_practices/)
**Sessions:**
- [ ] CV05.S01 — Question bank: 10 likely Helm questions for your CV; answer out loud and score.
- [ ] CV05.S02 — Chart anatomy: templates, values, `_helpers.tpl`; write a chart for a demo app from `helm create` down to only what you need.
- [ ] CV05.S03 — Lifecycle: install, upgrade, rollback, hooks, dependencies; `helm lint`, `helm template`, `helm diff`. Helm vs Kustomize — when each fits.
- [ ] CV05.S04 — Defend the bullet: "Helm charts" for your EKS and ECS services.
**Gate artifact:** `qbank/CV05.md` at 8/10 + `labs/CV05/` (your chart).

## CV06 · Terraform
<!-- rung: U | prereq: CV07 basics help | feeds: every IaC question — it's the top line of your experience -->
**Goal:** Explain state, modules and multi-environment layouts deeply enough to survive an IaC-heavy interview.
**Resources:**
- [Terraform documentation](https://developer.hashicorp.com/terraform/docs)
- [Terraform — S3 backend (state locking)](https://developer.hashicorp.com/terraform/language/backend/s3)
- [Gruntwork — Terraform tips and tricks](https://www.gruntwork.io/blog) — free articles
**Sessions:**
- [ ] CV06.S01 — Question bank: 10 likely Terraform questions for your CV; answer out loud and score.
- [ ] CV06.S02 — State: what's in a state file, why remote state, and locking (DynamoDB vs the S3 backend's newer `use_lockfile`). Run two `apply`s at once and watch the lock work.
- [ ] CV06.S03 — Modules: inputs, outputs, versioning, composition. Rebuild one of your nine internship modules from a blank file.
- [ ] CV06.S04 — Multiple environments: workspaces vs separate directories vs Terragrunt — the pros and cons, and why you chose what you chose.
- [ ] CV06.S05 — Change safely: drift, `import`, `moved` blocks, `state mv` and `state rm`, refactoring without destroying anything.
- [ ] CV06.S06 — The language: `for_each` vs `count`, dynamic blocks, `lifecycle`, data sources, provider aliases.
- [ ] CV06.S07 — Testing and CI: fmt, validate, tflint, checkov, plan-on-PR, `terraform test`.
- [ ] CV06.S08 — Defend the bullet: "9 reusable modules, 90+ resources, state locking to eliminate drift".
**Gate artifact:** `qbank/CV06.md` at 8/10 + `labs/CV06/` (the rebuilt module with tests and CI).

## CV07 · AWS Core Services
<!-- rung: U | prereq: CV02 | feeds: EKS/ECS, every cloud question -->
**Goal:** Explain IAM evaluation, the core services on your CV, and their failure and cost traps.
**Resources:**
- [AWS documentation](https://docs.aws.amazon.com)
- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
- [AWS Skill Builder](https://skillbuilder.aws) — free courses; Solutions Architect Associate prep, if you want the certificate
**Sessions:**
- [ ] CV07.S01 — Question bank: 10 likely AWS questions for your CV; answer out loud and score.
- [ ] CV07.S02 — IAM deep: identity vs resource policies, the evaluation logic, roles and trust policies, STS AssumeRole, permission boundaries, SCPs. Write one least-privilege policy by hand.
- [ ] CV07.S03 — Compute and storage: EC2 (instance types, Auto Scaling groups, launch templates); S3 (storage classes, bucket policies, encryption, versioning, lifecycle).
- [ ] CV07.S04 — Data: RDS (Multi-AZ vs read replicas, backups, point-in-time recovery); ElastiCache Redis (cluster mode, failover).
- [ ] CV07.S05 — The edge: ALB vs NLB, Route53, ACM, CloudFront.
- [ ] CV07.S06 — Security and ops: KMS envelope encryption and key policies, CloudTrail, CloudWatch metrics, logs and alarms, SNS.
- [ ] CV07.S07 — Cost: the pricing traps (NAT Gateway data, cross-AZ traffic, idle load balancers); redo the FinOps model from your internship ADRs.
- [ ] CV07.S08 — Defend the bullets: RDS PostgreSQL 16, ElastiCache, Amazon MQ, KMS, CloudWatch, CloudTrail.
**Gate artifact:** `qbank/CV07.md` at 8/10 + the hand-written IAM policy + a cost note.

## CV08 · EKS & ECS Fargate
<!-- rung: U | prereq: CV04, CV07 | feeds: container-platform interviews -->
**Goal:** Explain how AWS runs containers — and exactly how a pod gets AWS credentials.
**Resources:**
- [Amazon EKS Best Practices Guide](https://docs.aws.amazon.com/eks/latest/best-practices/introduction.html)
- [Amazon ECS developer guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)
**Sessions:**
- [ ] CV08.S01 — Question bank: 10 likely EKS/ECS questions for your CV; answer out loud and score.
- [ ] CV08.S02 — EKS architecture: the managed control plane; node groups vs Fargate vs Karpenter; the VPC CNI and IP exhaustion.
- [ ] CV08.S03 — IRSA vs EKS Pod Identity: the OIDC provider, the projected token, AssumeRoleWithWebIdentity — trace the whole path.
- [ ] CV08.S04 — Traffic in: the AWS Load Balancer Controller (Ingress → ALB), ExternalDNS, ACM vs cert-manager.
- [ ] CV08.S05 — ECS Fargate: task definitions, services, Cloud Map service discovery; ECS vs EKS — when you'd pick each.
- [ ] CV08.S06 — Operations: EKS version upgrades, managed add-ons, node rotation without downtime.
- [ ] CV08.S07 — Defend the bullets: "fault-tolerant microservices on EKS and ECS Fargate" and "IRSA".
**Gate artifact:** `qbank/CV08.md` at 8/10 + a diagram of the IRSA credential flow.

## CV09 · CI/CD with GitHub Actions
<!-- rung: U | prereq: CV03 | feeds: GitOps, security, platform design -->
**Goal:** Build a secure pipeline with keyless AWS access, and explain why every piece is there.
**Resources:**
- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [GitHub — configuring OpenID Connect in AWS](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-aws)
- [GitHub — security hardening for Actions](https://docs.github.com/en/actions/reference/security/secure-use)
**Sessions:**
- [ ] CV09.S01 — Question bank: 10 likely CI/CD questions for your CV; answer out loud and score.
- [ ] CV09.S02 — Workflows: jobs, matrices, caching, artifacts, reusable workflows, composite actions.
- [ ] CV09.S03 — OIDC to AWS: the trust policy and its `sub` condition; why it beats long-lived keys. Build it on this repo.
- [ ] CV09.S04 — Supply chain: Trivy in CI, SBOMs, signing with cosign, pinning actions by SHA, a least-privilege `GITHUB_TOKEN`.
- [ ] CV09.S05 — Pipeline design: build → test → scan → push → deploy; environments and required approvals.
- [ ] CV09.S06 — Defend the bullet: "keyless AWS OIDC authentication to eliminate long-lived credentials".
**Gate artifact:** `qbank/CV09.md` at 8/10 + a working, hardened workflow in `labs/CV09/`.

## CV10 · GitOps with ArgoCD
<!-- rung: U | prereq: CV05, CV09 | feeds: deployment-strategy and platform questions -->
**Goal:** Explain GitOps and run ArgoCD with multi-environment promotion and safe rollbacks.
**Resources:**
- [Argo CD documentation](https://argo-cd.readthedocs.io/en/stable/)
- [OpenGitOps principles](https://opengitops.dev)
- [Argo Rollouts](https://argoproj.github.io/rollouts/)
**Sessions:**
- [ ] CV10.S01 — Question bank: 10 likely GitOps/ArgoCD questions for your CV; answer out loud and score.
- [ ] CV10.S02 — The principles and the architecture: Applications, sync, self-heal, prune. Install ArgoCD on kind and deploy your Helm chart.
- [ ] CV10.S03 — At scale: app-of-apps, ApplicationSets, promoting between environments, Image Updater.
- [ ] CV10.S04 — Safety: sync waves and hooks, drift detection, rollbacks; a canary with Argo Rollouts.
- [ ] CV10.S05 — Defend the bullet: "automated GitOps CI/CD pipelines using GitHub Actions and ArgoCD".
**Gate artifact:** `qbank/CV10.md` at 8/10 + `labs/CV10/` (the app-of-apps repo layout).

## CV11 · DevSecOps — Vault, RBAC, KMS
<!-- rung: U | prereq: CV04, CV07 | feeds: security questions, platform design -->
**Goal:** Explain secrets, identity and least privilege across AWS and Kubernetes, and run Vault yourself.
**Resources:**
- [HashiCorp Vault tutorials](https://developer.hashicorp.com/vault/tutorials) — free
- [Kubernetes — security overview](https://kubernetes.io/docs/concepts/security/)
- [OWASP Top 10](https://owasp.org/projects/top-ten)
**Sessions:**
- [ ] CV11.S01 — Question bank: 10 likely security questions for your CV; answer out loud and score.
- [ ] CV11.S02 — Vault: architecture, unseal, auth methods (Kubernetes auth), secrets engines, dynamic Postgres credentials, leases. Run dev Vault on kind.
- [ ] CV11.S03 — Injecting secrets into pods: the Vault Agent injector vs the CSI driver vs External Secrets — trade-offs.
- [ ] CV11.S04 — Kubernetes hardening: Pod Security Standards, NetworkPolicies, encrypting secrets at rest with KMS, image admission policies.
- [ ] CV11.S05 — AWS hardening: least privilege, KMS, CloudTrail, GuardDuty, Security Hub; Secrets Manager vs Vault.
- [ ] CV11.S06 — Threat-model your own pipeline (STRIDE), plus OWASP Top 10 basics.
- [ ] CV11.S07 — Defend the bullet: "IRSA, Kubernetes RBAC and dynamic secrets injection via HashiCorp Vault".
**Gate artifact:** `qbank/CV11.md` at 8/10 + `labs/CV11/` (Vault on kind with dynamic database credentials).

## CV12 · Observability — Prometheus, Grafana, Alertmanager
<!-- rung: U | prereq: CV04 | feeds: SRE loops, incident questions -->
**Goal:** Instrument a service, write PromQL fluently, and alert on symptoms, not causes.
**Resources:**
- [Prometheus documentation](https://prometheus.io/docs/introduction/overview/)
- [PromLabs — PromQL cheat sheet](https://promlabs.com/promql-cheat-sheet/)
- [Google SRE book — Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
**Sessions:**
- [ ] CV12.S01 — Question bank: 10 likely observability questions for your CV; answer out loud and score.
- [ ] CV12.S02 — Prometheus: the pull model, exporters, service discovery, the data model, retention. Install kube-prometheus-stack on kind.
- [ ] CV12.S03 — PromQL: `rate` vs `irate`, counters vs gauges, histograms and `histogram_quantile`, aggregation. Write 15 queries.
- [ ] CV12.S04 — SLIs: RED, USE and the four golden signals; recording rules and a burn-rate alert for a demo service.
- [ ] CV12.S05 — Grafana dashboards as code; Alertmanager routing, grouping, inhibition and silences.
- [ ] CV12.S06 — Logs and traces: Loki, OpenTelemetry, CloudWatch Logs Insights — when you need each.
- [ ] CV12.S07 — Defend the bullet: "9 custom application SLIs and automated alert routing".
**Gate artifact:** `qbank/CV12.md` at 8/10 + `labs/CV12/` (rules, dashboards and the 15 queries).

## CV13 · Python, SQL & APIs for DevOps
<!-- rung: S | prereq: none | feeds: the coding round, your projects -->
**Goal:** Be honest and solid on the languages on your CV — Python for automation, SQL for data, FastAPI for your projects.
**Resources:**
- [Boto3 documentation](https://docs.aws.amazon.com/boto3/latest/)
- [PostgreSQL tutorial](https://neon.com/postgresql/tutorial) — free
- [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/)
**Sessions:**
- [ ] CV13.S01 — Question bank: 10 likely language questions for your CV; answer out loud and score. Decide your honest level for each language listed.
- [ ] CV13.S02 — Python automation: a packaged CLI with `argparse`, `logging`, typing and boto3.
- [ ] CV13.S03 — Testing: pytest fixtures and parametrize, mocking AWS with `moto`.
- [ ] CV13.S04 — SQL: joins, GROUP BY, window functions, indexes, reading `EXPLAIN ANALYZE` — 10 queries on Postgres.
- [ ] CV13.S05 — FastAPI: rebuild one Sentinel Trading endpoint with validation and tests.
- [ ] CV13.S06 — Defend the line: "Python, Bash, HCL, SQL, TypeScript, Java" — what you've built in each, and what you'd still need to learn.
**Gate artifact:** `qbank/CV13.md` at 8/10 + `labs/CV13/` (the CLI and the SQL file).

## CV14 · Your Story — Projects, Internship & Behavioural
<!-- rung: S | prereq: none | feeds: every interview's first and last 15 minutes -->
**Goal:** Tell your story in two minutes, walk through any project for 15, and have a STAR story ready for every common question.
**Resources:**
- [Tech Interview Handbook — behavioural interviews](https://www.techinterviewhandbook.org/behavioral-interview/)
- [Amazon Leadership Principles](https://www.amazon.jobs/content/en/our-workplace/leadership-principles) — the most common behavioural framework
**Sessions:**
- [ ] CV14.S01 — "Tell me about yourself": write a two-minute version, then say it out loud ten times. Your First in Computer Science, the internship, what you want next.
- [ ] CV14.S02 — Eight STAR stories from the internship and your projects: ownership, failure, conflict, a tight deadline, learning fast, disagreement, impact with numbers, helping others (your ADRs).
- [ ] CV14.S03 — Sentinel Trading deep dive: an architecture diagram, the key decisions, and what you'd change — a 15-minute walk-through, recorded.
- [ ] CV14.S04 — LivestockChain deep dive, the same way.
- [ ] CV14.S05 — The internship platform end to end, from memory: VPC → EKS/ECS → GitHub Actions → ArgoCD → Vault → Prometheus.
- [ ] CV14.S06 — Your questions for them, and how to close an interview well.
- [ ] CV14.S07 — A recorded mock behavioural interview: five questions, scored on STAR structure and specifics.
- [ ] CV14.S08 — After every real interview: add the questions you were asked to the right question bank and re-rate (`today rate`).
**Gate artifact:** `qbank/CV14.md` (pitch + 8 STAR stories) + both project walk-throughs recorded and noted.
