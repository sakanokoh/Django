from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.

class Profile(User):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    postal = models.IntegerField()
    country = CountryField()

    class Meta:
        db_table = "Profile" 
        verbose_name = "profile"
        verbose_name_plural = "Profiles"
