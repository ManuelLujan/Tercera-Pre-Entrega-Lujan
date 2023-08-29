from django.urls import path
from .views import *

urlpatterns = [
    path('monotributistas/', monotributistas, name="monotributistas"),
    path('vencimientos_servicio/', vencimientos_servicio, name= "vencimientos_servicio"),
    path('profesiones/', profesiones, name="profesiones"),
    path('monoFormulario/', monoFormulario, name="monoFormulario"),
]
