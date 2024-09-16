from django.shortcuts import render, get_object_or_404, redirect
from Prueba.models.aulas_model import AulasLaboratorios
from Prueba.forms.aulas_forms import AulasLaboratoriosForm

# Vista para listar las aulas/laboratorios
def listar_aulas(request):
    aulas = AulasLaboratorios.objects.all()
    return render(request, 'aulas/listar_aulas.html', {'aulas': aulas})

# Vista para agregar una nueva aula/laboratorio
def agregar_aula(request):
    if request.method == 'POST':
        form = AulasLaboratoriosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_aulas')
    else:
        form = AulasLaboratoriosForm()
    return render(request, 'aulas/agregar_aula.html', {'form': form})

# Vista para editar una aula/laboratorio existente
def editar_aula(request, pk):
    aula = get_object_or_404(AulasLaboratorios, pk=pk)
    if request.method == 'POST':
        form = AulasLaboratoriosForm(request.POST, instance=aula)
        if form.is_valid():
            form.save()
            return redirect('listar_aulas')
    else:
        form = AulasLaboratoriosForm(instance=aula)
    return render(request, 'aulas/editar_aula.html', {'form': form, 'aula': aula})

# Vista para eliminar una aula/laboratorio
def eliminar_aula(request, pk):
    aula = get_object_or_404(AulasLaboratorios, pk=pk)
    if request.method == 'POST':
        aula.delete()
        return redirect('listar_aulas')
    return render(request, 'aulas/eliminar_aula.html', {'aula': aula})
