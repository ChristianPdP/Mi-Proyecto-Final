from django.shortcuts import render

def index(request):
    return render(request, "ejemplo/saludar.html", 
        {
            "nombre":"Christian",
            "apellido":" Porcel de Peralta",
        })

def imc(request, peso, altura):
    imc = 1 # calcular el imc
    return render(request, "ejemplo/imc.html", {"imc": imc}),