# Propuesta de Cambio: Automatizar CI de AGENDA

## 1. Objetivo
Ejecutar automáticamente las pruebas de AGENDA en un runner de GitHub ante cada Pull Request hacia `main` y cada push a `main`, conservando el informe JUnit como artefacto de la ejecución, para detectar problemas de regresión antes de integrar.

## 2. Alcance del Cambio
- Creación del workflow `.github/workflows/ci-agenda.yml` con los eventos `pull_request` hacia `main`, `push` a `main` y `workflow_dispatch`.
- Dependencias de pruebas declaradas en `requirements-dev.txt` (instaladas por el runner).
- Generación del informe JUnit en `reports/junit.xml` y subida como artefacto de GitHub Actions también cuando pytest falla (mediante `if: always()`).
- Registro de evidencias de la ejecución del pipeline en `docs/p10-pipelines.md`.

## 3. Fuera de Alcance
- Despliegue continuo a producción.
- Autenticación y autorización.
- Modificación o eliminación de personas.
- Cambios en el contrato de la API (`POST /api/personas`, `GET /api/personas`).
- Incorporación de frameworks adicionales.
- Fijado de versiones exacto (`==`) de las dependencias (mejora futura).

## 4. Impacto en la Arquitectura
El cambio no altera `docs/architecture.md`. La aplicación FastAPI, el acceso a datos SQLite y la interfaz web quedan intactos; se trata de una automatización de integración continua, contemplada en las tecnologías aprobadas del documento de arquitectura. En cuanto a configuración, `openspec/config.yaml` fija Python 3.11 o superior y el workflow utiliza la versión 3.11.
