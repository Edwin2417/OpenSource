from django.urls import path
from Sistema_Reservacion_Horas.views.empleados.empleados import listar_empleados, agregar_empleados, editar_empleados, eliminar_empleados

urlpatterns = [
    path('/', listar_empleados, name='listar_empleados'),
    path('/agregar/', agregar_empleados, name='agregar_empleados'),
    path('/editar/<int:pk>/', editar_empleados, name='editar_empleados'),
    path('/eliminar/<int:pk>/', eliminar_empleados, name='eliminar_empleados'),
]
