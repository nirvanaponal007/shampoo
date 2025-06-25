from django.urls import path
from .import views
from productos.views import ProductoTemplateView, ProductoDetailView


urlpatterns = [
    path('',  ProductoTemplateView.as_view(), name= 'list_producto'),
    path('<str:idProducto>/',  ProductoDetailView.as_view(), name= 'detail_producto'),
   # path('form',  OrdenFormView.as_view(), name= 'form_orden'),
   # path('<str:idOrden_Compra>/delete/',  OrdenDeleteView.as_view(), name= 'delete_orden'),
   # path('<str:idOrden_Compra>/update/',  OrdenUpdateView.as_view(), name= 'update_orden'),
]



