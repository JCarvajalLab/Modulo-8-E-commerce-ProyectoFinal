from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from .forms import LoginForm

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect("productos:home")
    else:
        form = LoginForm(request)
    context = {"form": form}
    return render(request, "usuarios/login.html", context)

def logout_view(request):
    logout(request)
    return redirect("productos:home")