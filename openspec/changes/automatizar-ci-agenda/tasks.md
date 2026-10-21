# Tareas de Implementación: Automatizar CI de AGENDA

## Dependencias de Pruebas (`requirements-dev.txt`)
- [ ] 1.1 Crear `requirements-dev.txt` con `-r requirements.txt`, pytest y httpx (verificar si ya existe; no recrear si está completo).
- [ ] 1.2 Verificar la instalación local con `pip install -r requirements-dev.txt` y ejecutar `pytest` en verde.

## Workflow de CI (`.github/workflows/ci-agenda.yml`)
- [ ] 2.1 Crear el workflow con eventos `pull_request` hacia `main`, `push` a `main` y `workflow_dispatch`.
- [ ] 2.2 Definir el job "Pruebas AGENDA" en `ubuntu-latest` con `timeout-minutes: 10` y permisos `contents: read`.
- [ ] 2.3 Añadir steps: `actions/checkout@v6`, `actions/setup-python@v6` con Python 3.11, instalación de `requirements-dev.txt`, ejecución de `pytest -q --junitxml=reports/junit.xml`.
- [ ] 2.4 Añadir step de conservación del informe con `actions/upload-artifact@v4`, `if: always()`, `if-no-files-found: warn` y retención de 7 días.

## Pruebas P8 (`tests/test_agenda.py`)
- [ ] 3.1 Revisar que la suite cubre el registro de una persona existente (`201` y posterior `200` con los datos persistidos).
- [ ] 3.2 Revisar que la suite cubre la consulta de una persona inexistente (`404`).
- [ ] 3.3 Revisar que la ejecución repetida de la suite es determinista (datos aislados por fixture SQLite temporal).
- [ ] 3.4 Completar únicamente los escenarios que falten, sin tocar el contrato de la API.

## Pull Request
- [ ] 4.1 Abrir PR desde `feature/p10-pipeline` hacia `main`, enlazando la Issue #10 y describiendo qué verifica el pipeline.

## Evidencias (`docs/p10-pipelines.md`)
- [ ] 5.1 Analizar la ejecución del pipeline: steps, resumen de pytest y artefacto generado.
- [ ] 5.2 Registrar evidencias en `docs/p10-pipelines.md`: URL de la ejecución, SHA, evento, duración, resultado, número de pruebas, informe JUnit y observaciones.

## Fallo Controlado
- [ ] 6.1 Añadir temporalmente `tests/test_pipeline_control.py` con un `assert False` y verificar el fallo local con pytest.
- [ ] 6.2 Hacer push, observar el check fallido de la PR y confirmar que el artefacto `junit.xml` conserva el detalle del fallo.
- [ ] 6.3 Retirar `tests/test_pipeline_control.py` y verificar que el pipeline vuelve a quedar en verde.

## Verificación de Calidad
- [ ] 7.1 Ejecutar la suite completa con `pytest` en verde.
- [ ] 7.2 Comprobar conformidad con `docs/architecture.md`: sin cambios en la aplicación (`app/` intacto, sin SQL fuera de `app/database.py`, sin dependencias nuevas de la app).
