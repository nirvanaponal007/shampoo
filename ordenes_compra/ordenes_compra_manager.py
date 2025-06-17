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
    def add_orden(self, nombre_orden ):
        orden = Orden.objects.create(nombre_orden = nombre_orden )
        for callback in self.callbacks:
            callback(orden)
        return orden

    def ordenes_generador(self):
        ordenes = Orden.objects.all().order_by('nombre_orden')
        for orden in ordenes:
            yield {
                'id': orden.id,
                'title': orden.nombre_orden
        }
            

    def obtener_orden(self, id_orden): 
        return Orden.objects.get(id=id_orden)
    
    def borrar_orden(self, id_orden):
        return Orden.objects.get(id=id_orden).delete()
    

    def actualizar_orden(self, orden):
        orden.save()

    def notificacion_creacion_orden(orden):
        print(f"Nueva Orden Creada: {orden.nombre_orden}")



# crear una instancia global

ordenes_manager = ordenesmanager()
        