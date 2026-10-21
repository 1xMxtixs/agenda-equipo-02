# Testing Capabilities — agenda-equipo-02

**Strict TDD Mode**: enabled
**Detected**: 2026-10-21
**Source**: detected runner fallback (no `strict_tdd` marker in agent files, no `strict_tdd:` key in `openspec/config.yaml`; test runner present → `strict_tdd: true`)

## Test Runner

- Command: `.venv/Scripts/python -m pytest -q`
- Framework: pytest 9.1.1 (declared `pytest>=8.0.0` in `requirements.txt`)
- Local runtime: Python 3.14.3 (`.venv`), verified — 11 passed
- CI runtime: Python 3.11 (`.github/workflows/ci.yml` runs `python -m pytest`)

## Test Layers

| Layer | Available | Tool |
| --- | --- | --- |
| Unit | ✅ | pytest (`tests/test_agenda.py`, 11 tests) |
| Integration | ✅ | `fastapi.testclient.TestClient` + httpx 0.28.1 (API → SQLite end-to-end in-process) |
| E2E | ❌ | — (no playwright/cypress/selenium) |

## Coverage

- Available: ✅ (`pytest-cov` 7.1.0 in `requirements.txt`)
- Command: `.venv/Scripts/python -m pytest -q --cov=app` (not yet verified)
- No coverage threshold configured (no `pytest.ini`/`pyproject.toml`).

## Quality Tools

| Tool | Available | Command |
| --- | --- | --- |
| Linter | ❌ | — (no ruff/flake8/pylint config or dependency) |
| Type checker | ❌ | — (no mypy/pyright config or dependency) |
| Formatter | ❌ | — (no black/ruff-format config or dependency) |

## Notes

- No `pyproject.toml`, `pytest.ini`, or `Makefile`: pytest runs with default configuration from the project root.
- Test command of record for SDD phases: `.venv/Scripts/python -m pytest -q`.
- Adding linters/type checkers/coverage gates requires human approval per `openspec/config.yaml` and `docs/architecture.md` (no new technologies without approval).
- Detected mid-session (2026-10-21 11:04, concurrent work, not created by this init): `requirements-dev.txt` (`-r requirements.txt`, pytest, httpx — still no linters) and a second workflow `.github/workflows/ci-agenda.yml` running `.venv`-equivalent `python -m pytest -q --junitxml=reports/junit.xml` on Python 3.11 (change `openspec/changes/automatizar-ci-agenda/`). Layer/tool verdicts above remain valid.
