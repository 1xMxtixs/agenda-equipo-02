# Diseño Técnico: Formato Estricto Fecha de Nacimiento (YYYY-MM-DD)

## 1. Arquitectura y Participación de Capas

- **API y Validación (`app/main.py`)**:
  - En el modelo Pydantic `PersonaBase`, el validador `@field_validator("fecha_nacimiento")` se refuerza con:
    1. Expresión regular obligatoria: `^(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$`.
    2. Conversión estricta mediante `datetime.strptime(v, "%Y-%m-%d").date()`.
    3. Verificación de no futuridad (`parsed_date <= date.today()`).
  - Devolver mensajes descriptivos en español ante violaciones de validación.

- **Interfaz de Usuario (`app/static/index.html`)**:
  - Elemento `<input>` de fecha configurado con:
    - `type="date"`
    - `pattern="\d{4}-\d{2}-\d{2}"`
    - `placeholder="YYYY-MM-DD"`
  - Ayuda contextual en el formulario indicando el formato `(AAAA-MM-DD)`.

- **Persistencia (`app/database.py`)**:
  - Sin modificaciones requeridas; las fechas se persisten directamente como cadenas `TEXT` normalizadas `YYYY-MM-DD` en SQLite.

## 2. Ficheros Involucrados
- `app/main.py`: [MODIFICAR] Reforzar validador de fecha de nacimiento.
- `app/static/index.html`: [MODIFICAR] Añadir ayuda visual y pattern HTML5 en el campo de fecha.
- `tests/test_agenda.py`: [MODIFICAR] Añadir pruebas específicas de validación de formato `YYYY-MM-DD`.

## 3. Estrategia de Pruebas
- Pruebas unitarias de validación con `pytest`:
  - Formato válido `YYYY-MM-DD` (ej: 1995-08-26).
  - Formatos no permitidos: `26/08/1995`, `1995/08/26`, `1995-8-5`, `1995-02-30`.
