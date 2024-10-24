from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from Sistema_Reservacion_Horas.models.aulas_model import Campus
from Sistema_Reservacion_Horas.forms.campus_forms import CampusForms
from django.http import HttpResponseForbidden
from Sistema_Reservacion_Horas.views.utils import paginar_objetos

# Verificación de permisos
def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        tipo_usuario = request.session.get('tipo_usuario')
        if tipo_usuario != 'Administrador':
            return HttpResponseForbidden("No tienes permiso para acceder a esta sección.")
        return view_func(request, *args, **kwargs)
    return wrapper

# Campus CRUD

@admin_required
def listar_campus(request):
    query = request.GET.get('q', '')  # Obtiene la consulta de búsqueda
    if query:
        campus = Campus.objects.filter(descripcion__icontains=query)  # Filtra aulas por descripción
    else:
        campus = Campus.objects.all()  # Obtiene todas las aulas si no hay consulta

    page_obj = paginar_objetos(request, campus, 4)

    return render(request, 'campus/listar_campus.html', {'page_obj': page_obj, 'campus': campus})


@admin_required
def agregar_campus(request):
    if request.method == 'POST':
        form = CampusForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Campus creado con éxito.')
            return redirect('listar_campus')
    else:
        form = CampusForms()
    return render(request, 'campus/agregar_campus.html', {'form': form})


@admin_required
def editar_campus(request, pk):
    campus = get_object_or_404(Campus, pk=pk)
    if request.method == 'POST':
        form = CampusForms(request.POST, instance=campus)
        if form.is_valid():
            form.save()
            messages.success(request, 'Campus actualizado con éxito.')
            return redirect('listar_campus')
    else:
        form = CampusForms(instance=campus)
    return render(request, 'campus/editar_campus.html', {'form': form})


@admin_required
def eliminar_campus(request, pk):
    campus = get_object_or_404(Campus, pk=pk)
    if request.method == 'POST':
        campus.delete()
        messages.success(request, 'Campus eliminado con éxito.')
        return redirect('listar_campus')
    return render(request, 'campus/eliminar_campus.html', {'campus': campus})