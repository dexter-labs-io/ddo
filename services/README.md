# DDO Microservices Directory

This directory contains the microservices that make up the DDO (Domain-Driven Orchestration) architecture. Each service is containerized and deployable via Kubernetes manifests under its own `k8s/` subdirectory.

## 📁 Structure

Each subfolder contains one DDO component:

services/
├── orchestrator/
├── domain-context/
├── tool-router/
├── memory-manager/
├── governance-engine/
├── telemetry-agent/
├── api-gateway/


Inside each service directory:
<service-name>/
├── app.py # Core logic (to be implemented)
├── Dockerfile # Container build file
└── k8s/
├── deployment.yaml # Kubernetes deployment config
└── service.yaml # Kubernetes service config


## 🔧 Notes

- Services communicate internally via the Kubernetes network (ClusterIP).
- Each service should expose its functionality over HTTP (default: port 8000).
- Docker image tag: `:latest` by default (can be customized for CI/CD).

## 📌 Developer Tips

- Keep services lightweight and stateless.
- Use logging and health checks where applicable.
- Follow the modular DDO architecture in `framework.md`.

---

Maintained by the DDO Engineering Team
