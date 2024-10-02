from django import forms
from Sistema_Reservacion_Horas.models.aulas_model import Edificios, Campus, Estado

class EdificiosForms(forms.ModelForm):
    class Meta:
        model = Edificios
        fields = ['descripcion', 'estado', 'campus']
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'campus': forms.Select(attrs={'class': 'form-control'}),  # Campo campus como un Select
            'estado': forms.Select(attrs={'class': 'form-control'}),  # Cambiado a Select para el estado
        }

    def __init__(self, *args, **kwargs):
        super(EdificiosForms, self).__init__(*args, **kwargs)

        # Filtrar los estados disponibles para el campo 'estado'
        self.fields['estado'].queryset = Estado.objects.all()

        # Filtrar solo los campus activos para el campo 'campus'
        self.fields['campus'].queryset = Campus.objects.filter(estado__descripcion="Activo")

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
        campus = cleaned_data.get('campus')

        # Validación adicional
        if not estado:
            raise forms.ValidationError('Debe seleccionar un estado válido.')

        if not campus:
            raise forms.ValidationError('Debe seleccionar un campus.')

        return cleaned_data
