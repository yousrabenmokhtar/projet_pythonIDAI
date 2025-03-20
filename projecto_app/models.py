from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from myApp.models import Utilisateur
#from django.db.models import Max  # Pour utiliser la fonction Max


# user est une clé étrangère (ForeignKey) faisant référence à un modèle d'utilisateur Django. 

# class Utilisateur(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     Nom_complet = models.CharField(max_length=100)
#     Email_utilisateur = models.EmailField(unique=True)
#     Password_utilisateur = models.CharField(max_length=100)
#     photo_profile = models.URLField(null=True, blank=True)
#     Description_profile = models.TextField(null=True, blank=True)
#     Etat_compte = models.CharField(max_length=50, default='active')  # Définition de l'état de compte par défaut
#     Etat_profile = models.CharField(max_length=50, default='public')  # Définition de l'état de profil par défaut
#     Nombre_amis = models.IntegerField(default=0)
#     Sexe_utilisateur = models.CharField(max_length=10)
#     role = models.CharField(max_length=100, default='user')  # Ajout de l'attribut "role"

#     def __str__(self):
#         return self.Nom_complet


class Education(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    nom_etablissement = models.CharField(max_length=100)  # Correction de la faute de frappe
    Diplome = models.CharField(max_length=100)
    Annees_Etudes = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.utilisateur.Nom_complet} - {self.Diplome} - {self.nom_etablissement}"

class Skills(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    nom_Skill = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nom_Skill

class Langues(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    Langue = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.Langue

class Experience(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    nom_experience = models.CharField(max_length=100)
    Lieu_fonctionnement = models.CharField(max_length=100, null=True)
    Duree_experience = models.CharField(max_length=100)
    description = models.TextField()
    date_experience = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom_experience


