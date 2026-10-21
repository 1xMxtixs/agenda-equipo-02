# Especificación: Automatizar CI de AGENDA

## Requisito
Como equipo de desarrollo, queremos que GitHub Actions ejecute las pruebas de AGENDA automáticamente ante cada Pull Request y cada push a `main`, de modo que los problemas se detecten antes de integrar y quede constancia en forma de informe JUnit.

Nota: este cambio es una automatización de integración continua, no una historia de usuario del propietario de la agenda; el actor observador es el equipo de desarrollo.

---

## Escenarios de Comportamiento (Given / When / Then)

### Escenario 1: Pull Request hacia main ejecuta el job de pruebas
- **Given** que existe una rama de característica con cambios dirigida a un Pull Request hacia `main`.
- **When** GitHub Actions procesa el evento `pull_request` asociado a esa PR.
- **Then** el workflow CI AGENDA ejecuta el job "Pruebas AGENDA" y sus steps: descarga del repositorio, configuración de Python 3.11, instalación de dependencias, ejecución de pytest y conservación del informe.

### Escenario 2: Push a main re-verifica el código integrado
- **Given** que se ha integrado código en `main` mediante un merge o push directo.
- **When** GitHub Actions procesa el evento `push` sobre `main`.
- **Then** el workflow ejecuta el job "Pruebas AGENDA" completo sobre el código ya integrado, verificando que la rama principal permanece funcional.

### Escenario 3: Un fallo real de pytest produce un check fallido
- **Given** que la suite contiene una prueba que falla.
- **When** se ejecuta el job de pruebas en el runner.
- **Then** el step "Ejecutar pruebas" termina con error, el check de la PR aparece como fallido y el pipeline no oculta el error.

### Escenario 4: El informe JUnit se conserva también con fallos
- **Given** que pytest genera `reports/junit.xml` aunque la suite tenga fallos.
- **When** termina la ejecución del job.
- **Then** el step "Conservar informe" sube el artefacto `resultados-pruebas-agenda` gracias a `if: always()`; si la instalación falla y no hay informe, se emite una advertencia (`if-no-files-found: warn`) y el job sigue en estado fallido.

### Escenario 5: Ejecución manual bajo demanda
- **Given** que el equipo necesita lanzar el pipeline sin una PR ni un push (por ejemplo, para re-validar `main`).
- **When** un miembro del equipo dispara el evento `workflow_dispatch` desde la interfaz de GitHub Actions.
- **Then** el job "Pruebas AGENDA" se ejecuta igual que en los eventos automáticos y produce el mismo informe JUnit como artefacto.

### Escenario 6: Las pruebas se ejecutan con datos aislados
- **Given** que cada prueba utiliza una base SQLite temporal mediante una fixture, sin depender de una base de datos personal ni del orden de ejecución.
- **When** la suite completa corre en el runner limpio de GitHub Actions.
- **Then** el resultado es determinista y reproducible, independiente del estado previo del runner.

### Escenario 7: Las dependencias declaradas bastan para ejecutar AGENDA
- **Given** que el runner instala `requirements-dev.txt`, que incluye `requirements.txt` más pytest y httpx.
- **When** el step de instalación completa sin errores y las pruebas se ejecutan.
- **Then** el éxito del job demuestra que las dependencias declaradas son suficientes para ejecutar AGENDA en una máquina limpia.
