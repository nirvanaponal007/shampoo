#from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, TemplateView, DetailView, FormView, DeleteView
from ordenes_compra.ordenes_compra_manager import ordenes_manager


class ProductoTemplateView(TemplateView):
    template_name = 'productos/productos_list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = list(ordenes_manager.productos_generador())
        return context


class ProductoDetailView(DetailView):
    template_name = 'productos/productos_detail.html'
    context_object_name = 'producto'

    def get_object(self):
        id_Producto = self.kwargs.get('idProducto')
        print(id_Producto)
        return ordenes_manager.obtener_producto(id_Producto)
        