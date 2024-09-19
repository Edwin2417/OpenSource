# Sistema_Reservacion_Horas/views/home.py
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
