from django.urls import path
from . import views
from web_admin.views import LoginFormViews,modulo_paciente
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('',LoginFormViews.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    path('home',login_required(views.Home),name='home'),
    path('usuarios',login_required(views.registro_usuario),name='usuarios'),
    path('historial_pacientes/',login_required(modulo_paciente.listar_paciente_historial),name='historial_pacientes'),
    path('registro_paciente/',login_required(modulo_paciente.listar_paciente_registro),name='registro_paciente'),


    path('registrar_paciente/',login_required(modulo_paciente.registrarPaciente),name='registrar_paciente'),
    path('validar_dni/',login_required(modulo_paciente.validarDniPaciente),name='validar_dni'),
    path('validar_telef/',login_required(modulo_paciente.validartelPaciente),name='validar_telef')


]