# Especificación: Formato Estricto Fecha de Nacimiento (YYYY-MM-DD)

## Requisito
Como propietario de la agenda, quiero que las fechas de nacimiento se ingresen y almacenen estrictamente en formato `YYYY-MM-DD` para asegurar la consistencia y ordenación temporal de los datos.

---

## Escenarios de Comportamiento (Given / When / Then)

### Escenario 1: Fecha de nacimiento válida en formato YYYY-MM-DD
- **Given** que el propietario de la agenda ingresa una fecha en formato ISO `YYYY-MM-DD` (ejemplo: `"1995-08-26"`).
- **When** se envía la petición `POST /api/personas`.
- **Then** el sistema valida la fecha exitosamente, responde con código `201 Created` y almacena la fecha exactamente como `"1995-08-26"`.

### Escenario 2: Rechazo por formato con barras (DD/MM/YYYY o YYYY/MM/DD)
- **Given** que el propietario de la agenda ingresa una fecha con formato `"26/08/1995"` o `"1995/08/26"`.
- **When** se envía la petición `POST /api/personas`.
- **Then** el sistema rechaza la petición con código `422 Unprocessable Entity` indicando que el formato debe ser estrictamente `YYYY-MM-DD`.

### Escenario 3: Rechazo por dígitos incompletos (YYYY-M-D)
- **Given** que se ingresa una fecha con meses o días de un solo dígito como `"1995-8-5"`.
- **When** se envía la petición `POST /api/personas`.
- **Then** el sistema responde con código `422 Unprocessable Entity` exigiendo ceros a la izquierda para meses y días (`1995-08-05`).

### Escenario 4: Rechazo por día o mes inexistente en el calendario
- **Given** que se ingresa una fecha estructuralmente similar a YYYY-MM-DD pero con días inexistentes (ejemplo: `"2023-02-30"` o `"1990-13-01"`).
- **When** se envía la petición `POST /api/personas`.
- **Then** el sistema responde con código `422 Unprocessable Entity` con mensaje de error de fecha calendario inválida.

### Escenario 5: Campo de fecha opcional
- **Given** que el campo `fecha_nacimiento` se omite, se envía como `null` o como cadena vacía `""`.
- **When** se envía la petición `POST /api/personas`.
- **Then** el sistema permite el registro exitoso respondiendo `201 Created` y guardando el valor como `null`.
