from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    # Relación 1 a 1 con el User por defecto
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    
    # Campos personalizados
    direccion = models.TextField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    foto_perfil = models.ImageField(upload_to='perfiles/', null=True, blank=True)
    biografia = models.TextField(max_length=500, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    
    # Metadata
    class Meta:
        verbose_name_plural = "Perfiles"
    
    def __str__(self):
        return f"Perfil de {self.usuario.username}"