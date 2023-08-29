from django import forms


class monotributoForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    cuit=forms.IntegerField()

class profesionForm(forms.Form):
    actividad=forms.CharField(max_length=50)
    moneda=forms.CharField(max_length=50)
    ingresos_brutos=forms.IntegerField()

class venciminetosForm(forms.Form):
    cuit=forms.IntegerField()
    fecha_vencimiento=forms.DateField()
    pagaDeServicio=forms.BooleanField()
