from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django import forms

from .models import *

def index(request):
    latest_escuderies_list = Escuderia.objects.order_by("nom")[:5]
    context = {"latest_escuderies_list": latest_escuderies_list}
    return render(request, "index.html", context)

def escuderia(request, escuderia_nom):
    escuderia = get_object_or_404(Escuderia, pk=escuderia_nom)
    return render(request, "escuderia.html", {"escuderia": escuderia})

class EscuderiaForm(forms.ModelForm):
    class Meta:
        model = Escuderia
        exclude = ()

def crea_escuderia(request):
    form = EscuderiaForm()

    # si hi ha dades, les processem
    if request.method == "POST":
        form = EscuderiaForm(request.POST)
        if form.is_valid():
            escuderia = Escuderia.objects.filter(nom=form.cleaned_data.get("nom"))
            if escuderia.count()>0:
                return HttpResponse("ERROR: el nom de l'equip ja existeix.")
            form.save()

    # creem form si no hi ha dades
    return render(request,"crea_equip.html",{
        "form":form,
        })

