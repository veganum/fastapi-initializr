"""
Este módulo configura la sesión de la base de datos para FastAPI.
"""

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore
from app.core.config import settings

# Configuración del motor de base de datos
engine = create_async_engine(settings.DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
