import os

services = [
    "orchestrator",
    "domain-context",
    "tool-router",
    "memory-manager",
    "governance-engine",
    "telemetry-agent",
    "api-gateway"
]

base_path = "services"

deployment_template = '''apiVersion: apps/v1
kind: Deployment
metadata:
  name: {name}
  labels:
    app: {name}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {name}
  template:
    metadata:
      labels:
        app: {name}
    spec:
      containers:
      - name: {name}
        image: {name}:latest
        ports:
        - containerPort: 8000
'''

service_template = '''apiVersion: v1
kind: Service
metadata:
  name: {name}
spec:
  selector:
    app: {name}
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8000
'''

for svc in services:
    k8s_path = os.path.join(base_path, svc, "k8s")
    os.makedirs(k8s_path, exist_ok=True)

    with open(os.path.join(k8s_path, "deployment.yaml"), "w") as f:
        f.write(deployment_template.format(name=svc))

    with open(os.path.join(k8s_path, "service.yaml"), "w") as f:
        f.write(service_template.format(name=svc))

print("✅ K8s structure and templates created.")
