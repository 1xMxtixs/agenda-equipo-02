"""
Capa de API REST de la aplicación Agenda con FastAPI.
Define endpoints POST y GET para la entidad Persona según HU-01 y HU-02.
No contiene sentencias SQL (se delegan a app/database.py).
"""

import os
import re
from contextlib import asynccontextmanager
from datetime import date
from typing import List, Optional
from fastapi import FastAPI, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field, field_validator

from app.database import init_db, insert_persona, get_all_personas


@asynccontextmanager
async def lifespan(app_instance: FastAPI):
    """Gestor de ciclo de vida para inicializar la base de datos."""
    init_db()
    yield


app = FastAPI(
    title="API Agenda - Equipo 02",
    description="API REST para el registro y consulta de personas en la Agenda",
    version="1.0.0",
    lifespan=lifespan,
)


class PersonaBase(BaseModel):
    nombre: str = Field(..., min_length=1, description="Nombre de la persona (obligatorio)")
    apellidos: str = Field(..., min_length=1, description="Apellidos de la persona (obligatorio)")
    fecha_nacimiento: Optional[str] = Field(None, description="Fecha de nacimiento en formato YYYY-MM-DD")
    correo_electronico: Optional[str] = Field(None, description="Correo electrónico válido")
    telefono: Optional[str] = Field(None, description="Teléfono de contacto")
    direccion: Optional[str] = Field(None, description="Dirección")
    categoria: Optional[str] = Field(None, description="Categoría del contacto")
    comentarios: Optional[str] = Field(None, description="Comentarios o notas adicionales")

    @field_validator("nombre", "apellidos")
    @classmethod
    def validate_not_blank(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("El campo no puede estar vacío ni contener solo espacios en blanco")
        return v.strip()

    @field_validator("correo_electronico")
    @classmethod
    def validate_email_format(cls, v: Optional[str]) -> Optional[str]:
        if v is None or v == "":
            return None
        v = v.strip()
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(pattern, v):
            raise ValueError("El correo electrónico no tiene un formato válido")
        return v

    @field_validator("fecha_nacimiento")
    @classmethod
    def validate_birth_date(cls, v: Optional[str]) -> Optional[str]:
        if v is None or v == "":
            return None
        v = v.strip()
        try:
            parsed_date = date.fromisoformat(v)
        except ValueError:
            raise ValueError("Formato de fecha inválido. Utilice YYYY-MM-DD")
        if parsed_date > date.today():
            raise ValueError("La fecha de nacimiento no puede ser una fecha futura")
        return v


class PersonaCreate(PersonaBase):
    pass


class PersonaResponse(PersonaBase):
    id: int


@app.post(
    "/api/personas",
    status_code=status.HTTP_201_CREATED,
    response_model=PersonaResponse,
    summary="Registrar una nueva persona (HU-01)",
    tags=["Personas"],
)
def create_persona(persona: PersonaCreate):
    """
    Registra una nueva persona en la base de datos persistente SQLite.
    Valida campos obligatorios, formato de correo y fecha de nacimiento.
    """
    try:
        created = insert_persona(persona.model_dump())
        if not created:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error al insertar la persona",
            )
        return created
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno al registrar la persona en la base de datos",
        )


@app.get(
    "/api/personas",
    status_code=status.HTTP_200_OK,
    response_model=List[PersonaResponse],
    summary="Listar todas las personas registradas (HU-02)",
    tags=["Personas"],
)
def list_personas():
    """
    Devuelve la lista de personas ordenadas alfabéticamente por apellidos y nombre.
    Retorna una lista vacía [] con HTTP 200 si la agenda no tiene registros.
    """
    try:
        personas = get_all_personas()
        return personas
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno al consultar el listado de personas",
        )


# Montaje de archivos estáticos para la interfaz web
current_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(current_dir, "static")

if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/", include_in_schema=False)
def get_root():
    """Sirve la interfaz web HTML principal o mensaje de inicio."""
    index_path = os.path.join(static_dir, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"mensaje": "API de Agenda disponible. Visite /docs para Swagger UI."}
