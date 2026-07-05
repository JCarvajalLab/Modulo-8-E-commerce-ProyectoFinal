from django.shortcuts import render, redirect
from .carrito import Carrito

def ver_carrito(request):
    carrito = Carrito(request)
    contexto = {
        'productos_carrito': carrito.obtener_productos(),
        'total': carrito.obtener_total(),}
    return render(request, 'carrito/ver_carrito.html', contexto)

def agregar_al_carrito(request, producto_id):
    carrito = Carrito(request)
    carrito.agregar(producto_id)
    return redirect('carrito:ver_carrito')

def eliminar_del_carrito(request, producto_id):
    carrito = Carrito(request)
    carrito.eliminar(producto_id)
    return redirect('carrito:ver_carrito')