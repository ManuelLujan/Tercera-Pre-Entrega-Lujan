from django.shortcuts import render
from .models import Monotributo, Profesion, Vencimientos
from django.http import HttpResponse    
from .forms import monotributoForm
# Create your views here.


def inicio(request):
    return render(request,"AppCoder/inicio.html")
    
def monotributistas(request):
    if request.method=="POST":

        pass
    else:
        formulario_mono=monotributoForm()
    monotributistas= Monotributo.objects.all()
    return render(request,"AppCoder/monotributo.html", {"formulario": formulario_mono})

def profesiones(request):
    return render(request,"AppCoder/profesion.html")

def vencimientos_servicio(request):
    return render(request,"AppCoder/venc.html")



        