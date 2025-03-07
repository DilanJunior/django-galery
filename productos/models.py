from django.db import models
from cloudinary.models import CloudinaryField


class Imagen(models.Model):
    nombre = models.CharField(max_length=255)
    imagen = CloudinaryField('image')  # Guarda la imagen en Cloudinary
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre