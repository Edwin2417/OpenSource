from django.shortcuts import render, get_object_or_404, redirect
from Sistema_Reservacion_Horas.models.aulas_model import TiposAulas
from Sistema_Reservacion_Horas.forms.tipos_aulas_forms import TiposAulasForm

# Vista para listar los tipos de aula
def listar_tipo_aula(request):
    tipos_aulas = TiposAulas.objects.all()
    return render(request, 'tipos/listar_tipo_aula.html', {'tipos_aulas': tipos_aulas})

# Vista para agregar un nuevo tipo de aula
def agregar_tipo_aula(request):
    if request.method == 'POST':
        form = TiposAulasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tipo_aula')
    else:
        form = TiposAulasForm()
    return render(request, 'tipos/agregar_tipo_aula.html', {'form': form})


# Vista para editar un tipo de aula existente
def editar_tipo_aula(request, pk):
    tipo_aula = get_object_or_404(TiposAulas, pk=pk)
    if request.method == 'POST':
        form = TiposAulasForm(request.POST, instance=tipo_aula)
        if form.is_valid():
            form.save()
            return redirect('listar_tipo_aula')
    else:
        form = TiposAulasForm(instance=tipo_aula)
    return render(request, 'tipos/editar_tipo_aula.html', {'form': form, 'tipo_aula': tipo_aula})


# Vista para eliminar un tipo de aula
def eliminar_tipo_aula(request, pk):
    tipo_aula = get_object_or_404(TiposAulas, pk=pk)
    if request.method == 'POST':
        tipo_aula.delete()
        return redirect('listar_tipo_aula')
    return render(request, 'tipos/eliminar_tipo_aula.html', {'tipo_aula': tipo_aula})

