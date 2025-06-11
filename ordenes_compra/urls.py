from django.urls import path
from .import views


urlpatterns = [
    #api endpoints
    path('add/<str:idOrdenCompra/>', views.add_orden, name='add_orden'),
    path('list/', views.OrdenListView.as_view(), name='ordenes'),

    # tempatle-based views
    path('', views.OrdenTemplateView.as_view(), name='list_orden'),
    path('form/', views.OrdenFormView.as_view(), name='orden_form'),
    path('<int:orden_id>', views.OrdenDeleteView.as_view(), name='orden_delete'),
    path('<int:orden_id>', views.OrdenUpdateView.as_view(), name='orden_update'),
]