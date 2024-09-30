# forms.py
from django import forms
from Sistema_Reservacion_Horas.models.aulas_model import Usuario

class LoginForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")
        password = cleaned_data.get("password")

        # Verifica si los campos están vacíos
        if not nombre or not password:
            raise forms.ValidationError("Por favor, complete todos los campos.")

        # Verifica si el usuario existe y la contraseña es correcta
        try:
            usuario = Usuario.objects.get(nombre=nombre)
            if usuario.password != password:  # Considera usar un método seguro para comparar contraseñas
                raise forms.ValidationError("Contraseña incorrecta.")
        except Usuario.DoesNotExist:
            raise forms.ValidationError("El usuario no está registrado.")

        return cleaned_data
