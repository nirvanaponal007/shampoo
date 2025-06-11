from django.db import models

class Venta(models.Model):
    idProducto = models.CharField(max_length=100)
    NombreProducto = models.CharField(max_length=100)
    PresentacionProducto = models.CharField(max_length=100)
    CantidadProductoblue = models.CharField(max_length=100)

def __str__(self): 
    return self.NombreProducto
