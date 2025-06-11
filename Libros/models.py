from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_publicacion = models.DateField(null=True, blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    genero = models.ManyToManyField(Genero)
    isbn = models.CharField(max_length=13, unique=True, blank=True, null=True)
    portada = models.ImageField(upload_to='portadas/', blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    rating = models.FloatField(default=0)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    favoritos_de = models.ManyToManyField(User, related_name='libros_favoritos')

    def __str__(self):
        return f"{self.titulo} ({self.autor.nombre if self.autor else 'Autor desconocido'})"

    class Meta:
        ordering = ['-fecha_agregado']