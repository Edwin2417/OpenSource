from django import forms
from Prueba.models.aulas_model import AulasLaboratorios

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
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
