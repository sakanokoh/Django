from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django_countries.fields import CountryField
# from django_countries.widgets import CountrySelect

# Formulaire d' authentification
class LoginForm(AuthenticationForm):
    username = forms.CharField(label = "Nom d'utilisateur", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Veuillez entrer votre nom d\'utilisateur'}))
    
    password = forms.CharField(label = "Mot de passe", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Veuillez entrer votre mot de passe'}))



# formulaires d'inscription
class InscriptionForm1(UserCreationForm):
    name = forms.CharField(label="Nom complet", widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'Veuillez entrer votre nom'}))
    
    username = forms.CharField(label="Nom d\'utilisateur", widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'Veuillez entrer votre nom d\'utilisateur'}))
    
    email = forms.CharField(label="Email", widget=forms.EmailInput(
        attrs={'class': 'form-control','placeholder': 'Veuillez entrer votre email'}))
    
    phone = forms.IntegerField(label="Numéro de téléphone", widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'Veuillez entrer votre tel'}))
    
    password1 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(
        attrs={'class': 'form-control','placeholder': 'Veuillez entrer votre mdp'}))
    
    password2 = forms.CharField(label="Confirmation mot de passe", widget=forms.PasswordInput(
        attrs={'class': 'form-control','placeholder': 'Veuillez entrer votre mdp'}))
    
    class Meta:
        model = Profile
        fields = ("name", "username", "email", "phone", "password1", "password2")
  



class InscriptionForm2(forms.ModelForm):
    country = CountryField().formfield(widget=forms.Select(
        attrs={'class': 'form-control','placeholder': 'Veuillez entrer votre pays'}))
    
    city = forms.CharField(label="ville", widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'Veuillez entrer votre ville'}))
    
    address = forms.CharField(label="adresse", widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'Veuillez entrer votre adresse'}))
    
    postal = forms.IntegerField(label="code postal", widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'Veuillez entrer code postal'}))
    
    class Meta:
        model = Profile
        fields = ("country", "city", "address", "postal")

    




