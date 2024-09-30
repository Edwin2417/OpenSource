from django.shortcuts import render, redirect
from django.contrib import messages
from Sistema_Reservacion_Horas.forms.login_forms import LoginForm
from Sistema_Reservacion_Horas.models.aulas_model import Usuario

def login_view(request):
    # Verifica si ya hay un usuario logueado
    if request.session.get('usuario_id'):
        return redirect('home')  # Redirige al home si ya está logueado

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            password = form.cleaned_data['password']

            try:
                usuario = Usuario.objects.get(nombre=nombre)

                # Verifica si el usuario está activo
                if not usuario.estado:
                    messages.error(request, 'El usuario está inactivo. Contacte al administrador.')
                elif usuario.password == password:  # Usa un método seguro para comparar contraseñas
                    request.session['usuario_id'] = usuario.identificador
                    return redirect('home')
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
