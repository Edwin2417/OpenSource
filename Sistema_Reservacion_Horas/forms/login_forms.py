from django import forms
from Sistema_Reservacion_Horas.models.aulas_model import Usuario


class LoginForm(forms.Form):
    no_carnet = forms.CharField(
        label='Número de Carnet',
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    def clean_no_carnet(self):
        no_carnet = self.cleaned_data.get("no_carnet")
        # Verificar si el usuario existe
        if not Usuario.objects.filter(no_carnet=no_carnet).exists():
            raise forms.ValidationError("El usuario no está registrado.")
        return no_carnet

    def clean_password(self):
        no_carnet = self.cleaned_data.get("no_carnet")
        password = self.cleaned_data.get("password")

        if no_carnet and password:
            try:
                usuario = Usuario.objects.get(no_carnet=no_carnet)
                if usuario.password != password:  # Verificación básica de contraseñas
                    raise forms.ValidationError("Contraseña incorrecta.")
            except Usuario.DoesNotExist:
                pass  # Esto ya lo manejamos en clean_no_carnet
        return password
