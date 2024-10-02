from django import forms
from Sistema_Reservacion_Horas.models.aulas_model import Usuario, TiposUsuarios, Estado  # Asegúrate de que la ruta sea correcta

class UsuarioForms(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'password', 'cedula', 'no_carnet', 'tipo_usuario', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}, render_value=True),
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'no_carnet': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_usuario': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),  # Cambiado a Select para el estado
        }

    def __init__(self, *args, **kwargs):
        super(UsuarioForms, self).__init__(*args, **kwargs)
        # Cargar todos los tipos de usuarios
        self.fields['tipo_usuario'].queryset = TiposUsuarios.objects.all()
        # Cargar todos los estados disponibles
        self.fields['estado'].queryset = Estado.objects.all()

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise forms.ValidationError('El nombre es requerido.')
        if len(nombre) > 255:
            raise forms.ValidationError('El nombre no puede superar los 255 caracteres.')
        return nombre

    def clean_cedula(self):
        cedula = self.cleaned_data.get('cedula')
        if not cedula:
            raise forms.ValidationError('La cédula es requerida.')
        if len(cedula) > 15:
            raise forms.ValidationError('La cédula no puede superar los 15 caracteres.')
        return cedula

    def clean_no_carnet(self):
        no_carnet = self.cleaned_data.get('no_carnet')
        if not no_carnet:
            raise forms.ValidationError('El número de carnet es requerido.')
        if len(no_carnet) > 20:
            raise forms.ValidationError('El número de carnet no puede superar los 20 caracteres.')
        return no_carnet

    def clean_password(self):
        password = self.cleaned_data.get('password')
        # Si estamos editando, permite la contraseña existente
        if self.instance and self.instance.pk and not password:
            return self.instance.password
        return password

    def clean(self):
        cleaned_data = super().clean()
        tipo_usuario = cleaned_data.get('tipo_usuario')
        estado = cleaned_data.get('estado')

        if not tipo_usuario:
            raise forms.ValidationError('Debe seleccionar un tipo de usuario.')
        if not estado:
            raise forms.ValidationError('Debe seleccionar un estado válido.')

        return cleaned_data
