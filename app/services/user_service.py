"""
Este módulo proporciona servicios para gestionar usuarios en la base de datos.
"""

import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from app.db.models.user import UserModel
from app.schemas.user import UserCreate


async def obtener_todos_usuarios(db: AsyncSession):
    """
    Obtener todos los usuarios de la base de datos.

    :param db: Sesión de base de datos asíncrona.
    :return: Lista de usuarios.
    """
    result = await db.execute(select(UserModel))
    return result.scalars().all()


async def obtener_usuario_por_id(user_id: int, db: AsyncSession):
    """
    Obtener un usuario por su ID.

    :param user_id: ID del usuario.
    :param db: Sesión de base de datos asíncrona.
    :return: Usuario encontrado o None.
    """
    return await db.get(UserModel, user_id)


async def crear_usuario(user: UserCreate, db: AsyncSession) -> UserModel:
    """
    Crear un nuevo usuario en la base de datos.

    :param user: Datos del usuario a crear.
    :param db: Sesión de base de datos asíncrona.
    :return: Usuario creado.
    :raises SQLAlchemyError: Si ocurre un error en la base de datos.
    """
    nuevo_usuario = UserModel(
        nombre=user.nombre,
        apellido=user.apellido,
        direccion=user.direccion,
        telefono=user.telefono,
        creacion_user=datetime.datetime.utcnow()
    )
    db.add(nuevo_usuario)
    try:
        await db.commit()
        await db.refresh(nuevo_usuario)
        return nuevo_usuario
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"Error en la base de datos: {str(e)}") from e
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"Error inesperado: {str(e)}") from e


async def actualizar_usuario(user_id: int, user_data: dict, db: AsyncSession):
    """
    Actualizar un usuario existente en la base de datos.

    :param user_id: ID del usuario a actualizar.
    :param user_data: Datos actualizados del usuario.
    :param db: Sesión de base de datos asíncrona.
    :return: Usuario actualizado.
    """
    usuario = await db.get(UserModel, user_id)
    for key, value in user_data.items():
        setattr(usuario, key, value)
    await db.commit()
    await db.refresh(usuario)
    return usuario


async def eliminar_usuario(user_id: int, db: AsyncSession):
    """
    Eliminar un usuario de la base de datos.

    :param user_id: ID del usuario a eliminar.
    :param db: Sesión de base de datos asíncrona.
    """
    usuario = await db.get(UserModel, user_id)
    await db.delete(usuario)
    await db.commit()
