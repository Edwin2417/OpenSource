# Sistema_Reservacion_Horas/views/usuarios.py
from django.shortcuts import render, redirect, get_object_or_404
from Sistema_Reservacion_Horas.models.aulas_model import Usuario
from Sistema_Reservacion_Horas.forms.usuario_form import UsuarioForms
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
def listar_usuario(request):
    query = request.GET.get('q', '')  # Obtiene la consulta de búsqueda
    if query:
        usuarios = Usuario.objects.filter(nombre__icontains=query)  # Filtra usuarios por nombre
    else:
        usuarios = Usuario.objects.all()  # Obtiene todos los usuarios si no hay consulta

    # Utiliza la función auxiliar para paginar
    page_obj = paginar_objetos(request, usuarios, 4)

    return render(request, 'usuarios/listar_usuario.html', {
        'page_obj': page_obj,  # Objeto paginado
        'query': query  # Mantener el término de búsqueda en la plantilla
    })


@admin_required
def agregar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')  # Asegúrate de que el nombre de la URL sea correcto
    else:
        form = UsuarioForms()
    return render(request, 'usuarios/agregar_usuario.html', {'form': form})

@admin_required
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

@admin_required
def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')  # Asegúrate de que el nombre de la URL sea correcto
    return render(request, 'usuarios/eliminar_usuario.html', {'usuario': usuario})
