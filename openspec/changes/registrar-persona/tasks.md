# Tareas de Implementación: HU-01 Registrar Persona

## Persistencia y Acceso a Datos (`app/database.py`)
- [ ] 1.1 Crear módulo `app/database.py` con conexión a SQLite (`agenda.db`).
- [ ] 1.2 Implementar función `init_db()` para crear la tabla `personas` con los tipos adecuados.
- [ ] 1.3 Implementar función `insert_persona(data: dict) -> dict` con SQL parametrizado.

## API y Validaciones (`app/main.py`)
- [ ] 2.1 Crear instancia de `FastAPI` y montar archivos estáticos en `/static`.
- [ ] 2.2 Definir esquemas Pydantic `PersonaCreate` y `PersonaResponse` con validaciones (nombre no vacío, fecha no futura, email válido).
- [ ] 2.3 Implementar endpoint `POST /api/personas` con retorno `HTTP 201 Created`.
- [ ] 2.4 Controlar errores y excepciones HTTP.

## Interfaz de Usuario (`app/static/index.html`)
- [ ] 3.1 Diseñar formulario de registro con los campos requeridos y opcionales.
- [ ] 3.2 Implementar JavaScript para interceptar el formulario y enviar la petición `POST /api/personas`.
- [ ] 3.3 Mostrar mensajes de éxito y error en la interfaz.

## Pruebas Automatizadas (`tests/test_agenda.py`)
- [ ] 4.1 Configurar entorno de pruebas con `TestClient` de FastAPI.
- [ ] 4.2 Implementar test **PR-01**: Registro con datos válidos (`HTTP 201`).
- [ ] 4.3 Implementar test **PR-02**: Rechazo por falta de nombre o apellidos (`HTTP 422`).
- [ ] 4.4 Implementar test **PR-03**: Rechazo por formato de correo inválido (`HTTP 422`).
- [ ] 4.5 Implementar test **PR-04**: Rechazo por fecha de nacimiento futura (`HTTP 422`).

## Verificación de Calidad
- [ ] 5.1 Ejecutar suite completa con `pytest`.
- [ ] 5.2 Comprobar conformidad arquitectónica estricta con `docs/architecture.md`.
