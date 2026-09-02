# Especificación: HU-01 Registrar Persona

## Requisito
Como propietario de la agenda, quiero registrar nuevas personas dentro de la agenda para mantener su información de contacto guardada de forma persistente.

---

## Escenarios de Comportamiento (Given / When / Then)

### Escenario 1 (PR-01): Registrar una persona con datos válidos
- **Given** que el propietario de la agenda proporciona los datos de una nueva persona con nombre "Carlos", apellidos "Pérez Gómez", correo "carlos.perez@example.com", fecha de nacimiento "1990-05-15", teléfono "+56912345678", dirección "Av. Central 123", categoría "Trabajo" y comentarios "Contacto laboral".
- **When** se envía una petición `POST /api/personas` con estos datos.
- **Then** el sistema responde con código `201 Created`, un objeto JSON que incluye el identificador único `id` asignado y los datos guardados en SQLite.

### Escenario 2 (PR-02): Rechazar registro sin nombre o sin apellidos
- **Given** que el propietario de la agenda envía una petición sin el campo obligatorio `nombre` o sin `apellidos` (o con cadenas vacías / solo espacios).
- **When** se envía la petición `POST /api/personas`.
- **Then** el sistema rechaza la solicitud devolviendo código `422 Unprocessable Entity`, detalla el error de validación y no crea ningún registro en la base de datos.

### Escenario 3 (PR-03): Rechazar un correo con formato inválido
- **Given** que se proporcionan nombre y apellidos válidos pero el campo `correo_electronico` tiene un valor inválido como "correo-no-valido".
- **When** se envía la petición `POST /api/personas`.
- **Then** el sistema responde con código `422 Unprocessable Entity` indicando formato de correo electrónico incorrecto y no persiste el registro.

### Escenario 4 (PR-04): Rechazar una fecha de nacimiento futura
- **Given** que se proporciona una `fecha_nacimiento` posterior a la fecha actual del sistema (por ejemplo, fecha en el año 2099).
- **When** se envía la petición `POST /api/personas`.
- **Then** el sistema responde con código `422 Unprocessable Entity` indicando que la fecha de nacimiento no puede ser futura y rechaza la inserción.

### Escenario 5: Registro exitoso solo con campos obligatorios
- **Given** que el propietario de la agenda solo ingresa `nombre` ("María") y `apellidos` ("López"), dejando opcionales en blanco o nulos.
- **When** se envía la petición `POST /api/personas`.
- **Then** el sistema responde con código `201 Created` y persiste a la persona correctamente con los campos opcionales nulos/vacíos.
