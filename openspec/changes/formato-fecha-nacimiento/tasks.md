# Tareas de Implementación: Formato Estricto Fecha de Nacimiento

## Validación Backend (`app/main.py`)
- [x] 1.1 Reforzar el validador `@field_validator("fecha_nacimiento")` con regex estricto `^\d{4}-\d{2}-\d{2}$` y parseo con `strptime`.
- [x] 1.2 Mantener regla de rechazo de fechas de nacimiento futuras.

## Interfaz de Usuario (`app/static/index.html`)
- [x] 2.1 Actualizar el campo de fecha en el HTML con `placeholder="YYYY-MM-DD"`, `pattern` y texto de ayuda.

## Pruebas Automatizadas (`tests/test_agenda.py`)
- [x] 3.1 Añadir prueba para validar fechas válidas `YYYY-MM-DD`.
- [x] 3.2 Añadir pruebas para rechazar formatos `DD/MM/YYYY`, `YYYY/MM/DD`, `YYYY-M-D` y fechas calendario inexistentes como `2023-02-30`.

## Verificación y Calidad
- [x] 4.1 Ejecutar suite completa `pytest` y confirmar que todos los tests pasen (11/11 pasados, 91% cobertura).
