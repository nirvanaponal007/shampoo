#from django.shortcuts import render



#Importaciones necesarias para ordenes_compra_manager.py:
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, TemplateView, DetailView, FormView, DetailView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django import forms
from .ordenes_compra_manager import ordenes_manager


@require_http_methods(["GET"])
def add_orden(request, idOrdenCompra):
    orden = ordenes_manager.add_orden(idOrdenCompra)
    return JsonResponse({
        'status': 'success',
        'orden': {
            'id': orden.idOrdenCompra,
            'idProducto' : orden.idProducto,
            'PresentacionSolicitada' : orden.PresentacionSolicitada,
            'CantidadSolicitada' : orden.CantidadSolicitada ,
            'PrecioUnidadSolicitada' : orden.PrecioUnidadSolicitada,
        }
    })




class OrdenListView(ListView):
    def get_queryset(self):
        return list(ordenes_manager.ordenes_generador())
    
    def render_to_response(self, context):
        return JsonResponse({
            'status':'success',
            'ordenes': self.get_queryset()
        })
    