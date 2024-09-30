from django.shortcuts import render, redirect
from Sistema_Reservacion_Horas.models.aulas_model import Usuario


def home(request):
    usuario_id = request.session.get('usuario_id')  # Obtiene el ID del usuario de la sesión
    usuario = None

    if not usuario_id:
        return redirect('login')  # Redirige al login si no hay sesión

    try:
        usuario = Usuario.objects.get(identificador=usuario_id)
    except Usuario.DoesNotExist:
        pass  # Manejo del caso si el usuario no se encuentra

    return render(request, 'index.html', {'usuario': usuario})
