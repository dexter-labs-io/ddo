#!/bin/bash

echo "🚀 Creating DDO namespace..."
kubectl apply -f k8s/namespace.yaml

SERVICES=(
  orchestrator
  domain-context
  tool-router
  memory-manager
  governance-engine
  telemetry-agent
  api-gateway
)

for svc in "${SERVICES[@]}"
do
  echo "📦 Deploying $svc..."
  kubectl apply -n ddo -f services/$svc/k8s/deployment.yaml
  kubectl apply -n ddo -f services/$svc/k8s/service.yaml
done

echo "✅ All services deployed to namespace 'ddo'"
