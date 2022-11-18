from django.db import models 
from django.forms import ModelForm  
# Create your models here.
class Libro(models.Model):
    id= models.AutoField(primary_key=True) 
    nombre=models.CharField(max_length=30, verbose_name='Titulo')
    imagenes= models.ImageField(upload_to='Images', verbose_name='Imagen',null=True)
    descripcion= models.TextField(verbose_name='Descripcion',null=True)

 