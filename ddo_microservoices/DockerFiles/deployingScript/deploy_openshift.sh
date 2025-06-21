#!/bin/bash

set -e

NAMESPACE="ddo-system"

echo "⏳ Creating namespace and service account..."
oc create namespace $NAMESPACE || true
oc apply -f helm/templates/namespace.yaml
oc apply -f helm/templates/serviceaccount.yaml
oc apply -f helm/templates/rbac.yaml

echo "🔑 Creating config and secrets..."
oc apply -f helm/templates/configmap.yaml
oc apply -f helm/templates/secret.yaml

echo "🚀 Installing Helm chart..."
helm upgrade --install ddo ./helm --namespace $NAMESPACE

echo "📡 Port-forwarding to service..."
kubectl port-forward svc/ddo-orchestrator -n $NAMESPACE 8080:8080
