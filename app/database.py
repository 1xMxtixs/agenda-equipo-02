"""
Capa de Persistencia y Acceso a Datos SQLite.
Conforme a docs/architecture.md, todas las sentencias SQL se concentran en este archivo.
"""

import os
import sqlite3
import unicodedata
from typing import Any, Dict, List, Optional

DB_FILE = os.getenv("AGENDA_DB_PATH", "agenda.db")


def _normalize_for_sort(text: Optional[str]) -> str:
    """Normaliza texto eliminando acentos y convirtiendo a minúsculas para ordenación precisa."""
    if not text:
        return ""
    return "".join(
        c for c in unicodedata.normalize("NFD", text)
        if unicodedata.category(c) != "Mn"
    ).lower()


def _spanish_collation(str1: str, str2: str) -> int:
    """Función de colación personalizada para ordenación alfabética en español."""
    s1 = _normalize_for_sort(str1)
    s2 = _normalize_for_sort(str2)
    if s1 < s2:
        return -1
    if s1 > s2:
        return 1
    return 0


def get_connection(db_path: Optional[str] = None) -> sqlite3.Connection:
    """Obtiene una conexión a la base de datos SQLite con colación en español registrada."""
    path = db_path or os.getenv("AGENDA_DB_PATH", DB_FILE)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.create_collation("ES_NOCASE", _spanish_collation)
    return conn


def init_db(db_path: Optional[str] = None) -> None:
    """Inicializa la base de datos creando la tabla 'personas' si no existe."""
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """
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
        """
    )
    conn.commit()
    conn.close()


def insert_persona(data: Dict[str, Any], db_path: Optional[str] = None) -> Dict[str, Any]:
    """
    Inserta una nueva persona en SQLite de forma parametrizada.
    Retorna el diccionario con la entidad creada incluyendo su 'id'.
    """
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO personas (
            nombre, apellidos, fecha_nacimiento, correo_electronico,
            telefono, direccion, categoria, comentarios
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            data.get("nombre"),
            data.get("apellidos"),
            data.get("fecha_nacimiento"),
            data.get("correo_electronico"),
            data.get("telefono"),
            data.get("direccion"),
            data.get("categoria"),
            data.get("comentarios"),
        ),
    )
    conn.commit()
    created_id = cursor.lastrowid
    cursor.execute("SELECT * FROM personas WHERE id = ?", (created_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else {}


def get_all_personas(db_path: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Recupera todas las personas registradas ordenadas alfabéticamente
    por apellidos y, en caso de coincidencia, por nombre (insensible a acentos y mayúsculas).
    """
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT id, nombre, apellidos, fecha_nacimiento, correo_electronico,
               telefono, direccion, categoria, comentarios
        FROM personas
        ORDER BY apellidos COLLATE ES_NOCASE ASC, nombre COLLATE ES_NOCASE ASC
        """
    )
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]
