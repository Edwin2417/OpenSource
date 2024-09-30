from django import forms
from Sistema_Reservacion_Horas.models.aulas_model import Edificios


class EdificiosForms(forms.ModelForm):
    class Meta:
        model = Edificios
        fields = ['descripcion', 'estado', 'campus']  # Agregando el campo campus
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'campus': forms.Select(attrs={'class': 'form-control'}),  # Para el campo campus
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input custom-checkbox-margin'}),
        }

    def __init__(self, *args, **kwargs):
        super(EdificiosForms, self).__init__(*args, **kwargs)
        # Aquí podrías personalizar más el formulario si es necesario

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if not descripcion:
            raise forms.ValidationError('La descripción es requerida.')
        if len(descripcion) > 255:
            raise forms.ValidationError('La descripción no puede superar los 255 caracteres.')
        return descripcion

    def clean(self):
        cleaned_data = super().clean()
        estado = cleaned_data.get('estado')
        campus = cleaned_data.get('campus')  # Obtener el campo campus

        # Validación adicional
        if not estado and not cleaned_data.get('descripcion'):
            raise forms.ValidationError('Debe proporcionar una descripción y un estado válido.')

        if not campus:
            raise forms.ValidationError('Debe seleccionar un campus.')

        return cleaned_data
