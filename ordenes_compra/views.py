#from django.shortcuts import render



#Importaciones necesarias para ordenes_compra_manager.py:
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, TemplateView, DetailView, FormView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django import forms
from .ordenes_compra_manager import ordenes_manager


@require_http_methods(["GET"])
def add_orden(request, nombre_orden):
    orden = ordenes_manager.add_orden(nombre_orden)
    return JsonResponse({
        'status': 'success',
        'orden': {
            'id': orden.id,
            'title': orden.nombre_orden 
           
        }
    })



#Listar las Ordenes
class OrdenListView(ListView):
    def get_queryset(self):
        return list(ordenes_manager.ordenes_generador())
    
    def render_to_response(self, context):
        return JsonResponse({
            'status':'success',
            'ordenes': self.get_queryset()
        })



#renderizar desde orden_list.html
class OrdenTemplateView(TemplateView):
    template_name = 'ordenes/orden_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ordenes'] = list(ordenes_manager.ordenes_generador())
        return context
    

#ordenesDetalle
class OrdenDetailView (DetailView):
    template_name = 'ordenes/orden_detail.html'
    context_object_name = 'orden'

    def get_object(self):
        id_Orden= self.kwargs.get('idOrden_Compra')
        print(id_Orden)
        return ordenes_manager.obtener_orden(id_Orden)
    
    

#declaro ordenForm
class OrdenForm(forms.Form):
    codigo_oc = forms.CharField(max_length=50, required=True)
    #codigo_producto_oc = forms.IntegerField(required=True,  label="Ingresa un número", help_text="Debe estar entre 1 y 100")
    #presentacion_oc = forms.IntegerField(required=True,  label="Ingresa un número", help_text="Debe estar entre 1 y 100")
    #cantidad_oc = forms.IntegerField(required=True,  label="Ingresa un número", help_text="Debe estar entre 1 y 100")
    #precio_oc = forms.IntegerField(required=True,  label="Ingresa un número", help_text="Debe estar entre 1 y 100")

#Formulario
class OrdenFormView(FormView):
    template_name = 'ordenes/orden_form.html'
    form_class = OrdenForm
    success_url = reverse_lazy('list_orden')


    def form_valid(self, form):
        orden_titulo = form.cleaned_data['codigo_oc']
        #orden_titulo = form.cleaned_data['codigo_producto_oc']
        #orden_titulo = form.cleaned_data['presentacion_oc']
        #orden_titulo = form.cleaned_data['cantidad_oc']
        #orden_titulo = form.cleaned_data['precio_oc']
        ordenes_manager.add_orden(orden_titulo)
        return super().form_valid(form)
    


#Eliminar
class OrdenDeleteView(DeleteView):
    template_name = 'ordenes/orden_confirm_delete.html'
    success_url = reverse_lazy('list_orden')

    def get_object(self):
        orden_id = self.kwargs.get('idOrden_Compra')
        return ordenes_manager.obtener_orden(orden_id)
    
    def delete(self, request, *args, **kwargs):
        orden = self.get_object()
        ordenes_manager.borrar_orden(orden.id)
        return redirect(self.success_url)
    

#actualizar, pediente ajustar

class OrdenUpdateView(FormView):
    template_name = 'ordenes/orden_update.html'
    form_class = OrdenForm
    success_url = reverse_lazy('list_orden')

    
    def get_object(self):
        orden_id = self.kwargs.get('idOrden_Compra')
        return ordenes_manager.obtener_orden(orden_id)
    
    def get_initial(self):
        orden = self.get_object()
        return {'codigo_oc': orden.nombre_orden}
    
    def form_valid(self, form):
        orden = self.get_object()
        orden.nombre_orden = form.cleaned_data['codigo_oc']
        ordenes_manager.actualizar_orden(orden)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['idOrden_Compra'] = self.get_object()
        return context
    