# Propuesta de Cambio: HU-01 Registrar Persona

## 1. Objetivo
Permitir al propietario de la agenda registrar nuevas personas con su información básica y de contacto (nombre, apellidos, fecha de nacimiento, correo electrónico, teléfono, dirección, categoría y comentarios), persistiendo los datos de manera confiable en SQLite.

## 2. Alcance del Cambio
- Creación de la tabla `personas` en SQLite con identificador único autonumérico/entero.
- Exposición del endpoint `POST /api/personas`.
- Validación de datos:
  - `nombre` y `apellidos` obligatorios.
  - `correo_electronico` opcional; si se proporciona, debe cumplir con formato de email válido.
  - `fecha_nacimiento` opcional; no puede ser una fecha futura.
  - `telefono`, `direccion`, `categoria` y `comentarios` opcionales.
- Formulario de captura en la interfaz web (`app/static/index.html`).
- Manejo de respuestas HTTP coherentes:
  - `201 Created` en caso de éxito con el registro creado.
  - `422 Unprocessable Entity` o `400 Bad Request` en caso de datos inválidos.
- Pruebas automatizadas unitarias y de integración (PR-01 a PR-04).

## 3. Fuera de Alcance
- Modificación o eliminación de personas.
- Búsquedas y filtros avanzados.
- Paginación.
- Autenticación o roles de usuario.

## 4. Impacto en la Arquitectura
El cambio no altera `docs/architecture.md`. Sigue rigurosamente la separación de responsabilidades:
- SQL confinado exclusivamente a `app/database.py`.
- Lógica de endpoints y validaciones en `app/main.py`.
- Interfaz HTML/JS consumiendo la API sin acceso directo a la base de datos.
