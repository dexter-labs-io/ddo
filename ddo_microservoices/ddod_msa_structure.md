ddo/
│
├── core/                          # Core orchestration logic (used by all services)
│   ├── orchestrator.py
│   ├── planner.py
│   ├── executor.py
│   ├── memory_manager.py
│   ├── policy.py
│   └── plugin_loader.py
│
├── plugins/                       # Swappable agents, tools, planners, memory
│   ├── agents/
│   ├── tools/
│   ├── planners/
│   └── memory/
│
├── config/                        # Shared configuration
│   ├── settings.py
│   └── plugin_config.yaml
│
├── telemetry/                     # Logs, tracing, observability
│   ├── logger.py
│   ├── tracer.py
│   └── audit.py
│
├── services/                      # Microservices: each is independently deployable
│   ├── orchestrator/
│   │   ├── main.py                # Exposes orchestrator.run() via REST
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   └── service_config.yaml
│   │
│   ├── api/
│   │   ├── main.py                # FastAPI service
│   │   ├── routes/
│   │   │   ├── agent_routes.py
│   │   │   ├── tool_routes.py
│   │   │   ├── memory_routes.py
│   │   │   └── ask.py
│   │   ├── schemas/
│   │   └── Dockerfile
│   │
│   ├── memory/
│   │   ├── main.py                # Optional external memory API wrapper
│   │   └── Dockerfile
│   │
│   ├── telemetry/
│   │   ├── main.py
│   │   └── Dockerfile
│   │
│   └── devtools/
│       ├── seed.py
│       ├── bootstrap.py
│       └── run_agent.py
│
├── sdk/                           # Python SDK to call the API
│   ├── client.py
│   └── examples/
│
├── cli/                           # CLI tools to drive local usage
│   ├── ddo_cli.py
│   └── utils.py
│
├── tests/                         # Unit + integration tests
│   ├── test_orchestrator.py
│   ├── test_plugins.py
│   └── test_memory.py
│
├── scripts/                       # Scripts for quick testing
│   ├── run_demo.py
│   └── test_cases/
│
├── docker/                        # Container setup and orchestration
│   ├── docker-compose.yml
│   ├── .env
│   ├── redis/
│   │   └── redis.conf
│   ├── jaeger/
│   │   └── config.yml
│   └── volumes/
│
├── docs/                          # Docs and diagrams
│   ├── architecture.md
│   ├── sequences.md
│   ├── ddo_external_integration.md
│   └── README.md
│
├── pyproject.toml / requirements.txt
└── README.md
