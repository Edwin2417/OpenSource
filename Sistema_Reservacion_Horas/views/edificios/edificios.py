from django.shortcuts import render, get_object_or_404, redirect
from Sistema_Reservacion_Horas.models.aulas_model import Edificios
from Sistema_Reservacion_Horas.forms.edificios_form import EdificiosForms

# Vista para listar los tipos de aula
def listar_edificio(request):
    edificios = Edificios.objects.all()
    return render(request, 'edificios/listar_edificios.html', {'edificios': edificios})

def agregar_edificio(request):
    if request.method == 'POST':
        form = EdificiosForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_edificios')
    else:
        form = EdificiosForms()
    return render(request, 'edificios/agregar_edificios.html', {'form': form})

def editar_edificio(request, pk):
    edificio = get_object_or_404(Edificios, pk=pk)
    if request.method == 'POST':
        form = EdificiosForms(request.POST, instance=edificio)
        if form.is_valid():
            form.save()
            return redirect('listar_edificios')
    else:
        form = EdificiosForms(instance=edificio)
    return render(request, 'edificios/editar_edificios.html', {'form': form})

def eliminar_edificio(request, pk):
    edificio = get_object_or_404(Edificios, pk=pk)
    if request.method == 'POST':
        edificio.delete()
        return redirect('listar_edificios')
    return render(request, 'edificios/eliminar_edificios.html', {'edificio': edificio})

