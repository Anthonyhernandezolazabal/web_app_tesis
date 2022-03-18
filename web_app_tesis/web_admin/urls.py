from django.urls import path
from . import views
from web_admin.views import LoginFormViews
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('',LoginFormViews.as_view(),name='login'),
    path('home',login_required(views.Home),name='home'),
    path('usuarios',login_required(views.registro_usuario),name='usuarios'),
]