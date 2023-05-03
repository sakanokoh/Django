from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import InscriptionForm1, InscriptionForm2
from .models import Profile

#TEST
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

# La vue pour choisir entre inscription et authentification
def choix(resquest):
    return render(resquest,"choix.html")

#Les vue d'inscription
def inscrire1(request):
    if request.method == 'POST':        
        form1 = InscriptionForm1(request.POST)
        if form1.is_valid():
            form1.cleaned_data['password'] = form1.cleaned_data['password1']
            del form1.cleaned_data['password1']
            del form1.cleaned_data['password2']
            request.session['signup_data'] = form1.cleaned_data
            return redirect("utilisateur:inscrire2")
    else:
        form1 = InscriptionForm1()
    return render(request,"inscription1.html", {"form": form1})


def inscrire2(request):
    signup_data = request.session.get('signup_data', {})
    print(signup_data)
    if not signup_data:
        return redirect('utilisateur:inscrire1')
    if request.method == 'POST':        
        form2 = InscriptionForm2(request.POST)
        if form2.is_valid(): 
            print("NEW POST")           
            user_data = {**signup_data, **form2.cleaned_data}
            print(user_data)
            Profile.objects.create_user(**user_data)
            del request.session['signup_data']
            return redirect('utilisateur:login')
    else:
        form2 = InscriptionForm2()
    return render(request, 'inscription2.html', {'form': form2})


# La vue pour afficher les profiles
@login_required(login_url='utilisateur:choix')
def profile(request):
    user_actu = request.user
    if user_actu.is_superuser:
        return render(request,"profile.html",{"profil": request.user})
    id = user_actu.id
    navigateur = Profile.objects.get(pk=id)
    return render(request,"profile.html",{"profil": navigateur})




