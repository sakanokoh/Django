from django.db import models


# Create your models here.
class Voiture(models.Model):
    nom = models.CharField(max_length=250, default="")
    couleurs = models.CharField(max_length=250, default="")
    prix_moyen = models.CharField(max_length=250, default="")
    consommation_carburant = models.CharField(max_length=250, default="")
    technologie_securite = models.CharField(max_length=250, default="")
    confort_de_conduite = models.CharField(max_length=250, default="")
    espace_intérieur = models.CharField(max_length=250, default="")
    connectivité = models.CharField(max_length=250, default="")
    image = models.ImageField(upload_to="static/img_base")


    # def __str__(self) -> str:
    #     return f"{self.nom } : {self.prix_moyen}"
    
    class Meta:
        db_table = "Voiture" 
        verbose_name = "voiture"
        verbose_name_plural = "Voitures"


