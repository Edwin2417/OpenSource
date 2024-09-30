from django.urls import path
from Sistema_Reservacion_Horas.views.usuarios import listar_usuario, agregar_usuario, editar_usuario, eliminar_usuario

urlpatterns = [
    path('/', listar_usuario, name='listar_usuarios'),
    path('/agregar/', agregar_usuario, name='agregar_usuario'),
    path('/editar/<int:pk>/', editar_usuario, name='editar_usuario'),
    path('/eliminar/<int:pk>/', eliminar_usuario, name='eliminar_usuario'),
]
