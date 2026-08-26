# Propuesta de Cambio: HU-02 Listar Personas

## 1. Objetivo
Permitir al propietario de la agenda consultar la lista completa de todas las personas registradas, presentadas de forma clara y ordenadas alfabéticamente por apellidos y, en caso de coincidencia, por nombre.

## 2. Alcance del Cambio
- Exposición del endpoint `GET /api/personas`.
- Recuperación de todas las personas registradas desde SQLite mediante `app/database.py`.
- Ordenación determinista en base de datos: `ORDER BY apellidos COLLATE NOCASE ASC, nombre COLLATE NOCASE ASC`.
- Manejo de agenda vacía:
  - La API responde `HTTP 200 OK` con un arreglo vacío `[]`.
  - La interfaz web muestra un mensaje informativo claro indicando que no hay personas registradas.
- Visualización de tabla/tarjetas de contactos en la interfaz web (`app/static/index.html`).
- Refresco automático del listado tras un registro exitoso.
- Manejo controlado de errores de consulta `HTTP 500` sin exponer detalles técnicos internos.
- Pruebas automatizadas de listado (PL-01 a PL-06).

## 3. Fuera de Alcance
- Paginación.
- Búsqueda por texto o filtros por categoría.
- Modificación o eliminación de registros.
- Autenticación y permisos.

## 4. Impacto en la Arquitectura
Cumple plenamente con `docs/architecture.md`. Mantiene la separación estricta:
- Consultas SQL `SELECT` únicamente en `app/database.py`.
- La interfaz no accede a SQLite ni contiene lógica de ordenación o negocio.
