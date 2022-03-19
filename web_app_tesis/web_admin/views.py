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
        return redirect('home')
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