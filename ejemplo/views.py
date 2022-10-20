from django.shortcuts import render
from ejemplo.models import Familiar
from ejemplo.forms import Buscar
from django.views import View

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

class BuscarFamiliar(View):

    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})