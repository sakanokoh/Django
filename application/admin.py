from django.contrib import admin
from .models import *

# Register your models here.
#admin.site.register(DepartementModel)


@admin.register(Voiture)
class Voiture(admin.ModelAdmin):
    list_display = ("nom", "prix_moyen")



admin.site.site_title = " Authentification pour le site de MK-auto"
admin.site.index_title = " Les models site d'administration de MK-auto"
admin.site.site_header = " Site d'administration de MK-auto"