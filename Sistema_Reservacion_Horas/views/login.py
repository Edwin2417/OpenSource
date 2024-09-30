from django.shortcuts import render, redirect
from django.contrib import messages
from Sistema_Reservacion_Horas.forms.login_forms import LoginForm
from Sistema_Reservacion_Horas.models.aulas_model import Usuario

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            password = form.cleaned_data['password']

            try:
                # Cambia 'Nombre' a 'nombre'
                usuario = Usuario.objects.get(nombre=nombre)

                # Aquí, verifica la contraseña
                if usuario.password == password:  # Considera usar un método seguro para comparar contraseñas
                    # Si se encuentra, guarda el ID del usuario en la sesión
                    request.session['usuario_id'] = usuario.identificador
                    return redirect('home')  # Redirige al home
                else:
                    messages.error(request, 'Contraseña incorrecta. Intente de nuevo.')

            except Usuario.DoesNotExist:
                messages.error(request, 'El usuario no está registrado. Intente de nuevo.')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
