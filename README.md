# Proyecto: Ejemplo de FastAPI

Este proyecto es un ejemplo básico de cómo iniciar un proyecto utilizando **Python** y **FastAPI**. Incluye pasos esenciales para configurar el entorno, instalar dependencias y ejecutar una aplicación FastAPI.

## Configuración del Entorno

### Activar el Entorno Virtual

En **Windows**:

```bash
venv\Scripts\activate
```

### Desactivar el Entorno Virtual

Cuando termines de trabajar en tu proyecto, desactiva el entorno virtual con:

```bash
deactivate
```

## Instalación de Dependencias

Instala todas las dependencias listadas en `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## Ejecución de la Aplicación FastAPI

### Forma 1: Ejecutar con Uvicorn

Ejecuta el servidor con el siguiente comando:

```bash
uvicorn app.main:app --reload
```

- **main**: El nombre del archivo principal sin la extensión `.py`.
- **app**: El nombre de la instancia de FastAPI dentro del archivo.

### Forma 2: Código con Ejecución Directa

Añade el siguiente bloque al final de tu archivo `main.py`:

```python
if __name__ == "__main__": 
    import uvicorn 
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
```

Luego, ejecuta el archivo:

```bash
python main.py
```

### Documentación Interactiva

FastAPI genera automáticamente documentación interactiva en las siguientes URLs:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Estructura Básica de un Proyecto FastAPI

```plaintext
🗂 proyecto-fastapi/
├── 🗂 app/                    # Directorio de la aplicación
│   ├── 🗄 main.py             # Archivo principal con la instancia de FastAPI
│   ├── 🗄 __init__.py         # Archivo de inicialización del paquete
│   ├── 🗂 api/                # Directorio de la API
│   │   ├── 🗄 __init__.py     # Archivo de inicialización del paquete
│   │   └── 🗂 v1/             # Versión 1 de la API
│   │       ├── 🗄 __init__.py # Archivo de inicialización del paquete
│   │       └── 🗂 endpoints/  # Endpoints de la API
│   │           ├── 🗄 user.py # Endpoints de usuario
│   │           └── 🗄 __init__.py # Archivo de inicialización del paquete
│   ├── 🗂 core/               # Directorio de configuración central
│   │   ├── 🗄 config.py       # Configuraciones de la aplicación
│   │   ├── 🗄 database.py     # Configuración de la base de datos
│   │   └── 🗄 __init__.py     # Archivo de inicialización del paquete
│   ├── 🗂 db/                 # Directorio de la base de datos
│   │   ├── 🗄 session.py      # Sesión de la base de datos
│   │   ├── 🗄 __init__.py     # Archivo de inicialización del paquete
│   │   └── 🗂 models/         # Modelos de la base de datos
│   │       ├── 🗄 user.py     # Modelo de usuario
│   │       └── 🗄 __init__.py # Archivo de inicialización del paquete
│   ├── 🗂 schemas/            # Esquemas de la aplicación
│   │   ├── 🗄 user.py         # Esquema de usuario
│   │   └── 🗄 __init__.py     # Archivo de inicialización del paquete
│   ├── 🗂 services/           # Servicios de la aplicación
│   │   ├── 🗄 user_service.py # Servicio de usuario
│   │   └── 🗄 __init__.py     # Archivo de inicialización del paquete
├── 🗄 requirements.txt        # Dependencias del proyecto
├── 🗄 .pylintrc               # Archivo de configuración del linter
├── 🗄 Dockerfile              # Archivo de configuración de Docker
├── 🗄 docker-compose.yml      # Archivo de configuración de Docker Compose
├── 🗄 README.md               # Documentación del proyecto
├── 🗂 env/                    # Entorno virtual (excluido del control de versiones)
```

---

## Integración con Docker

### Construir y Ejecutar el Contenedor

Construye la imagen de Docker:

```bash
docker-compose build
```

Ejecuta el contenedor:

```bash
docker-compose up
```

Para detener el contenedor:

```bash
docker-compose down
```

Para borrar volumenes y contenedores:

```bash
docker-compose down --volumes --remove-orphans
```

---

## Base de Datos

### Script de Inserción de Usuarios

Inserta datos en la tabla `usuarios`:

```sql
INSERT INTO usuarios (id, nombre, apellido, direccion, telefono, creacion_user)
VALUES
    (1, 'José', 'Franco Nieto', 'C/ incognito', 670302349, NOW()),
    (2, 'Bozhidara', 'Angelova Nedyalkova', 'C/ incognito', 670302349, NOW()),
    (3, 'Alejandro', 'García López', 'C/ Gran Vía nº 10 2ºB', 680123456, NOW()),
    (4, 'Lucía', 'Martínez Sánchez', 'C/ Alcalá nº 15 Bajo A', 690234567, NOW()),
    (5, 'Carlos', 'Hernández Gómez', 'C/ Serrano nº 45 3ºC', 670345678, NOW()),
    (6, 'María', 'Ruiz Fernández', 'C/ Velázquez nº 3 1ºA', 660456789, NOW()),
    (7, 'David', 'Pérez Torres', 'C/ Castellana nº 50 5ºD', 650567890, NOW()),
    (8, 'Elena', 'López Morales', 'C/ Hortaleza nº 100 4ºB', 640678901, NOW()),
    (9, 'Miguel', 'Gómez Martín', 'C/ Princesa nº 20 Bajo B', 630789012, NOW()),
    (10, 'Ana', 'Díaz Ramírez', 'C/ Mayor nº 80 2ºC', 620890123, NOW());
```

Con esta guía, puedes configurar, desarrollar y ejecutar proyectos básicos utilizando **Python**, **FastAPI** y **Docker**. ¡Listo para empezar! 🚀
# fastapi-initializr
