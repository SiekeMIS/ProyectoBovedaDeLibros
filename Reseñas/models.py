from django.db import models
from django.contrib.auth.models import User
from Libros.models import Libro

class Reseña(models.Model):
    # Claves foráneas (optimizadas con índices)
    libro = models.ForeignKey(
        Libro, 
        on_delete=models.CASCADE, 
        related_name='reseñas',  # Acceso desde Libro: libro.reseñas.all()
        db_index=True  # ¡Importante para velocidad en búsquedas!
    )
    usuario = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='reseñas',  # Acceso desde User: usuario.reseñas.all()
        db_index=True
    )
    
    # Campos principales
    texto = models.TextField(max_length=1000)
    puntuacion = models.PositiveSmallIntegerField(  # Ej: 1-5 estrellas
        choices=[(i, str(i)) for i in range(1, 6)],
        default=5
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    # Metadata
    class Meta:
        verbose_name_plural = "Reseñas"
        ordering = ['-fecha_creacion']  # Ordenar por fecha descendente
        unique_together = [('libro', 'usuario')]  # Evitar reseñas duplicadas
    
    def __str__(self):
        return f"Reseña de {self.usuario.username} para {self.libro.titulo}"