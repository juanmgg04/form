from django.db import models
from django import forms

# Create your models here.
class Formulario(models.Model):
    nombre = models.CharField(max_length=100)
    pregunta_1 = models.IntegerField()
    pregunta_2 = models.IntegerField()
    pregunta_3 = models.IntegerField()
    pregunta_4 = models.IntegerField()
    pregunta_5 = models.IntegerField()
    pregunta_6 = models.IntegerField()
    pregunta_7 = models.IntegerField()
    pregunta_8 = models.IntegerField()
    pregunta_9 = models.CharField(max_length=100)
    pregunta_10 = models.CharField(max_length=100)
    pregunta_11 = models.CharField(max_length=100)
    pregunta_12 = models.CharField(max_length=100)
    pregunta_13 = models.CharField(max_length=100)
    pregunta_14 = models.CharField(max_length=100)
    pregunta_15 = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Formulario'
        verbose_name_plural = 'Formularios'