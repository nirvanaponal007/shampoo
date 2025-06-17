from django.db import models

class Orden(models.Model):
    #idOrdenCompra = models.IntegerField(unique=True)
    nombre_orden = models.CharField(max_length=50)
    #PresentacionSolicitada = models.IntegerField()  
    #CantidadSolicitada = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    #PrecioUnidadSolicitada = models.DecimalField( max_digits=8, decimal_places=2)


    def __str__(self):
        return self.nombre_orden
