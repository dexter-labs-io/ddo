structure = {
    "ddo-core": [
        "__init__.py", 
        "agent.py", 
        "domain.py", 
        "tool.py", 
        "router.py",       # <--- NEW: ToolRouter logic qui
        "README.md"
    ],
    "ddo-runtime": [
        "__init__.py", 
        "runtime.py", 
        "pipeline.py",     # <--- NEW: definisce pipeline di inferenza
        "README.md",
        ("memory", [
            "__init__.py", 
            "vectorstore.py", 
            "redis.py", 
            "filecache.py", 
            "memory_manager.py"  # <--- NEW: per gestire backend dinamici
        ])
    ],
    "ddo-gov": [
        "__init__.py", 
        "telemetry.py", 
        "audit.py", 
        "policy.py", 
        "compliance.py",    # <--- NEW: AI Act, GDPR etc.
        "README.md"
    ],
    "ddo-plugins": [
        "__init__.py", 
        "openai_plugin.py", 
        "watsonx_plugin.py", 
        "search_plugin.py", 
        "huggingface_plugin.py",  # <--- NEW
        "README.md"
    ],
    "ddo-ui": [  # <--- NEW: UI per UX di business users
        "__init__.py",
        "dashboards.py",
        "input_builder.py",
        "output_renderer.py",
        "README.md"
    ],
    "examples": [
        ("finance_demo", ["run.py", "config.yaml"]),
        ("healthcare_demo", ["run.py", "config.yaml"]),
        "README.md"
    ],
    "tests": [
        "test_core.py", 
        "test_runtime.py", 
        "test_plugins.py",
        "test_ui.py",         # <--- NEW
        "test_governance.py", # <--- NEW
        "README.md"
    ],
    "docs": [  # <--- NEW: cartella per documentazione tecnica
        "architecture.md",
        "contributing.md",
        "deployment.md",
        "glossary.md"
    ],
    ".github": [  # <--- NEW: automation GitHub Actions
        ("workflows", ["ci.yml", "lint.yml"])
    ]
}


