from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.clientes, name='clientes'),
    path('productos/', views.productos, name='productos'),
    path('proveedores/', views.proveedores, name='proveedores'),
    path('search/', views.search, name='search'),
    path('delete_cliente/<int:id>/', views.delete_cliente, name='delete_cliente'),  # Eliminar cliente
    path('delete_producto/<int:id>/', views.delete_producto, name='delete_producto'),  # Eliminar producto
    path('delete_proveedor/<int:id>/', views.delete_proveedor, name='delete_proveedor'),  # Eliminar proveedor
]