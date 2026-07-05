from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Ingresa tu usuario","autocomplete": "username",}),
    )

    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control","placeholder": "Ingresa tu contraseña","autocomplete": "current-password",}),
    )