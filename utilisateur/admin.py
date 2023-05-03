from django.contrib import admin
from utilisateur.models import Profile
from django.contrib.auth.models import Group


#@admin.register(Group)

# Register your models here.

@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ("name", "email", "phone")