from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Voiture

@login_required(login_url='utilisateur:choix')
def model(request):
    voitures = Voiture.objects.all()
    voiture=voitures[0]
    return render(request,"index.html",{"voiture":voiture})
##TEST

@login_required
def voiture(request,index:int=0):
    voitures = Voiture.objects.all()
    voiture=voitures[index]
    return render(request,"index.html",{"voiture":voiture})

def suiv(request,pk:int):
    voitures = Voiture.objects.all()
    voiture = Voiture.objects.get(id=pk)
    i = list(voitures).index(voiture)
    indice = i
    if i<len(voiture)-1:
        indice+=1
    else:
        indice=0 
    return redirect("application:voit",index=indice)

def prec(request, pk:int):
    voitures = Voiture.objects.all()
    voiture = Voiture.objects.get(id=pk)
    i = list(voitures).index(voiture)
    indice = i
    indice-=1 if 0<i else -(len(voitures)-1)
    return redirect("application:voit",index=indice)

    