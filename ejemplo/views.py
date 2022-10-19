from django.shortcuts import render
from ejemplo.models import Familiar

def index(request):
    return render(request, "ejemplo/saludar.html", 
        {
            "nombre":"Christian",
            "apellido":" Porcel de Peralta",
        })

def imc(request, peso, altura):
    altura_en_metros = altura / 100
    peso_en_kilos = peso / 100
    imc = peso_en_kilos / altura_en_metros * altura_en_metros # calcular el imc
    return render(request, "ejemplo/imc.html", {"imc": imc})


def monstrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "ejemplo/familiares.html", 
                {"lista_familiares": lista_familiares})