from django.shortcuts import render, redirect, get_object_or_404
from Sistema_Reservacion_Horas.models.aulas_model import Empleado  # Asegúrate de que el modelo Empleado esté correctamente importado
from Sistema_Reservacion_Horas.forms.empleados_form import EmpleadosForms  # Asegúrate de que la ruta sea correcta
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

@admin_required
def listar_empleados(request):
    query = request.GET.get('q', '')  # Obtiene la consulta de búsqueda
    if query:
        empleados = Empleado.objects.filter(nombre__icontains=query)  # Filtra empleados por nombre
    else:
        empleados = Empleado.objects.all()  # Obtiene todos los empleados si no hay consulta

    page_obj = paginar_objetos(request, empleados, 4)

    return render(request, 'empleados/listar_empleados.html', {'page_obj': page_obj, 'empleados': empleados})

@admin_required
def agregar_empleados(request):
    if request.method == 'POST':
        form = EmpleadosForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_empleados')  # Asegúrate de que el nombre de la URL sea correcto
    else:
        form = EmpleadosForms()
    return render(request, 'empleados/agregar_empleados.html', {'form': form})

@admin_required
def editar_empleados(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        form = EmpleadosForms(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('listar_empleados')  # Asegúrate de que el nombre de la URL sea correcto
    else:
        form = EmpleadosForms(instance=empleado)
    return render(request, 'empleados/editar_empleados.html', {'form': form})

@admin_required
def eliminar_empleados(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('listar_empleados')  # Asegúrate de que el nombre de la URL sea correcto
    return render(request, 'empleados/eliminar_empleados.html', {'empleado': empleado})
