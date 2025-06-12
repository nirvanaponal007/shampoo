from django.urls import path
from .import views
from ordenes_compra.views import OrdenTemplateView, OrdenFormView, OrdenDetailView, OrdenDeleteView, TaskUpdateView


urlpatterns = [
    path('',  OrdenTemplateView.as_view(), name= 'list_orden'),
    path('detail',  OrdenDetailView.as_view(), name= 'detail_orden'),
    path('form',  OrdenFormView.as_view(), name= 'form_orden'),
    path('delete',  OrdenDeleteView.as_view(), name= 'delete_orden'),
    path('update',  TaskUpdateView.as_view(), name= 'update_orden')
]