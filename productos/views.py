from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from .forms import ProductoForm
from django.contrib import messages
from django.db.models.deletion import ProtectedError

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

# CRUD DEL USUARIO ADMINISTRADOR

@login_required
def panel_productos(request):
    if not request.user.is_staff:
        raise PermissionDenied
    productos = Producto.objects.all().order_by("-id")
    context = {'productos': productos}
    return render(request, "productos/panel_productos.html", context)

@login_required
def crear_producto(request):
    if not request.user.is_staff:
        raise PermissionDenied
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Producto creado correctamente.")
            return redirect("productos:panel_productos")
    else:
        form = ProductoForm()
    context = { "form": form }
    return render(request, "productos/formulario_producto.html", context)

@login_required
def editar_producto(request, producto_id):
    if not request.user.is_staff:
        raise PermissionDenied
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request,"Producto actualizado correctamente.")
            return redirect("productos:panel_productos")
    else:
        form = ProductoForm(instance=producto)
    context = { "form": form, "producto": producto }
    return render(request, "productos/formulario_producto.html", context)

@login_required
def eliminar_producto(request, producto_id):
    if not request.user.is_staff:
        raise PermissionDenied
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == "POST":
        try:
            producto.delete()
            messages.success(request, "Producto eliminado correctamente.")
        except ProtectedError:
            messages.error(request,"No es posible eliminar este producto porque está asociado a uno o más pedidos.")
        return redirect("productos:panel_productos")
    context = {"producto": producto}
    return render(request, "productos/confirmar_eliminar.html", context)

