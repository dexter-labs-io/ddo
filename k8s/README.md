# Kubernetes Configuration – DDO Deployment Layer

This directory contains Kubernetes configuration files used to deploy the DDO (Domain-Driven Orchestration) microservices into an OpenShift or Minikube-based cluster.

## 📁 Directory Structure

- `namespace.yaml`  
  Defines the Kubernetes namespace `ddo` where all services will be deployed.

## 📦 Microservice Deployment Structure

Each microservice under `services/<service-name>/` includes:

services/
└── <service-name>/
└── k8s/
├── deployment.yaml # Describes the Deployment resource for the service
└── service.yaml # Exposes the service within the cluster (ClusterIP)


> These YAMLs are auto-generated via the script: `scripts/init_k8s_structure.py`

## 🚀 Deployment Instructions

1. **Set up Docker build environment for Minikube (if local):**
   ```bash
   eval $(minikube docker-env)
2. Build all service images locally:
    make build
3. Deploy all resources:
    ./deploy_all.sh
    or
    make deploy
4. Port-forward a service to test locally:
    kubectl -n ddo port-forward service/orchestrator 8080:80