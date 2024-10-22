from django.shortcuts import render, redirect
from django.contrib import messages
from Sistema_Reservacion_Horas.forms.login_forms import LoginForm
from Sistema_Reservacion_Horas.models.aulas_model import Usuario
import time

def login_view(request):
    if request.session.get('usuario_id'):
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            no_carnet = form.cleaned_data['no_carnet']
            password = form.cleaned_data['password']

            try:
                usuario = Usuario.objects.get(no_carnet=no_carnet)

                if not usuario.estado:
                    messages.error(request, 'El usuario está inactivo. Contacte al administrador.')
                elif usuario.password == password:
                    request.session['usuario_id'] = usuario.identificador
                    request.session['tipo_usuario'] = usuario.tipo_usuario.descripcion
                    return render(request, 'redirect.html')  # Renderiza la página de redirección
                else:
                    messages.error(request, 'Contraseña incorrecta. Intente de nuevo.')

            except Usuario.DoesNotExist:
                messages.error(request, 'El usuario no está registrado. Intente de nuevo.')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    request.session.flush()
    return redirect('login')
