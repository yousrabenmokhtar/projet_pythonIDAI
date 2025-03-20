from django.db import models
from django.contrib.auth.models import User
from .models import *
from PIL import Image
from django.core.validators import FileExtensionValidator
# Create your models here.

class Utilisateur(models.Model):
    CHOIX_ETAT_COMPTE = [
        ('active', 'Active'),
        ('bloque', 'Bloqué'),
        ('banni', 'Banni'),
    ]
    CHOIX_ETAT_PROFILE = [
        ('publique', 'Publique'),
        ('privee', 'Privée'),
    ]

    user = models.OneToOneField(User, related_name='utilisateur', null=True, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self" , blank=True, symmetrical=False, related_name="followed_By")
    Nom_complet = models.CharField(max_length=100 , blank=True , null=True)
    Email_utilisateur = models.EmailField(max_length=100 , blank=True , null=True)
    Password_utilisateur = models.CharField(max_length=100 , blank=True , null=True)
    photo_profile = models.ImageField(upload_to='images/images/', default='images/images/defaultImage.jpg',blank=True, null=True)
    Description_profile  = models.TextField(max_length = 400 , null=True)
    Etat_compte = models.CharField(max_length=50, choices=CHOIX_ETAT_COMPTE, default='active')
    Etat_profile = models.CharField(max_length=50, choices=CHOIX_ETAT_PROFILE, default='publique')
    Nombre_amis = models.IntegerField(default=0)
    user_type = models.CharField(max_length=50, blank=True)  
    bio = models.TextField(null=True, blank=True)
    image_back = models.ImageField(null=True, blank=True, upload_to="images/images/" , default='images/images/grey_pic.jpg')

    def __str__(self):  
        return self.user.username
    


class PublicationManager(models.Manager):
    def get_all_publications(self):
        return self.all()

from django.db import models
from PIL import Image

class Publication(models.Model):
    auteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    image_publication = models.ImageField(upload_to='publication_images', null=True, blank=True  )
    video_publication = models.FileField(upload_to='publication_videos/', null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'pdf', 'doc', 'docx', 'mp4', 'avi', 'mov'])
    ])

    document_publication = models.FileField(upload_to='publication_documents/', null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])
    ])
    Etat_publication = models.CharField(max_length=50, default='Active')
    Nombre_like = models.IntegerField(default=0)
    Nombre_partage = models.IntegerField(default=0)

    objects = PublicationManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image_publication:
            img = Image.open(self.image_publication.path)
            max_width = 560
            max_height = 370

            # Redimensionner l'image en conservant le rapport d'aspect
            img.thumbnail((max_width, max_height))

            # Enregistrer l'image redimensionnée
            img.save(self.image_publication.path)






class Commentaire(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    contenu_commentaire = models.TextField()
    date_commentaire = models.DateTimeField(auto_now_add=True)



# class Follow(models.Model):
#     follower = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='follower')
#     following = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='following')

#     def user_follow(sender, instance, *args, **kwargs):
#         follow = instance
#         sender = follow.follower
#         following = follow.following

#     def user_unfollow(sender, instance, *args, **kwargs):
#         follow = instance
#         sender = follow.follower
#         following = follow.following
    

class Likes(models.Model):

    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    post = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name="post_likes")
