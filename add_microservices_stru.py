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

base_dir = "services"

template_app = '''from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {{"message": "Hello from {name}!"}}
'''

template_dockerfile = '''FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
'''

template_deployment = '''apiVersion: apps/v1
kind: Deployment
metadata:
  name: {name}-deployment
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
          image: yourrepo/{name}:latest
          ports:
            - containerPort: 8000
'''

os.makedirs(base_dir, exist_ok=True)

for name in services:
    path = os.path.join(base_dir, name)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "app.py"), "w") as f:
        f.write(template_app.format(name=name))
    with open(os.path.join(path, "Dockerfile"), "w") as f:
        f.write(template_dockerfile)
    os.makedirs(os.path.join(path, "k8s"), exist_ok=True)
    with open(os.path.join(path, "k8s", "deployment.yaml"), "w") as f:
        f.write(template_deployment.format(name=name))

print("✅ Services scaffolded.")
