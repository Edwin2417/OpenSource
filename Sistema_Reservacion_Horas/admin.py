from django.contrib import admin
from Sistema_Reservacion_Horas.models.aulas_model import Campus, Edificios, TiposAulas, AulasLaboratorios

# Registra los modelos para que aparezcan en el panel de administración
admin.site.register(Campus)
admin.site.register(Edificios)
admin.site.register(TiposAulas)
admin.site.register(AulasLaboratorios)