from django.shortcuts import render, redirect
from .models import Monotributo, Profesion, Vencimientos
from django.http import HttpResponse    
from .forms import monotributoForm, profesionForm, venciminetosForm
# Create your views here.


def inicio(request):
    return render(request,"AppCoder/inicio.html")
    
def monotributistas(request):
    if request.method=="POST":
        formulario_mono=monotributoForm(request.POST)
        if formulario_mono.is_valid():
            data= formulario_mono.cleaned_data
            monotributo= Monotributo(nombre=data["nombre"], apellido=data["apellido"], cuit=data["cuit"])
            monotributo.save()
            return redirect("monotributistas")

        
    else:
        formulario_mono=monotributoForm()
    monotributistas= Monotributo.objects.all()
    return render(request,"AppCoder/monotributo.html", {"formulario": formulario_mono})

def profesiones(request):
    if request.method=="POST":
        formulario_prof=profesionForm(request.POST)
        if formulario_prof.is_valid():
            dataP= formulario_prof.cleaned_data
            profesion= Profesion(actividad=dataP["actividad"], moneda=dataP["moneda"] , ingresos_brutos=dataP["ingresos_brutos"])
            profesion.save()
            return redirect ("profesiones")
    else:
        formulario_prof=profesionForm()
        return render(request, "AppCoder/profesion.html", {"FormP": formulario_prof})


def vencimientos_servicio(request):
    if request.method=="POST":
        formulario_venc=venciminetosForm(request.POST)
        if formulario_venc.is_valid():
            dataF= formulario_venc.cleaned_data
            vencimientos= Vencimientos(cuit=dataF["cuit"], fecha_vencimiento=dataF["fecha_vencimiento"] , pagaDeServicio=dataF["pagaDeServicio"])
            vencimientos.save()
            return redirect ("vencimientos_servicio")
    else:
        formulario_venc=venciminetosForm()
        return render(request, "AppCoder/venc.html", {"FormF": formulario_venc})


def busquedaDatos(request):
    return render(request,"AppCoder/busquedaDatos.html")

def resultadosBusqueda(request):
    cuit=request.GET['cuit']
    if cuit != "":
        datos=Vencimientos.objects.filter(cuit_icontains=cuit)
        return render(request,"AppCoder/resultadosBusqueda.html", {"cuit": cuit})
    else:
        return render(request,"AppCoder/busquedaDatos.html", {"mensaje": "debe ingresar datos para la busqueda!"})


        