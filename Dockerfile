# Usa una imagen base ligera de Python
FROM python:3.9-slim

# Define el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos necesarios para instalar las dependencias
COPY requirements.txt /app/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del proyecto al contenedor
COPY . /app

# Expone el puerto 8000 para la aplicación
EXPOSE 8000

# Comando por defecto para iniciar FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
