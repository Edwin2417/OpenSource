from django.shortcuts import render, get_object_or_404, redirect
from Sistema_Reservacion_Horas.models.aulas_model import TiposAulas
from Sistema_Reservacion_Horas.forms.tipos_aulas_forms import TiposAulasForm
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
# Vista para listar los tipos de aula
def listar_tipo_aula(request):
    query = request.GET.get('q', '')  # Obtiene la consulta de búsqueda
    if query:
        tipos_aulas = TiposAulas.objects.filter(descripcion__icontains=query)  # Filtra aulas por descripción
    else:
        tipos_aulas = TiposAulas.objects.all()  # Obtiene todas las aulas si no hay consulta

    return render(request, 'tipos/listar_tipo_aula.html', {'tipos_aulas': tipos_aulas})


@admin_required
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


@admin_required
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


@admin_required
# Vista para eliminar un tipo de aula
def eliminar_tipo_aula(request, pk):
    tipo_aula = get_object_or_404(TiposAulas, pk=pk)
    if request.method == 'POST':
        tipo_aula.delete()
        return redirect('listar_tipo_aula')
    return render(request, 'tipos/eliminar_tipo_aula.html', {'tipo_aula': tipo_aula})

