from django import forms
from Sistema_Reservacion_Horas.models.aulas_model import TiposAulas

class TiposAulasForm(forms.ModelForm):
    class Meta:
        model = TiposAulas
        fields = ['descripcion', 'estado']
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input custom-checkbox-margin'}),
        }

    def __init__(self, *args, **kwargs):
        super(TiposAulasForm, self).__init__(*args, **kwargs)

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
        if not estado and not cleaned_data.get('descripcion'):
            raise forms.ValidationError('Debe proporcionar una descripción y un estado válido.')

        return cleaned_data
