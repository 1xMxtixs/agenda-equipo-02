# Especificación: HU-02 Listar Personas

## Requisito
Como propietario de la agenda, quiero consultar una lista de las personas registradas para conocer las personas disponibles y acceder a su información básica.

---

## Escenarios de Comportamiento (Given / When / Then)

### Escenario 1 (PL-01 / PL-02): Listar personas registradas y verificar campos
- **Given** que existen personas registradas en la base de datos (por ejemplo, con nombre, apellidos, teléfono y fecha de nacimiento).
- **When** el propietario de la agenda envía una petición `GET /api/personas`.
- **Then** el sistema responde con código `HTTP 200 OK` y una lista de objetos JSON conteniendo los campos `id`, `nombre`, `apellidos`, `telefono`, `correo_electronico`, `direccion`, `categoria` y `comentarios`.

### Escenario 2 (PL-03): Comprobar orden por apellidos y nombre
- **Given** que en la base de datos existen tres personas:
  1. "Juan Pérez"
  2. "Ana Álvarez"
  3. "Beatriz Pérez"
- **When** se solicita `GET /api/personas`.
- **Then** el sistema devuelve las personas en el siguiente orden alfabético:
  1. "Ana Álvarez"
  2. "Beatriz Pérez"
  3. "Juan Pérez"

### Escenario 3 (PL-04): Listar una agenda vacía
- **Given** que la base de datos no contiene ningún registro de personas.
- **When** se envía una petición `GET /api/personas`.
- **Then** el sistema responde con código `HTTP 200 OK` y un cuerpo JSON con un arreglo vacío `[]`.
- **And** la interfaz web muestra un mensaje informativo indicando "No hay contactos registrados en la agenda".

### Escenario 4 (PL-05): Comprobar que una persona recién registrada aparece en el listado
- **Given** que se registra exitosamente una persona mediante `POST /api/personas`.
- **When** se invoca inmediatamente `GET /api/personas`.
- **Then** la lista devuelta contiene la persona recién registrada en su posición alfabética correspondiente.

### Escenario 5 (PL-06): Gestionar error de consulta a base de datos
- **Given** que ocurre un error inesperado al conectar o consultar la base de datos.
- **When** se solicita `GET /api/personas`.
- **Then** el sistema responde con código `HTTP 500 Internal Server Error`, mensaje de error controlado y sin volcar trazas internas al cliente.
