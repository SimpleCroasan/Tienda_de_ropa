from django.db import models
from django.core.validators import MinValueValidator

class Producto(models.Model):
    Nombre = models.CharField(max_length=200)
    Descripcion = models.CharField(max_length=1000)
    Precio = models.DecimalField(max_digits=10, decimal_places=2)
    Imagen = models.ImageField(upload_to='static/img/productos/', null=True, blank=True)
    Unidades_disponibles = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    categoria = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.Nombre