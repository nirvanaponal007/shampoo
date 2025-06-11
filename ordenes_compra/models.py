from django.db import models

class Orden(models.Model):
    idOrdenCompra = models.CharField(max_length=100)
    idProducto = models.CharField(max_length=100)
    PresentacionSolicitada = models.CharField(max_length=100)
    CantidadSolicitada = models.CharField(max_length=100)
    PrecioUnidadSolicitada = models.CharField(max_length=100)


    def __str__(self):
        return self.idOrdenCompra
