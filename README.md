# DDO – Domain-Driven Orchestration
# DDO – Domain-Driven Orchestration for GenAI

Welcome to the official repository of **DDO (Domain-Driven Orchestration)** — the open, modular, and secure orchestration framework for deploying intelligent GenAI workflows at scale.

DDO allows enterprises and developers to orchestrate AI agents, LLMs, toolchains, and memory across domains, clouds, and execution layers, all under a unified governance and observability fabric.

---

## 🚀 Key Features

- **Domain Context Awareness** – Route GenAI requests based on persona, role, intent, and business domain
- **Pluggable Agent Runtimes** – Works with LangChain, CrewAI, LangGraph, MetaGPT, etc.
- **LLM-Agnostic ToolRouter** – OpenAI, Bedrock, Claude, Gemini, watsonx.ai, OSS models
- **Unified Memory Bus** – Redis, Weaviate, Postgres, Chroma, DuckDB, Zep
- **Governance Layer** – Policy enforcement (e.g., AI Act, GDPR, RBAC)
- **Telemetry & Replay** – Traceability for audit, optimization, and debugging
- **Microservices Native** – Built for OpenShift, ROSA, or K8s with service mesh

---

## 🧱 Core Architecture

See [framework.md](./framework.md) for the full component breakdown.

- `OrchestrationEngine`
- `DomainContextManager`
- `ToolRouter`
- `MemoryManager`
- `GovernanceEngine`
- `TelemetryService`

---

## 🛠️ Quick Start (WIP)

```bash
# Clone repo
$ git clone https://github.com/your-org/ddo.git && cd ddo

# Start orchestrator service locally
$ cd orchestrator && python3 main.py

# Run agent test (example)
$ curl localhost:8000/api/execute -d '{"prompt": "Generate legal summary"}'
```

> ⚠️ In active refactoring to support full microservices architecture. See roadmap.

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](./CONTRIBUTING.md)

---

## 📜 License

Apache 2.0

---

## 💰 Fundraising & Vision

DDO is being developed as an open-core orchestration platform with enterprise deployment, edge adaptation, and regulatory compliance at its heart. We are actively raising **£7M–10M** in early-stage funding to:

- Complete OSS architecture + cloud-native deployment
- Launch managed SaaS version (Equinix + private cloud interconnect)
- Enable integration with major cloud LLMs (Bedrock, Azure OpenAI, watsonx, Claude)
- Build UI kits for business user orchestration