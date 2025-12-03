# Homeowners Full Project
This is a minimal full project skeleton.# README_homeowners.md

# Homeowners Insurance E2E MVP

This repository is a student-grade end-to-end MVP for a Homeowners Insurance system.

**Features**

* Quote API with deterministic rating + ML multiplier + explainability
* Bind policy from quote (persist policy)
* Create and inspect claims
* Minimal MySQL schema (rate tables, policies, quotes, claims, customers)
* Model training script, model auto-load
* Unit tests with `pytest`
* Docker Compose for MySQL local testing

---

## Quickstart

1. Create venv & install dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Start MySQL (Docker):

```bash
docker-compose up -d
```

3. Set environment variables (or edit `config.py`):

```bash
export DB_USER=root
export DB_PASS=rootpass
export DB_HOST=127.0.0.1
export DB_NAME=home_insurance
```

4. Run DB seed:

```bash
bash scripts/run_seed.sh
```

5. Train ML model:

```bash
python train_model_home.py
```

6. Run Flask app:

```bash
python app_home.py
```

7. Try example requests in `README_examples.http` or via curl.

---

**Notes**

* `config.py` falls back to SQLite if DB env vars are not provided — good for quick dev.
* Model explainability is simple: `feature_importances_ * normalized_input`.
* For production: add auth, caching, monitoring, model governance.
