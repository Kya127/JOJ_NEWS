from django.contrib import admin
from .models import Categorie, Article,Commentaire

# Register your models here.

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('id','nom',)
    search_fields = ('nom',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre','contenu','date_publication')
    list_filter = ('categories', 'date_publication')
    search_fields = ('titre',)
    date_hierarchy = 'date_publication'


admin.site.register(Article,ArticleAdmin)


class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('article_commentaire','auteur_commentaire','texte_commentaire','date_commentaire')
    list_filter = ('article_commentaire', 'date_commentaire')
    search_fields = ('article_commentaire','auteur_commentaire')
    date_hierarchy = 'date_commentaire'
    
admin.register(Commentaire,CategorieAdmin)