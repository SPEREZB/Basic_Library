# Usa una imagen base oficial de Python
FROM python:3.10-slim

# Mantén el autor de la imagen
LABEL authors="user"

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requerimientos al contenedor
COPY requirements.txt /app/

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Instala las dependencias de MySQL
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev && \
    apt-get clean

# Copia el resto de los archivos de la aplicación al contenedor
COPY . /app/

# Expone el puerto por defecto de Django
EXPOSE 8000

# Establece las variables de entorno necesarias para Django
ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=expo.settings \
    DEBUG=False

# Realiza las migraciones y recopila los archivos estáticos en el contenedor
RUN python manage.py collectstatic --noinput && \
    python manage.py migrate

# Configura el punto de entrada para ejecutar Django en modo producción
CMD ["gunicorn", "libreria.wsgi:application", "--bind", "0.0.0.0:8000"]