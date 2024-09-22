from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Sistema_Reservacion_Horas.urls.home')),
    path('aulas/', include('Sistema_Reservacion_Horas.urls.aulas.aulas')),
    path('tipos_aulas/', include('Sistema_Reservacion_Horas.urls.tipos.tipos')),
]
