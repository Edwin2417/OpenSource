from django import forms
from Sistema_Reservacion_Horas.models.aulas_model import ProcesoReservacionHoras, Empleado, AulasLaboratorios, Usuario, Estado  # Asegúrate de que la ruta sea correcta

class ProcesoReservacionHorasForm(forms.ModelForm):
    class Meta:
        model = ProcesoReservacionHoras
        fields = ['empleado', 'aula', 'usuario', 'fecha_reservacion', 'cantidad_horas', 'comentario', 'estado']
        widgets = {
            'empleado': forms.Select(attrs={'class': 'form-control'}),
            'aula': forms.Select(attrs={'class': 'form-control'}),
            'usuario': forms.HiddenInput(), # Hacer el campo no editable
            'fecha_reservacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cantidad_horas': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'comentario': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user', None)  # Obtener el ID del usuario actual
        super(ProcesoReservacionHorasForm, self).__init__(*args, **kwargs)

        # Filtrar los empleados activos
        self.fields['empleado'].queryset = Empleado.objects.filter(estado__descripcion='Activo')
        # Filtrar las aulas activas
        self.fields['aula'].queryset = AulasLaboratorios.objects.filter(estado__descripcion='Activo')
        # Filtrar los usuarios activos
        self.fields['usuario'].queryset = Usuario.objects.filter(estado__descripcion='Activo')

        if user_id:
            # Asignar automáticamente el usuario actual
            self.fields['usuario'].initial = user_id  # Establecer el usuario en el formulario

        # Cargar todas las opciones de estado
        self.fields['estado'].queryset = Estado.objects.all()

    def clean_fecha_reservacion(self):
        fecha_reservacion = self.cleaned_data.get('fecha_reservacion')
        if not fecha_reservacion:
            raise forms.ValidationError('La fecha de reservación es requerida.')
        return fecha_reservacion

    def clean_cantidad_horas(self):
        cantidad_horas = self.cleaned_data.get('cantidad_horas')
        if not cantidad_horas or cantidad_horas <= 0:
            raise forms.ValidationError('La cantidad de horas debe ser mayor a 0.')
        if cantidad_horas > 5:
            raise forms.ValidationError('La cantidad de horas no puede exceder 5.')
        return cantidad_horas

    def clean(self):
        cleaned_data = super().clean()
        empleado = cleaned_data.get('empleado')
        aula = cleaned_data.get('aula')
        usuario = cleaned_data.get('usuario')
        estado = cleaned_data.get('estado')

        # Validaciones adicionales según el caso
        if not empleado:
            raise forms.ValidationError('Debe seleccionar un empleado.')
        if not aula:
            raise forms.ValidationError('Debe seleccionar un aula.')
        if not usuario:
            raise forms.ValidationError('Debe seleccionar un usuario.')
        if not estado:
            raise forms.ValidationError('Debe seleccionar un estado válido.')

        return cleaned_data
