import os

# Define base path relative to current working directory
base_path = os.path.join(os.getcwd(), "ddo", "helm")

# Define the Helm folder structure
helm_structure = [
    "charts",               # For Helm dependencies (if needed)
    "templates",            # Core Kubernetes manifests
    "templates/istio",      # Istio manifests
    "config",               # External config files
    "secrets",              # Sealed secrets or configmaps
    "scripts",              # Utility or setup scripts
    "docs"                  # Helm chart documentation
]

# Define the files with initial content
files_content = {
    "Chart.yaml": """\
apiVersion: v2
name: ddo
description: A Helm chart for deploying DDO microservices on OpenShift with Istio
type: application
version: 0.1.0
appVersion: "1.0"
""",

    "values.yaml": """\
global:
  namespace: ddo-system
  imagePullPolicy: IfNotPresent
  istio:
    enabled: true
    gateway: istio-ingressgateway
    hosts:
      - ddo.example.com

ddoOrchestrator:
  image: ddo/orchestrator:latest
  replicas: 2
  port: 8000
""",

    "templates/ddo-orchestrator-deployment.yaml": """\
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ddo-orchestrator
spec:
  replicas: {{ .Values.ddoOrchestrator.replicas }}
  selector:
    matchLabels:
      app: ddo-orchestrator
  template:
    metadata:
      labels:
        app: ddo-orchestrator
    spec:
      containers:
        - name: orchestrator
          image: {{ .Values.ddoOrchestrator.image }}
          ports:
            - containerPort: {{ .Values.ddoOrchestrator.port }}
          imagePullPolicy: {{ .Values.global.imagePullPolicy }}
""",

    "templates/ddo-orchestrator-service.yaml": """\
apiVersion: v1
kind: Service
metadata:
  name: ddo-orchestrator
spec:
  selector:
    app: ddo-orchestrator
  ports:
    - protocol: TCP
      port: 80
      targetPort: {{ .Values.ddoOrchestrator.port }}
""",

    "templates/istio/virtualservice.yaml": """\
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: ddo-orchestrator
spec:
  hosts:
    - {{ .Values.global.istio.hosts | first }}
  gateways:
    - {{ .Values.global.istio.gateway }}
  http:
    - match:
        - uri:
            prefix: /orchestrator
      route:
        - destination:
            host: ddo-orchestrator
            port:
              number: 80
""",

    "templates/istio/destinationrule.yaml": """\
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: ddo-orchestrator
spec:
  host: ddo-orchestrator
  trafficPolicy:
    loadBalancer:
      simple: ROUND_ROBIN
"""
}

# Create directories
for folder in helm_structure:
    os.makedirs(os.path.join(base_path, folder), exist_ok=True)

# Create files with content
for relative_path, content in files_content.items():
    file_path = os.path.join(base_path, relative_path)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as f:
        f.write(content)

print(f"✅ DDO Helm chart structure created at {base_path}")
