from django.shortcuts import render
from .models import Monotributo, Profesion, Vencimientos
from django.http import HttpResponse    
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