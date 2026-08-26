# Tareas de Implementación: HU-02 Listar Personas

## Persistencia y Acceso a Datos (`app/database.py`)
- [x] 1.1 Implementar función `get_all_personas() -> list[dict]` en `app/database.py`.
- [x] 1.2 Aplicar ordenamiento SQL determinista `ORDER BY apellidos COLLATE ES_NOCASE ASC, nombre COLLATE ES_NOCASE ASC`.

## API y Endpoints (`app/main.py`)
- [x] 2.1 Implementar endpoint `GET /api/personas` con retorno `HTTP 200 OK` y modelo `List[PersonaResponse]`.
- [x] 2.2 Proteger endpoint con captura de excepciones para manejo controlado de errores `HTTP 500`.

## Interfaz de Usuario (`app/static/index.html`)
- [x] 3.1 Agregar sección de visualización de listado (tabla/tarjetas) en el HTML.
- [x] 3.2 Implementar función JS `cargarPersonas()` para consultar `GET /api/personas`.
- [x] 3.3 Mostrar estado informativo cuando la agenda esté vacía (`[]`).
- [x] 3.4 Conectar refresco automático del listado al enviar exitosamente el formulario de registro.

## Pruebas Automatizadas (`tests/test_agenda.py`)
- [x] 4.1 Implementar test **PL-01**: Listar varias personas.
- [x] 4.2 Implementar test **PL-02**: Comprobar los campos devueltos en el listado.
- [x] 4.3 Implementar test **PL-03**: Comprobar orden alfabético por apellidos y nombre.
- [x] 4.4 Implementar test **PL-04**: Listar agenda vacía (`HTTP 200` y `[]`).
- [x] 4.5 Implementar test **PL-05**: Comprobar que una persona registrada aparece en el listado.
- [x] 4.6 Implementar test **PL-06**: Gestionar y comprobar error de base de datos (`HTTP 500`).

## Verificación de Calidad
- [x] 5.1 Ejecutar suite completa con `pytest --cov=app`.
- [x] 5.2 Comprobar conformidad con `docs/architecture.md`.
