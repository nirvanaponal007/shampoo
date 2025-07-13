#from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, TemplateView, DetailView, FormView, DeleteView
from ordenes_compra.ordenes_compra_manager import ordenes_manager
from django import forms
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.http import JsonResponse




#Listar los productos
class ProductoListView(ListView):
    def get_queryset(self):
        return list(ordenes_manager.productos_generador())
    
    def render_to_response(self, context):
        return JsonResponse({
            'status':'success',
            'productos': self.get_queryset()
        })



#renderizar desde productos_list.html
class ProductoTemplateView(TemplateView):
    template_name = 'productos/productos_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = list(ordenes_manager.productos_generador())
        return context

#productosDetalle
class ProductoDetailView(DetailView):
    template_name = 'productos/productos_detail.html'
    context_object_name = 'producto'

    def get_object(self):
        id_Producto = self.kwargs.get('idProducto')
        print(id_Producto)
        return ordenes_manager.obtener_producto(id_Producto)
    
#Declaro ProductoForm
class ProductoForm(forms.Form):
    NombreProducto_p = forms.CharField(max_length=100)
    PresentacionProducto_p = forms.CharField(max_length=100)
    CantidadProducto_p = forms.DecimalField(max_digits=8, decimal_places=2)

#Formulario
class ProductoFormView(FormView):
    template_name = 'productos/productos_form.html'
    form_class = ProductoForm
    success_url = reverse_lazy('list_producto')


    def form_valid(self, form):
        NombreProducto = form.cleaned_data['NombreProducto_p']
        PresentacionProducto = form.cleaned_data['PresentacionProducto_p']
        CantidadProducto = form.cleaned_data['CantidadProducto_p']
        ordenes_manager.add_producto(NombreProducto, PresentacionProducto, CantidadProducto)
        return super().form_valid(form)
    


#Eliminar Producto
class ProductoDeleteView(DeleteView):
    template_name = 'productos/productos_confirm_delete.html'
    success_url = reverse_lazy('list_producto')

    def get_object(self):
        producto_id = self.kwargs.get('idProducto')
        return ordenes_manager.obtener_producto(producto_id)
    
    def delete(self, request, *args, **kwargs):
        producto = self.get_object()
        ordenes_manager.borrar_producto(producto.id)
        return redirect(self.success_url)



#Actualizar Productos
class ProductoUpdateView(FormView):
    template_name = 'productos/productos_update.html'
    form_class = ProductoForm
    success_url = reverse_lazy('list_producto')

    def get_object(self):
        producto_id = self.kwargs.get('idProducto')
        return ordenes_manager.obtener_producto(producto_id)
    
    def get_initial(self):
        producto = self.get_object()
        return {'NombreProducto_p': producto.NombreProducto,
                'PresentacionProducto_p': producto.PresentacionProducto,
                'CantidadProducto_p': producto.CantidadProducto,
                }
    
    def form_valid(self, form):
        producto = self.get_object()
        producto.NombreProducto = form.cleaned_data['NombreProducto_p']
        producto.PresentacionProducto = form.cleaned_data['PresentacionProducto_p']
        producto.CantidadProducto = form.cleaned_data['CantidadProducto_p']
        ordenes_manager.actualizar_producto(producto)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['idProducto'] = self.get_object()
        return context

