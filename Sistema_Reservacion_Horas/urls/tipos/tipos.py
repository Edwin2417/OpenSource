from django.urls import path
from Sistema_Reservacion_Horas.views.tipos.tipo_aula import listar_tipo_aula, agregar_tipo_aula, editar_tipo_aula, eliminar_tipo_aula

urlpatterns = [
    path('/', listar_tipo_aula, name='listar_tipo_aula'),
    path('/agregar/', agregar_tipo_aula, name='agregar_tipo_aula'),
    path('/editar/<int:pk>/', editar_tipo_aula, name='editar_tipo_aula'),
    path('/eliminar/<int:pk>/', eliminar_tipo_aula, name='eliminar_tipo_aula'),
]
