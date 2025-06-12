from django.contrib import admin
from django.urls import path, include
from . import views
#importamos la vista de ordenes de compra


urlpatterns = [
  
    path('',  views.index, name= 'index'),
    path('admin/', admin.site.urls),
    #Se incluye include para conectar URL de ordenes de compra
    path('ordenes/', include('ordenes_compra.urls')),
]



