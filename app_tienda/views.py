from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Producto, Sucursal, Cliente




def inicio(request):
    return render(request,"app_tienda/index.html")

def clientes(request):
    query = request.GET.get("q")
    if query:
        clientes = Cliente.objects.filter(apellido__icontains=query)
    else:
        clientes = Cliente.objects.all()
    return render(request,"app_tienda/cliente.html",{"clientes":clientes})

def productos(request):
    query = request.GET.get("q")
    if query:
        productos = Producto.objects.filter(nombre__icontains=query)
    else:
        productos = Producto.objects.all()
    return render(request,"app_tienda/producto.html",{"productos":productos})

def sucursales(request):
    query = request.GET.get("q")
    if query:
        sucursales = Sucursal.objects.filter(nombre__icontains=query) 
    else:
        sucursales = Sucursal.objects.all()
    return render(request,"app_tienda/sucursal.html",{"sucursales":sucursales})

def producto_formulario(request):

    if request.method == "POST":
        producto = Producto(nombre=request.POST["nombre"],descripcion=request.POST["descripcion"],precio=request.POST["precio"],cantidad=request.POST["cantidad"])
        producto.save()
        return redirect("productos")
    else:
        return render(request,"app_tienda/forms/producto-formulario.html")
    
def sucursal_formulario(request):
    if request.method == "POST":
        sucursal = Sucursal(nombre=request.POST["nombre"],direccion=request.POST["direccion"],provincia=request.POST["provincia"])
        sucursal.save()
        return redirect("sucursales")
    else:
        return render(request,"app_tienda/forms/sucursal-formulario.html")
    
def cliente_formulario(request):
    if request.method == "POST":
        cliente = Cliente(nombre=request.POST["nombre"],apellido=request.POST["apellido"],email=request.POST["email"],pos_iva=request.POST["pos_iva"])
        cliente.save()
        return redirect("clientes")
    else:
        return render(request,"app_tienda/forms/cliente-formulario.html")


def ver_mas(request):
    return render(request,"app_tienda/ver-mas.html")