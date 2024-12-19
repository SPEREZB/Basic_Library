from django.db import models 
from django.forms import ModelForm  
# Create your models here.
class Libro(models.Model):
    id= models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30, verbose_name='Titulo')
    autor = models.CharField(max_length=100, verbose_name="Autor", default="Desconocido") # Campo autor
    categoria = models.CharField(max_length=50, choices=[
        ('ficcion', 'Ficción'),
        ('no-ficcion', 'No Ficción'),
        ('fantasia', 'Fantasía')
    ], verbose_name='Categoría',default="Desconocido")  # Campo categoría con opciones
    year = models.IntegerField(verbose_name='Año de publicación',default=2001)  # Campo año de publicación
    imagenes = models.ImageField(upload_to='Images', verbose_name='Imagen', null=True)
    descripcion = models.TextField(verbose_name='Descripcion', null=True)