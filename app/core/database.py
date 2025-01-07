"""
Este módulo configura la conexión a la base de datos y
proporciona un generador de sesiones para FastAPI.
"""

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings  # Usar configuración centralizada

# Configuración del motor de base de datos
DATABASE_URL = settings.DATABASE_URL
engine = create_async_engine(DATABASE_URL, echo=True)

# Creación de sesiones
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)

# Base declarativa para los modelos
Base = declarative_base()

# Generador de sesiones para FastAPI
async def get_db():
    """Genera una sesión de base de datos asincrónica para FastAPI."""
    async with SessionLocal() as session:
        yield session
