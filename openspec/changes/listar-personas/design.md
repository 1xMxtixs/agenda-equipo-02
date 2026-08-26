# Diseño Técnico: HU-02 Listar Personas

## 1. Arquitectura y Participación de Capas

En conformidad estricta con `docs/architecture.md`:

- **Capa Interfaz (`app/static/index.html`)**:
  - Contiene un contenedor de tabla o tarjetas para listar los contactos.
  - Implementa la función JavaScript `cargarPersonas()` que invoca `fetch('GET', '/api/personas')`.
  - Si el arreglo devuelto está vacío (`[]`), renderiza un mensaje visible de agenda vacía.
  - Si hay datos, renderiza las filas ordenadas con ID, nombre, apellidos, teléfono y demás detalles.
  - Llama automáticamente a `cargarPersonas()` al cargar la página (`DOMContentLoaded`) y tras completar con éxito un registro.

- **Capa API (`app/main.py`)**:
  - Endpoint `@app.get("/api/personas", response_model=List[PersonaResponse])`.
  - Invoca la función `get_personas()` de `app/database.py`.
  - Captura excepciones generales y retorna `HTTP 500` con mensaje controlado si ocurre un fallo de base de datos.

- **Capa Persistencia y Base de Datos (`app/database.py`)**:
  - Implementa la función `get_all_personas() -> List[dict]` ejecutando:
    ```sql
    SELECT id, nombre, apellidos, fecha_nacimiento, correo_electronico, telefono, direccion, categoria, comentarios 
    FROM personas 
    ORDER BY apellidos COLLATE NOCASE ASC, nombre COLLATE NOCASE ASC;
    ```
  - Mapea las filas (`sqlite3.Row`) a diccionarios limpios.

## 2. Ficheros involucrados
- `app/database.py`: [MODIFICAR] Implementar `get_all_personas()`.
- `app/main.py`: [MODIFICAR] Implementar endpoint GET `/api/personas`.
- `app/static/index.html`: [MODIFICAR] Integrar tabla de listado, estado vacío y refresco reactivo.
- `tests/test_agenda.py`: [MODIFICAR] Añadir casos de prueba PL-01 a PL-06.

## 3. Estrategia de Pruebas
- Pruebas unitarias y de integración automáticas con `pytest`.
- Verificación de ordenamiento lexicográfico insensible a mayúsculas.
- Verificación de retorno de lista vacía en estado inicial.
