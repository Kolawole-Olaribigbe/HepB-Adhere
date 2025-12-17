# Copilot / AI Agent Instructions — HepB Adhere

This file gives focused, repo-specific guidance so an AI coding agent can be immediately productive.

1) Project overview
- Backend: FastAPI app at [backend/app/main.py](backend/app/main.py). API router is mounted at `/api/v1`.
- Frontend: React app in [frontend/web](frontend/web) (run with `npm start`).
- Infra: `docker-compose.yml` defines `backend`, `frontend`, `db` (Postgres) and `redis` (see root `docker-compose.yml`).

2) Key integration points to know
- SMS: Twilio wrapper in [backend/app/services/twilio_client.py](backend/app/services/twilio_client.py). Expects Twilio credentials via env (see [backend/.env.example](backend/.env.example)).
- USSD: session objects and state machine live in [backend/app/services/ussd_session.py](backend/app/services/ussd_session.py). They are in-memory objects — persistence patterns are explicit in code.
- Background tasks: Celery tasks in [backend/app/tasks/worker.py](backend/app/tasks/worker.py) use Redis as broker (`redis://localhost:6379/0`). Start a worker with `celery -A app.tasks.worker worker --loglevel=info`.
- Database: SQLAlchemy session in [backend/app/db/session.py](backend/app/db/session.py) and migrations in [backend/migrations](backend/migrations) with `alembic.ini` at [backend/alembic.ini](backend/alembic.ini).

3) How to run & common developer workflows
- Local backend (dev):
  - `cd backend`
  - create venv and install: `python -m venv venv` then `venv\\Scripts\\activate` (Windows) and `pip install -r requirements.txt` ([backend/requirements.txt](backend/requirements.txt)).
  - set env vars from [backend/.env.example](backend/.env.example).
  - run DB migrations: `alembic upgrade head` (run from `backend`).
  - start server: `uvicorn app.main:app --reload` (binds to port 8000 in compose).
- Docker (recommended for full stack): `docker-compose up --build` from repo root — this runs Postgres and Redis automatically.
- Celery: ensure Redis is running (or use compose) then `celery -A app.tasks.worker worker --loglevel=info`.
- Tests: run `pytest backend` (tests are under `backend/tests`).

4) API & routing conventions
- Routes are grouped under `app.api.v1.routes`. Check: [backend/app/api/v1/routes/patients.py](backend/app/api/v1/routes/patients.py), `sms.py`, and `ussd.py` for examples of request handling and dependency usage in `deps.py`.
- Responses are simple Pydantic schemas under [backend/app/schemas](backend/app/schemas). Use these models when generating or modifying route handlers.

5) Code patterns and conventions to follow
- Services: utility logic lives in `app.services` (plain classes or functions). Prefer importing and calling service functions directly (see `twilio_client.py`, `ussd_session.py`).
- Tasks: background jobs call service functions (worker tasks are thin wrappers). Keep task code small and idempotent.
- DB access: prefer using the session helpers in `app.db.session` and models under `app.models` (see `backend/app/models/patient.py`).
- Config: centralized in [backend/app/core/config.py](backend/app/core/config.py). Read settings from `settings` rather than hard-coding.

6) Safety and operational notes
- Twilio calls are live — avoid sending real SMS in tests. Use mocking in tests or configure Twilio sandbox/test credentials.
- USSD flows are stateful and currently in-memory; be cautious when refactoring `USSDSession` — long-running flows expect session state management.

7) Useful files to reference during changes
- [backend/app/main.py](backend/app/main.py) — entrypoint
- [backend/app/api/v1/routes/patients.py](backend/app/api/v1/routes/patients.py) — example route
- [backend/app/services/twilio_client.py](backend/app/services/twilio_client.py) — Twilio integration
- [backend/app/services/ussd_session.py](backend/app/services/ussd_session.py) — USSD state
- [backend/app/tasks/worker.py](backend/app/tasks/worker.py) — Celery tasks
- [backend/requirements.txt](backend/requirements.txt) and [docker-compose.yml](docker-compose.yml)

8) When making changes
- Update or add migrations under [backend/migrations](backend/migrations) and run `alembic upgrade head`.
- Add/adjust Pydantic schemas in `app/schemas` when changing route I/O.
- If you modify background behavior, update Celery task signatures and search for `@celery.task` usages.

If anything above is unclear or you want this tailored to a different agent persona (test-writer, refactorer, or feature implementer), tell me which persona and I'll refine the instructions.
