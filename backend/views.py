from django.shortcuts import render, redirect
from .models import Formulario
from .forms import FormularioForm
# Create your views here.

def formulario_view(request):
    # form = Formulario()
    data = {
        'form': FormularioForm()
    }

    if request.method == 'POST':
        formulario = FormularioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            print("Formulario guardado")
        else:
            data["form"] = formulario
    return render(request, 'formulario.html', data)
    # if request.method == 'POST':
    #     formulario = FormularioForm(request.POST)
    #     if formulario.is_valid():
    #         formulario.save()
    #         print("Formulario guardado")
    # else:
    #     formulario = FormularioForm()
    # return render(request, 'formulario.html', {'formulario': formulario})

# def thank_you_view(request):
#     return render(request, 'thank_you.html')