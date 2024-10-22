from django.urls import path
from Sistema_Reservacion_Horas.views.proceso_reservacion.proceso_reservacion import listar_reservaciones, agregar_reservacion, editar_reservacion, eliminar_reservacion

urlpatterns = [
    path('/', listar_reservaciones, name='listar_reservaciones'),
    path('/agregar/', agregar_reservacion, name='agregar_reservacion'),
    path('/editar/<int:pk>/', editar_reservacion, name='editar_reservacion'),
    path('/eliminar/<int:pk>/', eliminar_reservacion, name='eliminar_reservacion'),
]
