from django.urls import path
from .views import clientes, productos, sucursales, inicio, producto_formulario, sucursal_formulario, cliente_formulario, ver_mas

urlpatterns = [
    path('', inicio, name="inicio"),
    path('productos/', productos, name="productos"),
    path('clientes/', clientes, name="clientes"),
    path('sucursales/', sucursales, name="sucursales"),
    path('agregar-producto', producto_formulario, name="agregar-producto"),
    path('agregar-sucursal', sucursal_formulario, name="agregar-sucursal"),
    path('agregar-cliente', cliente_formulario, name="agregar-cliente"),
    path('ver-mas', ver_mas, name="ver-mas"),
]