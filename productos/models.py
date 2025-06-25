from django.db import models

class Producto(models.Model):
    NombreProducto = models.CharField(max_length=100)
    PresentacionProducto = models.CharField(max_length=100)
    CantidadProducto = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)

    def __str__(self): 
        return self.NombreProducto
    

