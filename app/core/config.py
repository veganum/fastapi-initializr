"""
Este módulo configura las variables de entorno y proporciona una instancia de configuración global.
"""

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Clase de configuración que utiliza Pydantic para cargar variables de entorno."""
    DATABASE_URL: str
    SECRET_KEY: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str = (
        "localhost"  # Agregar la variable POSTGRES_HOST con un valor por defecto
    )

    class Config:
        """Configuración adicional para la clase Settings."""
        env_file = ".env"  # Cargar las variables de entorno desde el archivo .env
        extra = "allow"  # Permitir entradas adicionales si las hay en el archivo .env

# Instancia de configuración global
settings = Settings()
