from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "descripcion", "precio", "stock", "categoria", "imagen", "disponible",]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre del producto",}),
            "descripcion": forms.Textarea(attrs={"class": "form-control","rows": 4,"placeholder": "Descripcion",}),
            "precio": forms.NumberInput(attrs={"class": "form-control",}),
            "stock": forms.NumberInput(attrs={"class": "form-control","placeholder": 0,}),
            "categoria": forms.Select(attrs={"class": "form-select",}),
            "imagen": forms.ClearableFileInput(attrs={"class": "form-control","accept": "image/*",}),
            "disponible": forms.CheckboxInput(attrs={"class": "form-check-input",}),
}

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if nombre:
            nombre = nombre.strip()
        if not nombre:
            raise forms.ValidationError(
                "El nombre del producto es obligatorio.")
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return nombre

    def clean_precio(self):
        precio = self.cleaned_data.get("precio")
        if precio is not None and precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor que 0.")
        return precio

    def clean_stock(self):
        stock = self.cleaned_data.get("stock")
        if stock is not None and stock < 0:
            raise forms.ValidationError("El stock no puede ser negativo.")
        return stock