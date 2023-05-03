from django.urls import path, re_path
from .views import choix, inscrire1, inscrire2, profile
from django.contrib.auth.views import LoginView
from .forms import LoginForm

app_name = "utilisateur"

urlpatterns = [
    path('choix/',choix, name="choix"),
    path('login/',LoginView.as_view(template_name = "login.html", redirect_authenticated_user=True, authentication_form = LoginForm), name="login"),
    path('inscrire1', inscrire1, name="inscrire1"),
    path('inscrire2', inscrire2, name="inscrire2"),
    path('profile', profile, name="profile"),

]