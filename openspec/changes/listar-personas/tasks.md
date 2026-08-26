# Tareas de Implementación: HU-02 Listar Personas

## Persistencia y Acceso a Datos (`app/database.py`)
- [ ] 1.1 Implementar función `get_all_personas() -> list[dict]` en `app/database.py`.
- [ ] 1.2 Aplicar ordenamiento SQL determinista `ORDER BY apellidos COLLATE NOCASE ASC, nombre COLLATE NOCASE ASC`.

## API y Endpoints (`app/main.py`)
- [ ] 2.1 Implementar endpoint `GET /api/personas` con retorno `HTTP 200 OK` y modelo `List[PersonaResponse]`.
- [ ] 2.2 Proteger endpoint con captura de excepciones para manejo controlado de errores `HTTP 500`.

## Interfaz de Usuario (`app/static/index.html`)
- [ ] 3.1 Agregar sección de visualización de listado (tabla/tarjetas) en el HTML.
- [ ] 3.2 Implementar función JS `cargarPersonas()` para consultar `GET /api/personas`.
- [ ] 3.3 Mostrar estado informativo cuando la agenda esté vacía (`[]`).
- [ ] 3.4 Conectar refresco automático del listado al enviar exitosamente el formulario de registro.

## Pruebas Automatizadas (`tests/test_agenda.py`)
- [ ] 4.1 Implementar test **PL-01**: Listar varias personas.
- [ ] 4.2 Implementar test **PL-02**: Comprobar los campos devueltos en el listado.
- [ ] 4.3 Implementar test **PL-03**: Comprobar orden alfabético por apellidos y nombre.
- [ ] 4.4 Implementar test **PL-04**: Listar agenda vacía (`HTTP 200` y `[]`).
- [ ] 4.5 Implementar test **PL-05**: Comprobar que una persona registrada aparece en el listado.
- [ ] 4.6 Implementar test **PL-06**: Gestionar y comprobar error de base de datos (`HTTP 500`).

## Verificación de Calidad
- [ ] 5.1 Ejecutar suite completa con `pytest --cov=app`.
- [ ] 5.2 Comprobar conformidad con `docs/architecture.md`.
