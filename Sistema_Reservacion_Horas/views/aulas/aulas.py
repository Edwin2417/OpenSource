from django.shortcuts import render, get_object_or_404, redirect
from Sistema_Reservacion_Horas.models.aulas_model import AulasLaboratorios
from Sistema_Reservacion_Horas.forms.aulas_forms import AulasLaboratoriosForm
from django.http import HttpResponseForbidden

# Verificación de permisos
def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        tipo_usuario = request.session.get('tipo_usuario')
        if tipo_usuario != 'Administrador':
            return HttpResponseForbidden("No tienes permiso para acceder a esta sección.")
        return view_func(request, *args, **kwargs)
    return wrapper

@admin_required
# Vista para listar las aulas/laboratorios
def listar_aulas(request):
    query = request.GET.get('q', '')  # Obtiene la consulta de búsqueda
    if query:
        aulas = AulasLaboratorios.objects.filter(descripcion__icontains=query)  # Filtra aulas por descripción
    else:
        aulas = AulasLaboratorios.objects.all()  # Obtiene todas las aulas si no hay consulta

    return render(request, 'aulas/listar_aulas.html', {'aulas': aulas})


@admin_required
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


@admin_required
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


@admin_required
# Vista para eliminar una aula/laboratorio
def eliminar_aula(request, pk):
    aula = get_object_or_404(AulasLaboratorios, pk=pk)
    if request.method == 'POST':
        aula.delete()
        return redirect('listar_aulas')
    return render(request, 'aulas/eliminar_aula.html', {'aula': aula})
