# Diseño Técnico: Automatizar CI de AGENDA

## 1. Flujo del Pipeline

El flujo previsto es el siguiente:

1. Cambio en una rama de característica.
2. Apertura de un Pull Request hacia `main`.
3. GitHub Actions combina temporalmente la rama con `main` (checkout de la combinación aún sin integrar) y ejecuta el job sobre ese estado.
4. `setup-python` instala Python 3.11 en el runner.
5. `pip install -r requirements-dev.txt` instala las dependencias de la aplicación y de prueba.
6. pytest se ejecuta con `--junitxml` para generar el informe en `reports/junit.xml`.
7. `upload-artifact` sube el informe como artefacto, siempre (`if: always()`), incluso si el step de pruebas falla.

En `push` a `main` y en `workflow_dispatch` el mismo job se ejecuta sobre el estado de `main` o bajo demanda, respectivamente.

## 2. Elementos del Workflow

- Fichero: `.github/workflows/ci-agenda.yml`.
- Eventos: `pull_request` hacia `main`, `push` a `main` y `workflow_dispatch`.
- Un único job con identificador `pruebas` y nombre visible "Pruebas AGENDA", en `ubuntu-latest` con `timeout-minutes: 10`.
- Steps secuenciales: descarga del repositorio, configuración de Python, instalación de dependencias, ejecución de pruebas y conservación del informe.
- Acciones utilizadas: `actions/checkout@v6`, `actions/setup-python@v6` y `actions/upload-artifact@v4`.
- Permisos: `contents: read` (principio de mínimo privilegio; el workflow solo necesita leer el repositorio).
- Artefacto `resultados-pruebas-agenda` con retención de 7 días.

## 3. Ejecución de las Pruebas con TestClient

Las pruebas utilizan `TestClient` de FastAPI y corren dentro del propio proceso de pytest; no hace falta levantar Uvicorn ni un servidor `--reload` en el runner. El aislamiento de datos se logra con una fixture que crea una base SQLite temporal por prueba, de modo que la suite es determinista en un runner limpio.

## 4. Ficheros involucrados

- `.github/workflows/ci-agenda.yml`: [NUEVO] Workflow de CI con los eventos y steps descritos.
- `requirements-dev.txt`: [YA CREADO] Verificar que existe con `-r requirements.txt`, pytest y httpx; no recrearlo.
- `docs/p10-pipelines.md`: [NUEVO] Registro de evidencias de las ejecuciones del pipeline.
- `.github/workflows/ci.yml`: NO se modifica en este cambio. El equipo decidirá su destino; se señala como observación que su nombre visible también es "CI AGENDA" y ambos workflows se dispararían ante una PR hacia `main`. Decisión pendiente, no resuelta aquí.

## 5. Cómo se probará el Cambio

- Ejecución local de pytest con las dependencias de `requirements-dev.txt` instaladas.
- Ejecución real del pipeline al abrir la PR hacia `main`.
- Ejercicio de fallo controlado: añadir temporalmente `tests/test_pipeline_control.py` con un `assert False`, observar que el check de la PR aparece fallido y que el informe `junit.xml` se conserva como artefacto; después retirar el test y verificar una nueva ejecución verde.

## 6. Conformidad Arquitectónica

El cambio no introduce SQL, no toca `app/main.py` ni `app/database.py`, ni añade dependencias de la aplicación. GitHub Actions es infraestructura de CI ya aprobada en `docs/architecture.md`; `pytest` y `httpx` ya están declarados en `requirements.txt`.
