from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from Sistema_Reservacion_Horas.models.aulas_model import Campus
from Sistema_Reservacion_Horas.forms.campus_forms import CampusForms

# Campus CRUD
def listar_campus(request):
    campus = Campus.objects.all()
    return render(request, 'campus/listar_campus.html', {'campus': campus})

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

def eliminar_campus(request, pk):
    campus = get_object_or_404(Campus, pk=pk)
    if request.method == 'POST':
        campus.delete()
        messages.success(request, 'Campus eliminado con éxito.')
        return redirect('listar_campus')
    return render(request, 'campus/eliminar_campus.html', {'campus': campus})