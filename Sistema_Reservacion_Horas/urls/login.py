from django.urls import path
from Sistema_Reservacion_Horas.views.login import login_view

urlpatterns = [
    path('', login_view, name='login'),
]