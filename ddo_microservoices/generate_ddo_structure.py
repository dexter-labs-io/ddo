
import os

structure = {
    "ddo": [
        "core",
        "plugins/agents",
        "plugins/tools",
        "plugins/planners",
        "plugins/memory",
        "services/orchestrator",
        "services/api/routes",
        "services/api/schemas",
        "services/memory",
        "services/telemetry",
        "services/devtools",
        "config",
        "telemetry",
        "cli",
        "sdk",
        "scripts",
        "tests",
        "docker/jaeger",
        "docs"
    ]
}

files_to_create = [
    "README.md",
    "pyproject.toml",
    "core/orchestrator.py",
    "core/planner.py",
    "core/executor.py",
    "core/memory_manager.py",
    "core/plugin_loader.py",
    "config/settings.py",
    "scripts/run_demo.py",
    "services/orchestrator/main.py",
    "services/orchestrator/requirements.txt",
    "services/orchestrator/Dockerfile",
    "services/api/main.py",
    "services/api/Dockerfile",
    "cli/ddo_cli.py",
    "sdk/client.py",
    "docker/docker-compose.yml",
    "docker/jaeger/config.yml",
    "docs/architecture.md",
    "docs/ddo_external_integration.md"
]

def create_structure(base_dir=".", structure_dict=structure, files=files_to_create):
    for root, dirs in structure_dict.items():
        for d in dirs:
            path = os.path.join(base_dir, root, d)
            os.makedirs(path, exist_ok=True)
            print(f"Created directory: {path}")
    for file in files:
        filepath = os.path.join(base_dir, "ddo", file)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w") as f:
            f.write("")
        print(f"Created file: {filepath}")

if __name__ == "__main__":
    create_structure()
