from django.db import models
from django.contrib.auth.models import User
"""=============================================
PACIENTES
============================================="""
class pacientes(models.Model):
    cod_historial_clinica = models.CharField(max_length=11, verbose_name='Historial Clínica')
    dni = models.CharField(max_length=8, verbose_name='Dni paciente')
    nombre_apellidos = models.CharField(max_length=255, verbose_name='nombre y apellidos')
    observaciones = models.CharField(max_length=255, verbose_name='Observaciones', null=True)
    genero = models.BooleanField(default=True)
    telefono = models.CharField(max_length=9, verbose_name='Dni paciente', null=True)
    edad = models.CharField(max_length=2, verbose_name='Fecha Nacimiento', null=True)
    id_medico_tratante = models.ForeignKey(User,on_delete=models.SET_NULL, blank=True, null=True)
    registrado = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'pacientes'
        ordering = ['id'] #ordenar por ID
