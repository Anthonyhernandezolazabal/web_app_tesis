from django.urls import path
from . import views
from web_admin.views import LoginFormViews,modulo_paciente
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('',LoginFormViews.as_view(),name='login'),
    path('home',login_required(views.Home),name='home'),
    path('usuarios',login_required(views.registro_usuario),name='usuarios'),
    path('historial_pacientes/',login_required(modulo_paciente.listar_paciente_historial),name='historial_pacientes'),
    path('registro_paciente/',login_required(modulo_paciente.listar_paciente_registro),name='registro_paciente')
]