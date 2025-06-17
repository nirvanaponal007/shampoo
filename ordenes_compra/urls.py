from django.urls import path
from .import views
from ordenes_compra.views import OrdenTemplateView, OrdenFormView, OrdenDetailView, OrdenDeleteView, OrdenUpdateView


urlpatterns = [
    path('',  OrdenTemplateView.as_view(), name= 'list_orden'),
    path('<str:idOrden_Compra>/',  OrdenDetailView.as_view(), name= 'detail_orden'),
    path('form',  OrdenFormView.as_view(), name= 'form_orden'),
    path('<str:idOrden_Compra>/delete/',  OrdenDeleteView.as_view(), name= 'delete_orden'),
    path('<str:idOrden_Compra>/update/',  OrdenUpdateView.as_view(), name= 'update_orden'),
]