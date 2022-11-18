# Comandos requeridos para trabajar con Django y enlace de descarga de Python
# Enlace para descargar Python
https://www.python.org/downloads/

# Instalar Django
pip3 install Django==3.0.7
 
# Crear proyecto
django-admin startproject nombre

# Crear aplicacion
django-admin startapp nombre

# Instalar mysql
pip3 install mysqlclient

# Instalar PyMysql
pip3 install PyMysqlclient

# Instalar Pillow
pip3 install pillow

# Migrar a base de datos
python manage.py migrate

# Migrar modelo
python manage.py makemigrations

# Crear super usuario
python manage.py createsuperuser
 
# Ejecutar server
python manage.py runserver
