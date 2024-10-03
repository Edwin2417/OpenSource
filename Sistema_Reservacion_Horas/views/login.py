from django.shortcuts import render, redirect
from django.contrib import messages
from Sistema_Reservacion_Horas.forms.login_forms import LoginForm
from Sistema_Reservacion_Horas.models.aulas_model import Usuario

def login_view(request):
    if request.session.get('usuario_id'):
        return redirect('home')  # Redirige al home si ya está logueado

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            no_carnet = form.cleaned_data['no_carnet']  # Cambia 'nombre' por 'no_carnet'
            password = form.cleaned_data['password']

            try:
                # Busca al usuario por el número de carnet
                usuario = Usuario.objects.get(no_carnet=no_carnet)

                # Verifica si el usuario está activo
                if not usuario.estado:
                    messages.error(request, 'El usuario está inactivo. Contacte al administrador.')
                elif usuario.password == password:  # Asegúrate de usar un método seguro para comparar contraseñas
                    request.session['usuario_id'] = usuario.identificador
                    request.session['tipo_usuario'] = usuario.tipo_usuario.descripcion  # Guardamos el tipo de usuario
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
