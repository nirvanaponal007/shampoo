from django.urls import path
from .import views
from productos.views import ProductoTemplateView, ProductoDetailView, ProductoUpdateView, ProductoDeleteView, ProductoListView, ProductoFormView


urlpatterns = [
    path('',  ProductoTemplateView.as_view(), name= 'list_producto'),
    path('<str:idProducto>/',  ProductoDetailView.as_view(), name= 'detail_producto'),
    path('form',  ProductoFormView.as_view(), name= 'form_producto'),
    path('<str:idProducto>/delete/',  ProductoDeleteView.as_view(), name= 'delete_producto'),
    path('<str:idProducto>/update/',  ProductoUpdateView.as_view(), name= 'update_producto'),
]



