# Signal pour notifier l'admin lors de la création d'un commentaire
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Commentaire


# Signal pour notifier l'admin lors de la création d'un commentaire
@receiver(post_save, sender=Commentaire)
def notifier_nouveau_commentaire(sender, instance, created, **kwargs):
    if created:
        sujet = f"Nouveau commentaire sur : {instance.article.titre}"
        message = f"Un nouveau commentaire a été ajouté par {instance.auteur.username} sur l'article '{instance.article.titre}'.\n\n"
        message += f"Contenu du commentaire :\n{instance.contenu}\n\n"
        message += f"Lien vers l'article : /articles/{instance.article.id}/"
        
        # Email de l'expéditeur = email de l'utilisateur qui commente
        # Si l'utilisateur n'a pas d'email, utiliser l'email par défaut
        from_email = instance.auteur.email if instance.auteur.email else settings.DEFAULT_FROM_EMAIL
        
        # Envoyer l'email à l'admin configuré
        admin_email = "fassane348@gmail.com"
        send_mail(
            sujet,
            message,
            from_email,  # Email de l'utilisateur qui commente
            [admin_email],
            fail_silently=False, # Ne pas afficher d'erreur si l'envoi échoue
        )
