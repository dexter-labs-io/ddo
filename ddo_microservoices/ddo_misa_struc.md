# DDO Microservices Architecture – Phase-Aligned Structure

This document describes the file and directory structure of the DDO platform as a modular, microservices-based system. The architecture supports local development, container-based deployment, and cloud-native orchestration.

---

## 🧱 High-Level Structure

```bash
ddo/
│
├── core/                          # Core orchestration components (used by orchestrator)
│   ├── orchestrator.py
│   ├── planner.py
│   ├── executor.py
│   ├── memory_manager.py
│   └── plugin_loader.py
│
├── plugins/                       # Pluggable tools, agents, memory, planners
│   ├── agents/
│   ├── tools/
│   ├── planners/
│   └── memory/
│
├── services/                      # Each service is a standalone microservice
│   ├── orchestrator/
│   │   ├── main.py
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   │
│   ├── api/
│   │   ├── main.py
│   │   ├── routes/
│   │   ├── schemas/
│   │   └── Dockerfile
│   │
│   ├── memory/
│   ├── telemetry/
│   └── devtools/
│
├── config/                        # Shared system configs
│   ├── settings.py
│   ├── plugin_config.yaml
│   └── .env
│
├── telemetry/                     # Tracing/logging logic used by services
│   ├── logger.py
│   └── tracer.py
│
├── cli/                           # CLI entrypoints and commands
│   └── ddo_cli.py
│
├── sdk/                           # SDK to use DDO from other apps or scripts
│   └── client.py
│
├── scripts/                       # Demos and dev-only utilities
│   └── run_demo.py
│
├── tests/                         # Unit and integration tests
│
├── docker/                        # Docker orchestration (compose, volumes, redis)
│   ├── docker-compose.yml
│   └── jaeger/
│
├── docs/                          # Documentation and design diagrams
│
├── pyproject.toml / requirements.txt
└── README.md
