from django.db import models 
from django.forms import ModelForm  
# Create your models here. 
class Autor(models.Model):
    nombre = models.CharField(
        max_length=100,
        default="Autor Desconocido",
        verbose_name="Nombre del autor"
    )
    
    def __str__(self):
        return self.nombre

# models.py
class Libro(models.Model):
    GENERO_CHOICES = [
        ('F', 'Fantasía'),
        ('CF', 'Ciencia ficción'),
        ('T', 'Terror'),
        ('Z', 'Zombies'),
    ]
    
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    paginas = models.IntegerField(default=0)
    genero = models.CharField(max_length=2, choices=GENERO_CHOICES, default='F')
    portada = models.URLField(default="https://via.placeholder.com/300x450?text=Sin+portada")
    sinopsis = models.TextField(default="Sin sinopsis disponible")
    year = models.IntegerField(verbose_name="Año de publicación")
    isbn = models.CharField(max_length=20, default="000-0000000000")

    def get_genero_display(self):
        return dict(self.GENERO_CHOICES).get(self.genero, 'Desconocido')
    
    def __str__(self):
        return f"{self.titulo} ({self.year})"