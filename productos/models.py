from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    descripcion = models.TextField(blank=True, verbose_name="Descripcion")
    disponible = models.BooleanField(default=True, verbose_name="Disponible")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["nombre"]
    
    def __str__(self):
        return self.nombre