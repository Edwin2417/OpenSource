from django.urls import path
from Prueba.views.aulas import listar_aulas, agregar_aula, editar_aula, eliminar_aula

urlpatterns = [
    path('', listar_aulas, name='listar_aulas'),
    path('agregar/', agregar_aula, name='agregar_aula'),
    path('editar/<int:pk>/', editar_aula, name='editar_aula'),
    path('eliminar/<int:pk>/', eliminar_aula, name='eliminar_aula'),
]
