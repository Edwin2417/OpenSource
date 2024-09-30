# Sistema_Reservacion_Horas/views/home.py
from django.shortcuts import render, redirect

def home(request):
    if not request.session.get('usuario_id'):
        return redirect('login')  # Redirige al login si no hay sesión
    return render(request, 'index.html')
