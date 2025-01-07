"""
Este módulo define el modelo de usuario para la base de datos.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from app.core.database import Base

class UserModel(Base):
    """Modelo de usuario para la base de datos."""
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)  # Aquí agregamos autoincrement=True
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    direccion = Column(String, nullable=True)
    telefono = Column(Integer, nullable=False)
    creacion_user = Column(DateTime, default=datetime.utcnow)
