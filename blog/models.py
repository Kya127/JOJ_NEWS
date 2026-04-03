from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
    
class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    auteur = models.ForeignKey(User,on_delete=models.CASCADE)
    categories = models.ForeignKey(Categorie,on_delete=models.CASCADE)

    def __str__(self):
        return self.titre
    