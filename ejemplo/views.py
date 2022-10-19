from django.shortcuts import render

def index(request):
    return render(request, "ejemplo/saludar.html", 
        {
            "nombre":"Christian",
            "apellido":" Porcel de Peralta",
        })

def imc(request, peso, altura):
    imc = peso / (altura*altura)
    peso = 74
    altura = 170
    return render(request, "ejemplo/imc.html", {"imc": imc}),