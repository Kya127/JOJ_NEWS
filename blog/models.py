from django.db import models
from django.contrib.auth.models import User

# Signal pour notifier l'admin lors de la création d'un commentaire
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

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
    
    
class Commentaire(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="commentaires",
    )
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date_creation"]
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"

    def __str__(self):
        return f"Commentaire de {self.auteur} sur {self.article}"
    

# Signal pour notifier l'admin lors de la création d'un commentaire
@receiver(post_save, sender=Commentaire)
def notifier_nouveau_commentaire(sender, instance, created, **kwargs):
    if created:
        sujet = f"Nouveau commentaire sur : {instance.article.titre}"
        message = f"Un nouveau commentaire a été ajouté par {instance.auteur.username} sur l'article '{instance.article.titre}'.\n\n"
        message += f"Contenu du commentaire :\n{instance.contenu}\n\n"
        message += f"Lien vers l'article : /articles/{instance.article.id}/"
        
        # Envoyer l'email à l'admin configuré
        admin_email = "fassane348@gmail.com"
        send_mail(
            sujet,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [admin_email],
            fail_silently=False,
        )
