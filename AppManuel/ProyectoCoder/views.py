from django.shortcuts import render
from .models import Monotributo, Profesion, Vencimientos
from django.http import HttpResponse    
from .forms import monoForm
# Create your views here.


def inicio(request):
    return render(request,"AppCoder/inicio.html")
    
def monotributistas(request):
    monotributistas= Monotributo.objects.all()
    return render(request,"AppCoder/monotributo.html", {"monotributistas": monotributistas})

def profesiones(request):
    return render(request,"AppCoder/profesion.html")

def vencimientos_servicio(request):
    return render(request,"AppCoder/venc.html")

def monoFormulario(request):
    if request.method=="POST":
        nombre= request.POST['nombre']
        apellido= request.POST['apellido']
        cuit= request.POST['cuit']
        vencimiento=  request.POST['vencimiento']
        monotributistas= Monotributo(nombre=nombre, apellido=apellido, cuit=cuit, vencimiento=vencimiento)
        monotributistas.save()
        return render(request, "AppCoder/monoFormulario.html", {"mensaje": "Datos Registrados"})
    else:
        formu_mono=monoForm()
        return render(request, "AppCoder/monoFormulario.html", {"formulario":formu_mono})

        