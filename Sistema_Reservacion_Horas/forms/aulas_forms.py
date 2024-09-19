from django import forms
from Sistema_Reservacion_Horas.models.aulas_model import AulasLaboratorios, TiposAulas, Edificios


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
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input custom-checkbox-margin'}),
        }

    def __init__(self, *args, **kwargs):
        super(AulasLaboratoriosForm, self).__init__(*args, **kwargs)

        # Filtrar solo tipos de aula con estado True
        self.fields['tipo_aula'].queryset = TiposAulas.objects.filter(estado=True)

        # Filtrar solo edificios con estado True
        self.fields['edificio'].queryset = Edificios.objects.filter(estado=True)

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
            # Validación de que los cupos reservados no superen la capacidad
            if cupos_reservados > capacidad:
                self.add_error('cupos_reservados', 'Los cupos reservados no pueden ser mayores que la capacidad.')

            # Si los cupos reservados son iguales a la capacidad, desactivar y marcar estado como False
            if cupos_reservados == capacidad:
                cleaned_data['estado'] = False
                self.fields['estado'].widget.attrs['disabled'] = True
            # Si los cupos reservados son menores que la capacidad, activar y marcar estado como True
            else:
                cleaned_data['estado'] = True
                self.fields['estado'].widget.attrs.pop('disabled', None)  # Eliminar el atributo disabled si está presente

        return cleaned_data
