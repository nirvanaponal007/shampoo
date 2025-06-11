# manager de models

from .models import Orden
import time
from functools import wraps



def timer_decorator(func):
    @wraps(func)
    def wrapper (*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function{func.__name__} took {execution_time:.2f} seconds to execute")
        return result
    return wrapper



class ordenesmanager:

    def __init__(self):
        self.callbacks = []

    def registro_callback(self, callback):
        self.callbacks.append(callback)

    @timer_decorator
    def add_orden(self, idOrdenCompra ):
        orden = Orden.objects.create(idOrdenCompra = idOrdenCompra )
        for callback in self.callbacks:
            callback(orden)
        return orden

    def ordenes_generador(self):
        ordenes = Orden.objects.all().order_by('idOrdenCompra')
        for orden in ordenes:
            yield {
                'id': Orden.idOrdenCompra,
                'idProducto' : orden.idProducto,
                'PresentacionSolicitada' : orden.PresentacionSolicitada,
                'CantidadSolicitada' : orden.CantidadSolicitada ,
                'PrecioUnidadSolicitada' : orden.PrecioUnidadSolicitada,
        }
            

    def obtener_orden(self, idOrdenCompra): 
        return Orden.objects.get(id=idOrdenCompra)
    
    def borrar_orden(self, idOrdenCompra):
        return Orden.objects.get(id=idOrdenCompra).delete()
    

    def actualizar_orden(self, orden):
        orden.save()

    def notificacion_creacion_orden(orden):
        print(f"Nueva Orden Creada: {orden.titulo}")



# crear una instancia global

ordenes_manager = ordenesmanager()
        