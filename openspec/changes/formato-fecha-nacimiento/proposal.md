# Propuesta de Cambio: Formato Estricto Fecha de Nacimiento (YYYY-MM-DD)

## 1. Objetivo
Garantizar y forzar de manera estricta que el campo `fecha_nacimiento` de la entidad `Persona` cumpla con el estándar de formato `YYYY-MM-DD` (año de 4 dígitos, mes de 2 dígitos y día de 2 dígitos) tanto en la API como en la interfaz de usuario.

## 2. Alcance del Cambio
- **API Backend (`app/main.py`)**:
  - Validación con expresión regular estricta `^\d{4}-\d{2}-\d{2}$` combinada con parseo de fecha real (para evitar días inválidos como 2023-02-30).
  - Rechazo con código `422 Unprocessable Entity` ante formatos alternativos (ej: `DD/MM/YYYY`, `YYYY/MM/DD`, `DD-MM-YYYY`, meses/días de un solo dígito).
  - Mantenimiento de la regla de no admitir fechas futuras.
- **Interfaz Web (`app/static/index.html`)**:
  - Configuración del campo con `type="date"`, atributo `placeholder="YYYY-MM-DD"` y patrón de validación HTML5.
  - Formato estandarizado en la tabla de visualización de contactos (`YYYY-MM-DD`).
- **Pruebas Automatizadas (`tests/test_agenda.py`)**:
  - Nuevos casos de prueba automatizados verificando el formato exacto `YYYY-MM-DD` y rechazando formatos no conformes.

## 3. Fuera de Alcance
- Modificar el tipo de almacenamiento en SQLite (se mantiene como `TEXT` en formato ISO `YYYY-MM-DD`).
- Incorporar librerías externas adicionales de manejo de fechas (se utiliza `datetime` estándar de Python).

## 4. Impacto en la Arquitectura
El cambio no altera `docs/architecture.md` y respeta todas las restricciones de capas.
