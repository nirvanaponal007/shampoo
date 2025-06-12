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
    #'ordenes/orden_list.html'

    #def get_context_data(self, **kwargs):
     #   context = super().get_context_data(**kwargs)
      #  context['ordenes'] = list(ordenes_manager.ordenes_generador())
       # return context
    

#ordenesDetalle
class OrdenDetailView (TemplateView):   #(DetailView):
    template_name = 'ordenes/orden_detail.html'
   # context_object_name = 'orden'

    #def get_object(self):
     #   orden_id= self.kwargs.get('id_orden')
      #  return ordenes_manager.obtener_orden(orden_id)
    

#declaro ordenForm
class OrdenForm(TemplateView): #(forms.Form):
    #orden_titulo = forms.CharField(max_length=100, label='Orden Titulo')
    template_name = 'ordenes/orden_form.html'


#Formulario
class OrdenFormView(TemplateView): #(FormView):
    template_name = 'ordenes/orden_form.html'
   # form_class = OrdenForm
    #success_url = reverse_lazy('list_orden')


    #def form_valid(self, form):
     #   orden_titulo = form.cleaned_data['orden_titulo']
      #  ordenes_manager.add_orden(orden_titulo)
       # return super().form_valid(form)
    


#Eliminar
class OrdenDeleteView(TemplateView):#(DetailView):
    template_name = 'ordenes/orden_confirm_delete.html'
    #success_url = reverse_lazy('list_orden')

    #def get_object(self):
        #orden_id = self.kwargs.get('id_orden')
        #return ordenes_manager.obtener_orden(orden_id)
    
    #def delete(self, request, *args, **kwargs):
        #orden = self.get_object()
        #ordenes_manager.borrar_orden(orden.id)
        #return redirect(self.success_url)
    



#actualizar, pediente ajustar

class TaskUpdateView(TemplateView): #(TemplateView): #(FormView):
    template_name = 'ordenes/orden_update.html'
    #form_class = OrdenForm
    #success_url = reverse_lazy('list_orden')

    
    #def get_object(self):
        #task_id = self.kwargs.get('task_id')
        #return ordenes_manager.get_task(task_id)
    
    #def get_initial(self):
        #task = self.get_object()
        #return {'title': task.title}
    
    #def form_valid(self, form):
        #task = self.get_object()
        #task.title = form.cleaned_data['title']
        #ordenes_manager.update_task(task)
        #return super().form_valid(form)
    
    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #context['task'] = self.get_object()
        #return context
    