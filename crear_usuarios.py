import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

def crear_usuario(username, password, es_admin):
    if User.objects.filter(username=username).exists():
        print(f"El usuario '{username}' ya existe.")
        return

    if es_admin:
        User.objects.create_superuser(username=username, email="", password=password)
        print(f"Superusuario '{username}' creado correctamente.")
    else:
        User.objects.create_user(username=username, email="", password=password)
        print(f"Usuario '{username}' creado correctamente.")

if __name__ == "__main__":
    crear_usuario("admin", "Admin12345!", es_admin=True)
    crear_usuario("cliente", "Cliente12345!", es_admin=False)
