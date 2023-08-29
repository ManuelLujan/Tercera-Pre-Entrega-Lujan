from django import forms


class monoForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    cuit=forms.IntegerField()
    vencimiento=forms.IntegerField()