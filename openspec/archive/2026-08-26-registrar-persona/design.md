# Diseño Técnico: HU-01 Registrar Persona

## 1. Arquitectura y Participación de Capas

En conformidad estricta con `docs/architecture.md`:

- **Capa Interfaz (`app/static/index.html`)**:
  - Contiene un formulario con validaciones básicas en cliente (`required` para nombre y apellidos, `type="email"`, `type="date"`).
  - Escucha el evento `submit`, serializa los campos a JSON y realiza una petición `fetch('POST', '/api/personas')`.
  - Muestra alertas o mensajes de éxito/error según la respuesta HTTP.

- **Capa API y Validaciones (`app/main.py`)**:
  - Define modelos Pydantic: `PersonaCreate` y `PersonaResponse`.
  - Aplica validadores de Pydantic (`@field_validator`) para verificar que el email tenga estructura válida y que la fecha de nacimiento no sea futura.
  - Endpoint `@app.post("/api/personas", status_code=status.HTTP_201_CREATED, response_model=PersonaResponse)`.
  - Invoca a la función de inserción en `app/database.py` y devuelve la entidad creada.
  - Manejo de excepciones para responder con errores HTTP limpios sin trazas internas.

- **Capa Persistencia y Base de Datos (`app/database.py`)**:
  - Inicializa la base de datos SQLite creando la tabla `personas` si no existe:
    ```sql
    CREATE TABLE IF NOT EXISTS personas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellidos TEXT NOT NULL,
        fecha_nacimiento TEXT,
        correo_electronico TEXT,
        telefono TEXT,
        direccion TEXT,
        categoria TEXT,
        comentarios TEXT
    );
    ```
  - Función `insert_persona(persona: dict) -> dict` que ejecuta consultas parametrizadas con `sqlite3`.

## 2. Ficheros involucrados
- `app/database.py`: [NUEVO] Inicialización de SQLite y consultas parametrizadas.
- `app/main.py`: [NUEVO] Aplicación FastAPI, esquemas Pydantic y endpoint POST.
- `app/static/index.html`: [NUEVO] Formulario de registro e interactividad JS.
- `tests/test_agenda.py`: [NUEVO] Casos de prueba automatizados con `pytest` y `TestClient` de FastAPI.

## 3. Estrategia de Pruebas
- Pruebas automatizadas con `pytest` utilizando SQLite en memoria o BD de pruebas para aislamiento.
- Verificación de escenarios PR-01, PR-02, PR-03, PR-04.
