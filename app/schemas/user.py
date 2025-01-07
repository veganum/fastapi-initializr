"""
Este módulo define los esquemas de Pydantic para el modelo de usuario.
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    """Esquema base para el modelo de usuario."""
    nombre: str
    apellido: str
    direccion: Optional[str] = None
    telefono: int

class UserCreate(UserBase):
    """Esquema para la creación de un nuevo usuario."""
    # No incluir el campo 'id'

class UserResponse(UserBase):
    """Esquema para la respuesta del modelo de usuario."""
    id: int
    creacion_user: datetime

    class Config:
        """Configuración adicional para el esquema de respuesta."""
        from_attributes = True
