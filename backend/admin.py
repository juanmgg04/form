from django.contrib import admin
from .models import Formulario
import csv
from django.http import HttpResponse

# Register your models here.

# admin.site.register(Formulario)

def exportar_csv(modeladmin, request, queryset):
    # Define el nombre del archivo
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="formularios.csv"'
    
    # Define los campos a exportar
    writer = csv.writer(response)
    writer.writerow([
        'Nombre',
        'Pregunta 1',
        'Pregunta 2',
        'Pregunta 3',
        'Pregunta 4',
        'Pregunta 5',
        'Pregunta 6',
        'Pregunta 7',
        'Pregunta 8',
        'Pregunta 9',
        'Pregunta 10',
        'Pregunta 11',
        'Pregunta 12',
        'Pregunta 13',
        'Pregunta 14',
        'Pregunta 15',
        'Fecha'
    ])
    
    # Escribe los datos del queryset
    for formulario in queryset:
        writer.writerow([
            formulario.nombre,
            formulario.pregunta_1,
            formulario.pregunta_2,
            formulario.pregunta_3,
            formulario.pregunta_4,
            formulario.pregunta_5,
            formulario.pregunta_6,
            formulario.pregunta_7,
            formulario.pregunta_8,
            formulario.pregunta_9,
            formulario.pregunta_10,
            formulario.pregunta_11,
            formulario.pregunta_12,
            formulario.pregunta_13,
            formulario.pregunta_14,
            formulario.pregunta_15,
            formulario.fecha,
        ])
    
    return response

exportar_csv.short_description = "Exportar seleccionados a CSV"

@admin.register(Formulario)
class FormularioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'pregunta_1', 'pregunta_2', 'pregunta_3', 'pregunta_4', 'pregunta_5', 'pregunta_6', 'pregunta_7', 'pregunta_8', 'pregunta_9', 'pregunta_10', 'pregunta_11', 'pregunta_12', 'pregunta_13', 'pregunta_14', 'pregunta_15', 'fecha']
    actions = [exportar_csv]