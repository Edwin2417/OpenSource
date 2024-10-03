from django.shortcuts import render, redirect
from Sistema_Reservacion_Horas.models.aulas_model import Usuario


def home(request):
    usuario_id = request.session.get('usuario_id')
    tipo_usuario = request.session.get('tipo_usuario')

    if not usuario_id:
        return redirect('login')  # Redirige al login si no hay sesión

    try:
        usuario = Usuario.objects.get(identificador=usuario_id)
    except Usuario.DoesNotExist:
        return redirect('login')

    # Renderiza la página principal con el usuario y el tipo de usuario
    return render(request, 'index.html', {'usuario': usuario, 'tipo_usuario': tipo_usuario})

