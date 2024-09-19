from django.urls import path
from Sistema_Reservacion_Horas.views.home import home

urlpatterns = [
    path('', home, name='home'),
]