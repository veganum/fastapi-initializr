from fastapi import APIRouter, Depends, HTTPException  # type: ignore
from sqlalchemy.ext.asyncio import AsyncSession  # type: ignore
from sqlalchemy.exc import SQLAlchemyError  # type: ignore
from app.schemas.user import UserCreate, UserResponse, UserBase
from app.services.user_service import (
    obtener_todos_usuarios,
    obtener_usuario_por_id,
    crear_usuario,
    actualizar_usuario,
    eliminar_usuario,
)
from app.core.database import get_db

router = APIRouter(prefix="/user", tags=["Users"])

@router.get("/users", response_model=list[UserResponse], summary="Obtener todos los usuarios")
async def obtener_usuarios(db: AsyncSession = Depends(get_db)):
    """
    Obtener todos los usuarios.

    :param db: Sesión de base de datos asíncrona.
    :return: Lista de usuarios.
    :raises HTTPException: Si ocurre un error en la base de datos.
    """
    try:
        return await obtener_todos_usuarios(db)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Error en la base de datos")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/user/{user_id}", response_model=UserResponse, summary="Obtener un usuario por ID")
async def obtener_usuario(user_id: int, db: AsyncSession = Depends(get_db)):
    """
    Obtener un usuario por ID.

    :param user_id: ID del usuario.
    :param db: Sesión de base de datos asíncrona.
    :return: Usuario encontrado.
    :raises HTTPException: Si el usuario no es encontrado o si ocurre un error en la base de datos.
    """
    try:
        usuario = await obtener_usuario_por_id(user_id, db)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return usuario
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Error en la base de datos")
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/create", response_model=UserResponse, summary="Crear un nuevo usuario")
async def crear_usuario_endpoint(user: UserCreate, db: AsyncSession = Depends(get_db)):
    """
    Crear un nuevo usuario.

    :param user: Datos del usuario a crear.
    :param db: Sesión de base de datos asíncrona.
    :return: Usuario creado.
    :raises HTTPException: Si ocurre un error en la base de datos.
    """
    try:
        return await crear_usuario(user, db)  # Pasar el objeto UserCreate directamente
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inesperado: {str(e)}")

@router.put("/update/{user_id}", response_model=UserResponse, summary="Actualizar un usuario existente")
async def actualizar_usuario_endpoint(user_id: int, user: UserBase, db: AsyncSession = Depends(get_db)):
    """
    Actualizar un usuario existente.

    :param user_id: ID del usuario a actualizar.
    :param user: Datos del usuario a actualizar.
    :param db: Sesión de base de datos asíncrona.
    :return: Usuario actualizado.
    :raises HTTPException: Si el usuario no es encontrado o si ocurre un error en la base de datos.
    """
    try:
        usuario = await obtener_usuario_por_id(user_id, db)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return await actualizar_usuario(user_id, user.dict(), db)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Error en la base de datos")
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/delete/{user_id}", summary="Eliminar un usuario")
async def eliminar_usuario_endpoint(user_id: int, db: AsyncSession = Depends(get_db)):
    """
    Eliminar un usuario.

    :param user_id: ID del usuario a eliminar.
    :param db: Sesión de base de datos asíncrona.
    :return: Mensaje de confirmación.
    :raises HTTPException: Si el usuario no es encontrado o si ocurre un error en la base de datos.
    """
    try:
        usuario = await obtener_usuario_por_id(user_id, db)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        await eliminar_usuario(user_id, db)
        return {"message": "Usuario eliminado correctamente"}
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Error en la base de datos")
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))