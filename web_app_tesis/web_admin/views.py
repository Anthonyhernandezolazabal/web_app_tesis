from turtle import pos
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from web_admin.forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpRequest
from web_admin.models import pacientes
from rest_framework.views import APIView
from django.http import HttpResponse
"""=============================================
LOGIN
============================================="""
@login_required (login_url='home')
def Home(request):
  return render(request, 'layouts/inicio.html')

class LoginFormViews(LoginView):
  template_name = 'registration/acceso.html'

  def dispatch(self, request, *args, **kwargs):
      print('request.user :',request.user)
      if request.user.is_authenticated:
        id_user_login = request.session.get('_auth_user_id')
        username_user_login = request.user.username
        user_autenticate = request.user.is_authenticated
        params = {"id_user": id_user_login,'user_name':username_user_login,'user_autenticate':user_autenticate}
        return render(request,"layouts/inicio.html",params)
      return super().dispatch(request, *args, **kwargs)

  def get_context_data(self,**kwargs):
      context = super().get_context_data(**kwargs)
      context['title'] = 'Iniciar sesion'
      return context

"""=============================================
MÓDULO REGISTRO DE USUARIOS
============================================="""
def registro_usuario(request):

  if request.method == 'POST':

    form = CustomUserCreationForm(request.POST)

    if form.is_valid():
      form.save()

      username = form.cleaned_data['username']
      messages.success(request, f"Usuario {username} creado")

      return redirect('usuarios')

  else:

    form = CustomUserCreationForm
    usuariosAll = User.objects.all()

  context = {
    'form':form,
    'userall':usuariosAll
    }
  return render(request, 'layouts/register_user.html',context)

"""=============================================
MÓDULO PACIENTES
============================================="""
class modulo_paciente(HttpRequest):
  def listar_paciente_historial(request):
    pacientesall = pacientes.objects.all()
    context = {
      'allpacientes':pacientesall,
    }
    return render(request, 'layouts/historial.html',context)

  def listar_paciente_registro(request):
    return render(request, 'layouts/pacientes.html')

  def registrarPaciente(request):
    if request.GET['hist']:
      hist = request.GET.get('hist')
      dni = request.GET.get('dni')
      nombre_apellidos = request.GET.get('nombre_apellidos')
      genero = request.GET.get('genero')
      telefono = request.GET.get('telefono')
      edad = request.GET.get('edad')
      observaciones = request.GET.get('observaciones')
      id_medico_tratante_id = request.GET.get('id_medico_tratante_id')
      pac_r = pacientes(cod_historial_clinica=hist,dni=dni,nombre_apellidos=nombre_apellidos,genero=genero,id_medico_tratante_id=id_medico_tratante_id,telefono=telefono,edad=edad,observaciones=observaciones)
      pac_r.save()
      return HttpResponse(str('ok'))
    else:
      return HttpResponse(str('nook'))

  def validarDniPaciente(request):
    if request.GET['dni']:
      dni = request.GET.get('dni')
      pacientes.objects.get(dni=dni)
      return HttpResponse(str('ok'))

    else:

      return HttpResponse(str('nook'))

  def validartelPaciente(request):
    if request.GET['tel']:
      tel = request.GET.get('tel')
      pacientes.objects.get(telefono=tel)
      return HttpResponse(str('ok'))

    else:

      return HttpResponse(str('nook'))