# Sistema_Reservacion_Horas/views/usuarios.py
from django.shortcuts import render, redirect, get_object_or_404
from Sistema_Reservacion_Horas.models.aulas_model import Usuario
from Sistema_Reservacion_Horas.forms.usuario_form import UsuarioForms

def listar_usuario(request):
    query = request.GET.get('q', '')  # Obtiene la consulta de búsqueda
    if query:
        usuarios = Usuario.objects.filter(nombre__icontains=query)  # Filtra usuarios por nombre
    else:
        usuarios = Usuario.objects.all()  # Obtiene todos los usuarios si no hay consulta

    return render(request, 'usuarios/listar_usuario.html', {'usuarios': usuarios})

def agregar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')  # Asegúrate de que el nombre de la URL sea correcto
    else:
        form = UsuarioForms()
    return render(request, 'usuarios/agregar_usuario.html', {'form': form})

def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForms(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')  # Asegúrate de que el nombre de la URL sea correcto
    else:
        form = UsuarioForms(instance=usuario)
    return render(request, 'usuarios/editar_usuario.html', {'form': form})

def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')  # Asegúrate de que el nombre de la URL sea correcto
    return render(request, 'usuarios/eliminar_usuario.html', {'usuario': usuario})
