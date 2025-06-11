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



class ordenes_compra_manager:

    def __init__(self):
        self.callbacks = []

    def registro_callback(self, callback):
        self.callbacks.append(callback)

    @timer_decorator
    def add_orden(self, titulo):
        orden = Orden.objects.create(titulo=titulo)
        for callback in self.callbacks:
            callback(orden)
        return orden

    def ordenes_generador(self):
        ordenes = Orden.objects.all().order_by('idOrdenCompra')
        for orden in ordenes:
            yield {
                'id': Orden.idOrdenCompra,
                'Cantidad': Orden.CantidadSolicitada
            }

    def obtener_orden(self, idOrdenCompra): 
        return Orden.objects.get(id=idOrdenCompra)
    
    def borrar_orden(self, idOrdenCompra):
        return Orden.objects.get(id=idOrdenCompra).delete()
    

    def actualizar_orden(self, orden):
        orden.save()
        