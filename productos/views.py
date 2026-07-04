from django.shortcuts import render, get_object_or_404
from .models import Producto

def home(request):
    return render(request, 'productos/home.html')

def lista_productos(request):
    productos = Producto.objects.filter(disponible=True).order_by("-id")
    context = {'productos': productos}

    return render(request, 'productos/lista_productos.html', context)

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    context = {'producto' : producto}

    return render(request, 'productos/detalle_producto.html', context)