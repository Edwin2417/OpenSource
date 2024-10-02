from django import forms
from Sistema_Reservacion_Horas.models.aulas_model import AulasLaboratorios, TiposAulas, Edificios, Estado


class AulasLaboratoriosForm(forms.ModelForm):
    class Meta:
        model = AulasLaboratorios
        fields = ['descripcion', 'tipo_aula', 'edificio', 'capacidad', 'cupos_reservados', 'estado']
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_aula': forms.Select(attrs={'class': 'form-control'}),
            'edificio': forms.Select(attrs={'class': 'form-control'}),
            'capacidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'cupos_reservados': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(AulasLaboratoriosForm, self).__init__(*args, **kwargs)

        # Filtrar solo tipos de aula con estado activo
        self.fields['tipo_aula'].queryset = TiposAulas.objects.filter(estado__descripcion="Activo")

        # Filtrar solo edificios con estado activo
        self.fields['edificio'].queryset = Edificios.objects.filter(estado__descripcion="Activo")

        # Filtrar solo estados disponibles para selección
        self.fields['estado'].queryset = Estado.objects.all()

    def clean_capacidad(self):
        capacidad = self.cleaned_data.get('capacidad')
        if capacidad is None:
            raise forms.ValidationError('La capacidad es requerida.')
        if capacidad < 0 or capacidad > 30:
            raise forms.ValidationError('La capacidad debe estar entre 0 y 30.')
        return capacidad

    def clean_cupos_reservados(self):
        cupos_reservados = self.cleaned_data.get('cupos_reservados')
        if cupos_reservados is None:
            raise forms.ValidationError('Los cupos reservados son requeridos.')
        if cupos_reservados < 0 or cupos_reservados > 30:
            raise forms.ValidationError('Los cupos reservados deben estar entre 0 y 30.')
        return cupos_reservados

    def clean(self):
        cleaned_data = super().clean()
        capacidad = cleaned_data.get('capacidad')
        cupos_reservados = cleaned_data.get('cupos_reservados')

        # Verificar si la capacidad y los cupos reservados están disponibles
        if capacidad is not None and cupos_reservados is not None:
            # Si los cupos reservados son iguales a la capacidad, asignar el estado "Inactivo"
            if cupos_reservados == capacidad:
                estado_inactivo = Estado.objects.get(descripcion="Inactivo")
                cleaned_data['estado'] = estado_inactivo
                self.fields['estado'].widget.attrs['disabled'] = True
            # Si los cupos reservados son menores a la capacidad, asignar el estado "Activo"
            elif cupos_reservados < capacidad:
                estado_activo = Estado.objects.get(descripcion="Activo")
                cleaned_data['estado'] = estado_activo
                self.fields['estado'].widget.attrs.pop('disabled', None)  # Eliminar el atributo disabled si está presente

        return cleaned_data
