from django.urls import path
from Sistema_Reservacion_Horas.views.edificios.edificios import listar_edificio, agregar_edificio, editar_edificio, eliminar_edificio

urlpatterns = [
    path('/', listar_edificio, name='listar_edificios'),
    path('/agregar/', agregar_edificio, name='agregar_edificio'),
    path('/editar/<int:pk>/', editar_edificio, name='editar_edificio'),
    path('/eliminar/<int:pk>/', eliminar_edificio, name='eliminar_edificio'),
]
