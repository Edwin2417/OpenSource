from django import forms
from Sistema_Reservacion_Horas.models.aulas_model import Campus, Estado

class CampusForms(forms.ModelForm):
    class Meta:
        model = Campus
        fields = ['descripcion', 'estado']
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),  # Cambiado a Select para elegir estado
        }

    def __init__(self, *args, **kwargs):
        super(CampusForms, self).__init__(*args, **kwargs)
        # Filtrar y asignar los estados disponibles para el campo 'estado'
        self.fields['estado'].queryset = Estado.objects.all()

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

        # Aquí puedes aplicar cualquier lógica adicional relacionada al estado o la descripción.
        # En este caso, si la descripción está vacía o el estado no es seleccionado, no pasa la validación.
        if not estado:
            raise forms.ValidationError('Debe seleccionar un estado válido.')

        return cleaned_data
