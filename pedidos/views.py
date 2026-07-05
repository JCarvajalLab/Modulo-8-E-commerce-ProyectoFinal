from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect, render
from carrito.carrito import Carrito
from productos.models import Producto
from .models import Pedido, DetallePedido


@login_required

@login_required
def confirmar_pedido(request):
    carrito = Carrito(request)
    contexto = {
        'productos_carrito': carrito.obtener_productos(),
        'total': carrito.obtener_total(),
    }
    return render(request, 'pedidos/confirmar_pedido.html', contexto)

def confirmar_compra(request):
    carrito = Carrito(request)
    productos_carrito = carrito.obtener_productos()
    if not productos_carrito:
        return redirect('carrito:ver_carrito')
    total = Decimal('0')
    for item in productos_carrito:
        total += item['subtotal']
    with transaction.atomic():
        pedido = Pedido.objects.create(usuario=request.user, total=total)
        for item in productos_carrito:
            DetallePedido.objects.create(
                pedido=pedido,
                producto=item['producto'],
                cantidad=item['cantidad'],
                precio_unitario=item['producto'].precio,
                subtotal=item['subtotal']
            )
            producto = item['producto']
            producto.stock -= item['cantidad']
            if producto.stock == 0:
                producto.disponible = False
            producto.save()
    carrito.vaciar()
    return redirect('carrito:ver_carrito')