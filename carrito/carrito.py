from django.shortcuts import get_object_or_404
from productos.models import Producto

class Carrito:
    def __init__(self, request):
        self.session = request.session
        self.carrito = self.session.get('carrito', {})

    def agregar(self, producto_id):
        producto = get_object_or_404(Producto, id=producto_id)
        producto_id_str = str(producto.id)
        if producto_id_str in self.carrito:
            self.carrito[producto_id_str] += 1
        else:
            self.carrito[producto_id_str] = 1
        self.guardar()

    def obtener_productos(self):
        productos_carrito = []
        for producto_id, cantidad in self.carrito.items():
            producto = get_object_or_404(Producto, id=producto_id)
            subtotal = producto.precio * cantidad
            productos_carrito.append({
                'producto': producto,
                'cantidad': cantidad,
                'subtotal': subtotal,
            })
        return productos_carrito

    def obtener_total(self):
        total = 0
        for item in self.obtener_productos():
            total += item['subtotal']
        return total
    
    def guardar(self):
        self.session['carrito'] = self.carrito
        self.session.modified = True