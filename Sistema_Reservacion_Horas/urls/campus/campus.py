from django.urls import path
from Sistema_Reservacion_Horas.views.campus import listar_campus, agregar_campus, editar_campus, eliminar_campus

urlpatterns = [
    path('/', listar_campus, name='listar_campus'),
    path('/agregar/', agregar_campus, name='agregar_campus'),
    path('/editar/<int:pk>/', editar_campus, name='editar_campus'),
    path('/eliminar/<int:pk>/', eliminar_campus, name='eliminar_campus'),
    # Añade las URLs para Edificios y Usuario
]
