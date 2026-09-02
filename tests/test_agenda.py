"""
Suite de pruebas automatizadas para la aplicación Agenda.
Cubre los escenarios PR-01 a PR-04 (Registro), PL-01 a PL-06 (Listado)
y validación estricta de formato de fecha YYYY-MM-DD según OpenSpec.
"""

from unittest.mock import patch
import pytest
from fastapi.testclient import TestClient

from app.database import init_db
from app.main import app


@pytest.fixture(autouse=True)
def setup_test_db(tmp_path, monkeypatch):
    """Crea y configura una base de datos SQLite aislada para cada test."""
    test_db = str(tmp_path / "test_agenda.db")
    monkeypatch.setenv("AGENDA_DB_PATH", test_db)
    init_db(test_db)
    yield test_db


@pytest.fixture
def client():
    """Cliente de pruebas de FastAPI."""
    return TestClient(app)


# ==============================================================================
# Pruebas de Registro (HU-01)
# ==============================================================================

def test_pr01_registrar_persona_con_datos_validos(client):
    """PR-01: Registrar una persona con datos válidos (incluye fecha YYYY-MM-DD)."""
    payload = {
        "nombre": "Carlos",
        "apellidos": "Pérez Gómez",
        "fecha_nacimiento": "1990-05-15",
        "correo_electronico": "carlos.perez@example.com",
        "telefono": "+56912345678",
        "direccion": "Av. Central 123",
        "categoria": "Trabajo",
        "comentarios": "Contacto laboral",
    }
    response = client.post("/api/personas", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] is not None
    assert data["nombre"] == "Carlos"
    assert data["apellidos"] == "Pérez Gómez"
    assert data["fecha_nacimiento"] == "1990-05-15"
    assert data["correo_electronico"] == "carlos.perez@example.com"
    assert data["telefono"] == "+56912345678"


def test_pr02_rechazar_registro_sin_nombre_o_apellidos(client):
    """PR-02: Rechazar un registro sin nombre o apellidos."""
    # Sin nombre
    res_no_name = client.post("/api/personas", json={"nombre": "", "apellidos": "Gómez"})
    assert res_no_name.status_code == 422

    # Sin apellidos
    res_no_surname = client.post("/api/personas", json={"nombre": "Carlos", "apellidos": "   "})
    assert res_no_surname.status_code == 422

    # Objeto vacío
    res_empty = client.post("/api/personas", json={})
    assert res_empty.status_code == 422


def test_pr03_rechazar_correo_con_formato_invalido(client):
    """PR-03: Rechazar un correo con formato inválido."""
    payload = {
        "nombre": "Carlos",
        "apellidos": "Pérez",
        "correo_electronico": "correo_no_valido_sin_arroba",
    }
    response = client.post("/api/personas", json=payload)
    assert response.status_code == 422


def test_pr04_rechazar_fecha_nacimiento_futura(client):
    """PR-04: Rechazar una fecha de nacimiento futura."""
    payload = {
        "nombre": "Carlos",
        "apellidos": "Pérez",
        "fecha_nacimiento": "2099-12-31",
    }
    response = client.post("/api/personas", json=payload)
    assert response.status_code == 422


def test_fecha_nacimiento_formatos_invalidos(client):
    """Verifica que el formato YYYY-MM-DD sea exigido estrictamente rechazando formatos inválidos."""
    # Formato con barras DD/MM/YYYY
    res_slash = client.post("/api/personas", json={"nombre": "A", "apellidos": "B", "fecha_nacimiento": "15/05/1990"})
    assert res_slash.status_code == 422
    assert "YYYY-MM-DD" in str(res_slash.json())

    # Formato con barras YYYY/MM/DD
    res_slash_iso = client.post("/api/personas", json={"nombre": "A", "apellidos": "B", "fecha_nacimiento": "1990/05/15"})
    assert res_slash_iso.status_code == 422

    # Formato con mes/día de un dígito YYYY-M-D
    res_single_digit = client.post("/api/personas", json={"nombre": "A", "apellidos": "B", "fecha_nacimiento": "1990-5-5"})
    assert res_single_digit.status_code == 422

    # Fecha calendario inexistente (30 de febrero)
    res_invalid_cal = client.post("/api/personas", json={"nombre": "A", "apellidos": "B", "fecha_nacimiento": "2023-02-30"})
    assert res_invalid_cal.status_code == 422


# ==============================================================================
# Pruebas de Listado (HU-02)
# ==============================================================================

def test_pl01_listar_varias_personas(client):
    """PL-01: Listar varias personas."""
    client.post("/api/personas", json={"nombre": "Ana", "apellidos": "Álvarez"})
    client.post("/api/personas", json={"nombre": "Bernardo", "apellidos": "Barros"})

    response = client.get("/api/personas")
    assert response.status_code == 200
    personas = response.json()
    assert len(personas) == 2


def test_pl02_comprobar_campos_del_listado(client):
    """PL-02: Comprobar los campos del listado."""
    payload = {
        "nombre": "David",
        "apellidos": "Cortez",
        "fecha_nacimiento": "1995-10-20",
        "correo_electronico": "david@example.com",
        "telefono": "987654321",
        "direccion": "Calle 1",
        "categoria": "Universidad",
        "comentarios": "Compañero de equipo",
    }
    client.post("/api/personas", json=payload)

    response = client.get("/api/personas")
    assert response.status_code == 200
    personas = response.json()
    assert len(personas) == 1
    data = personas[0]
    for key, value in payload.items():
        assert data[key] == value
    assert "id" in data


def test_pl03_comprobar_orden_por_apellidos_y_nombre(client):
    """PL-03: Comprobar el orden por apellidos y nombre."""
    client.post("/api/personas", json={"nombre": "Juan", "apellidos": "Pérez"})
    client.post("/api/personas", json={"nombre": "Ana", "apellidos": "Álvarez"})
    client.post("/api/personas", json={"nombre": "Beatriz", "apellidos": "Pérez"})

    response = client.get("/api/personas")
    assert response.status_code == 200
    personas = response.json()

    nombres_ordenados = [(p["apellidos"], p["nombre"]) for p in personas]
    assert nombres_ordenados == [
        ("Álvarez", "Ana"),
        ("Pérez", "Beatriz"),
        ("Pérez", "Juan"),
    ]


def test_pl04_listar_agenda_vacia(client):
    """PL-04: Listar una agenda vacía: HTTP 200 y []."""
    response = client.get("/api/personas")
    assert response.status_code == 200
    assert response.json() == []


def test_pl05_persona_registrada_aparece_en_listado(client):
    """PL-05: Comprobar que una persona registrada aparece en el listado."""
    res_post = client.post("/api/personas", json={"nombre": "Matias", "apellidos": "Santos"})
    assert res_post.status_code == 201
    created_id = res_post.json()["id"]

    res_get = client.get("/api/personas")
    assert res_get.status_code == 200
    ids = [p["id"] for p in res_get.json()]
    assert created_id in ids


def test_pl06_gestionar_error_de_consulta(client):
    """PL-06: Gestionar un error de consulta de forma controlada (HTTP 500 sin trazas)."""
    with patch("app.main.get_all_personas", side_effect=Exception("Database failure")):
        response = client.get("/api/personas")
        assert response.status_code == 500
        assert "Error interno al consultar el listado de personas" in response.json()["detail"]
