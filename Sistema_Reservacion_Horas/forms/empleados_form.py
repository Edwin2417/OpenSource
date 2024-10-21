from django import forms
from Sistema_Reservacion_Horas.models.aulas_model import Empleado, Tanda, Estado, Usuario, TiposUsuarios

class EmpleadosForms(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'cedula', 'tanda', 'fecha_ingreso', 'estado', 'usuario']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'tanda': forms.Select(attrs={'class': 'form-control'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EmpleadosForms, self).__init__(*args, **kwargs)
        tipo_empleado = TiposUsuarios.objects.get(descripcion='Empleado')

        # Obtener el empleado actual (si está en modo edición)
        empleado = kwargs.get('instance')

        # Filtrar los usuarios asignados
        usuarios_asignados = Empleado.objects.exclude(usuario__isnull=True).exclude(identificador=empleado.identificador if empleado else None).values_list('usuario', flat=True)

        # Filtrar los usuarios con tipo 'Empleado' que no estén asignados a otro empleado, pero incluye al usuario actual si está editando
        self.fields['usuario'].queryset = Usuario.objects.filter(
            tipo_usuario=tipo_empleado,
            estado__descripcion="Activo"  # Aquí filtramos por estado activo
        ).exclude(identificador__in=usuarios_asignados)

        self.fields['tanda'].queryset = Tanda.objects.all()
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

    def clean_fecha_ingreso(self):
        fecha_ingreso = self.cleaned_data.get('fecha_ingreso')
        if not fecha_ingreso:
            raise forms.ValidationError('La fecha de ingreso es requerida.')
        return fecha_ingreso

    def clean(self):
        cleaned_data = super().clean()
        tanda = cleaned_data.get('tanda')
        estado = cleaned_data.get('estado')
        usuario = cleaned_data.get('usuario')

        if not tanda:
            raise forms.ValidationError('Debe seleccionar una tanda.')
        if not estado:
            raise forms.ValidationError('Debe seleccionar un estado válido.')
        if not usuario:
            raise forms.ValidationError('Debe seleccionar un usuario válido.')

        return cleaned_data
