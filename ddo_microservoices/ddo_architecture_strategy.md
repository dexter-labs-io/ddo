# 📐 Architectural Strategy – DDO Microservices

## Objective

This architecture defines the distributed, scalable, and secure deployment strategy for **DDO (Domain-Driven Orchestration)** as a cloud-native microservice platform. It is optimized for multi-AZ (Availability Zone) deployments and service mesh integration using **Istio**.

### Core Goals:
- **High Availability (HA)**: fault tolerance via AZ redundancy  
- **Horizontal Scalability**: independently scalable microservices  
- **Domain Isolation**: separate core responsibilities (orchestration, planning, execution, memory)  
- **Zero Trust Security**: mTLS, strict communication policies, and minimal exposure  
- **Native Observability**: full tracing, telemetry, and diagnostics via Istio and OpenTelemetry

## Core Microservices

| Microservice         | Description                                              | Ingress | Egress | AZ Replication |
|----------------------|----------------------------------------------------------|---------|--------|----------------|
| `ddo-orchestrator`   | Coordinates the THINK → PLAN → ACT → REFLECT loop        | ✅      | ❌     | ✅              |
| `ddo-planner`        | Generates execution plans based on prompts and context   | ❌      | ❌     | ✅              |
| `ddo-executor`       | Executes tool calls and agent steps defined in the plan  | ❌      | ✅     | ✅              |
| `ddo-memory`         | Stores and retrieves per-agent memory and context        | ❌      | ❌     | ✅              |
| `ddo-api-gateway`    | Public-facing entrypoint for external API consumers      | ✅      | ❌     | ✅              |
| `ddo-egress-gateway` | Routes and governs outbound traffic to external systems  | ❌      | ✅     | ✅              |

## Deployment Strategy – Multi-AZ with Istio Mesh

- All core services are deployed as **independent pods**, with at least one replica per AZ for fault tolerance.
- Each pod includes an **Istio sidecar proxy**, enabling:
  - Secure internal traffic via **mutual TLS (mTLS)**
  - Declarative traffic routing
  - Distributed tracing and observability
- **Entry and exit points** are controlled via:
  - `Istio IngressGateway`: handles inbound prompts and API calls
  - `Istio EgressGateway`: governs external API/tool access (e.g., GPT, watsonx, Bedrock)

## Security, Isolation & Policy Design

- **Zero Trust Principle**: Every communication is explicitly authorized with strict `AuthorizationPolicy` rules.
- **Service Communication Boundaries**:
  - `orchestrator` can call `planner`, `executor`, and `memory`
  - `executor` is allowed to communicate only with plugins or external agents (via abstraction)
  - `memory` is accessible only to internal core components, never exposed externally
- **No direct tool/API access** is permitted from the `planner` or `memory` services.

## Observability & Governance

- **Distributed tracing** is enabled through Istio and integrated with OpenTelemetry and Jaeger.
- **Logs, metrics, and spans** are exported to the observability stack for full lifecycle visibility.
- Future plans include:
  - **Telemetry hooks for plugin/tool execution**
  - **Governance layer integrations** (e.g., policy evaluation pre- and post-execution)
