from django.shortcuts import HttpResponse, render
from ejemplo.models import Familiar
from ejemplo.forms import Buscar, FamiliarForm
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView


def saludo(request):
    return HttpResponse("Este es un saludo")

def saludar_a(request, nombre):
    return HttpResponse(f"Hola como estas {nombre}")


def index(request):
    return render(request, "ejemplo/saludar.html", 
        {
            "nombre":"Christian",
            "apellido":" Porcel de Peralta",
        })

def mostrar_mi_template(request):
    return render (request, "ejemplo/index.html")


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

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class FamiliarList(ListView):
  model = Familiar

class FamiliarCrear(CreateView):
  model = Familiar
  success_url = "/panel-familia"
  fields = ["nombre", "direccion", "numero_pasaporte"]

class FamiliarBorrar(DeleteView):
  model = Familiar
  success_url = "/panel-familia"

class FamiliarActualizar(UpdateView):
  model = Familiar
  success_url = "/panel-familia"
  fields = ["nombre", "direccion", "numero_pasaporte"]
