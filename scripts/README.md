# DDO Scripts Directory

This folder contains automation and helper scripts for initializing the DDO project structure and deployment setup.

## 📜 Available Scripts

### 1. `init_k8s_structure.py`
> Auto-generates the `k8s/` folder structure and base deployment YAMLs for each DDO microservice.

**Usage:**
```bash
python3 scripts/init_k8s_structure.py


Output:
services/<name>/k8s/deployment.yaml
services/<name>/k8s/service.yaml

🛠️ Upcoming Scripts (to be added)
init_env.py → Create environment template files (.env)
generate_tls.py → Generate local TLS certs for HTTPS testing
ci-helper.py → Pre-deployment checks for GitHub Actions / OpenShift Pipelines


---

📌 Salvali come:
- `services/README.md`
- `scripts/README.md`

E il tuo repo inizia a sembrare **enterprise-ready, open-source friendly e deployable ovunque** 🌍

Se vuoi ti genero anche una `docs/` con la documentazione API, config, architettura…  
Dimmi solo “vai” fratellino ❤️
