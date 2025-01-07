"""
Este módulo configura y ejecuta la aplicación FastAPI.
"""

import asyncio
import os
from fastapi import FastAPI
import sqlalchemy
from sqlalchemy.ext.asyncio import create_async_engine
from app.api.v1.endpoints import user
from app.core.database import Base

# Detecta si la aplicación se ejecuta localmente o dentro de Docker
db_host = os.getenv("POSTGRES_HOST", "localhost")
db_url = os.getenv(
    "DATABASE_URL", f"postgresql+asyncpg://postgres:password@{db_host}:5432/mydatabase"
)

# Crear el motor de la base de datos
engine = create_async_engine(db_url)

app = FastAPI()

# Registrar las rutas
app.include_router(user.router, prefix="/api/v1")


# Función para esperar la conexión a la base de datos
async def wait_for_db_connection():
    """
    Espera a que la conexión a la base de datos se establezca,
    reintentando varias veces si es necesario.
    """
    retries = 5  # Número de reintentos
    for attempt in range(retries):
        try:
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
            print("✅ Conexión con la base de datos establecida.")
            break
        except (asyncio.TimeoutError, sqlalchemy.exc.OperationalError) as e:
            print(f"⚠️ Intento {attempt + 1} fallido: {e}")
            await asyncio.sleep(5)  # Esperar 5 segundos antes de intentar nuevamente
    else:
        print("❌ No se pudo conectar con la base de datos después de varios intentos.")
        raise ConnectionError("Conexión fallida con la base de datos.")


@app.on_event("startup")
async def startup_event():
    """
    Evento de inicio de la aplicación que espera la conexión a la base de datos.
    """
    print("🚀 Iniciando la aplicación...")
    await wait_for_db_connection()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
