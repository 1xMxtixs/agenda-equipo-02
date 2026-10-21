# P10 – Evidencias de la ejecución del pipeline

## Ejecución 1 – Pipeline verde (paso 4.9)

- **Enlace de la ejecución:** https://github.com/1xMxtixs/agenda-equipo-02/actions/runs/39624364261
- **Commit comprobado:** `31c948406ec656b5a8ee4b5cbc714125425147f1` (`31c9484`)
- **Evento:** `pull_request` (PR #12 hacia `main`)
- **Duración:** 28 s (15:18:03Z → 15:18:31Z)
- **Resultado:** `success` (correcto)
- **Pruebas:** 12 pasaron, 0 fallaron, 0 errores — `12 passed, 1 warning in 0.41s`
- **Informe:** artefacto `resultados-pruebas-agenda` descargable (582 bytes, `reports/junit.xml`, subido con `if: always()`)
- **Observaciones:**
  - El job **Pruebas AGENDA** completó los 5 pasos definidos (Descargar el repositorio, Configurar Python 3.11, Instalar dependencias, Ejecutar pruebas, Conservar informe) sin incidencias.
  - El workflow antiguo `.github/workflows/ci.yml` (job `test`) también se ejecutó en el mismo evento con el mismo nombre "CI AGENDA"; ambas ejecuciones terminaron en `success`. La duplicidad de nombre está señalada en `openspec/changes/automatizar-ci-agenda/design.md` como decisión pendiente.
  - 1 warning de pytest (deprecaciones de la suite existente), sin impacto en el resultado.
