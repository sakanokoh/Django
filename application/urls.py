from django.contrib import admin
from django.urls import path, re_path
from .views import voiture, suiv, prec, model

app_name = "application"

urlpatterns = [
    #path('index/',index, name="ind"),
    path('voiture/',model, name="model"),
    path('voiture/<int:index>',voiture, name="voit"),
    path('suivant/<int:pk>',suiv, name="suivant"),
    path('precedent/<int:pk>',prec, name="precedent"),
]
