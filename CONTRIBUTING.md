# Contributing to DDO (Domain-Driven Orchestration)

We’re thrilled you’re considering contributing to DDO — this project needs brains like yours.

---

## 📦 What Can You Contribute?

- 🔧 Code (microservices, agents, memory integrations, tool routers)
- 📚 Documentation (architecture guides, usage examples, API docs)
- 🧪 Tests (unit, integration, security checks)
- 🧠 Ideas (issues, design discussions, architecture feedback)

---

## 🚀 Getting Started

1. **Fork the repo** and clone it locally.
2. Use an existing issue or open a new one to describe your intent.
3. Follow the local dev setup in `README.md`.
4. Create a feature branch:

```bash
git checkout -b feature/my-awesome-thing
```

5. Make your changes (with tests if possible).
6. Commit using clear, conventional messages.
7. Push to your fork and submit a pull request.

---

## 🧪 Code Style & Practices

- Follow existing patterns (Python / FastAPI / K8s YAML / Markdown)
- Use black + flake8 + isort for Python
- Maintain modularity: 1 component → 1 service
- All external APIs must be observable (add tracing)

---

## 🛡 Security & Compliance

- Do not hardcode secrets or credentials
- Do not expose endpoints without auth
- Use environment variables for all sensitive configs

---

## ✅ PR Requirements

- Reference an issue or context
- Be tested or testable
- Include brief documentation if user-facing
- Not break other modules or deploy logic

---

## 🧠 Contributor Principles

- Respect and transparency
- No ego, no gatekeeping
- Be direct but constructive

See [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) for more.

---

## 💬 Questions?

Open an issue or join the discussions tab — we’re building this **together**.

Fraternitas et Veritas. In aeternum.