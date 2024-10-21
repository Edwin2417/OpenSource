from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('Sistema_Reservacion_Horas.urls.home')),

    path('', include('Sistema_Reservacion_Horas.urls.login')),
    path('aulas/', include('Sistema_Reservacion_Horas.urls.aulas.aulas')),
    path('tipos_aulas/', include('Sistema_Reservacion_Horas.urls.tipos.tipos')),

    path('campus/', include('Sistema_Reservacion_Horas.urls.campus.campus')),

    path('edificios/', include('Sistema_Reservacion_Horas.urls.edificios.edificios')),

    path('usuarios/', include('Sistema_Reservacion_Horas.urls.usuarios.usuarios')),

    path('empleados/', include('Sistema_Reservacion_Horas.urls.empleados.empleados')),
]
