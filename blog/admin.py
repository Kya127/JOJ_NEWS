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
    list_display = ("article", "auteur", "date_creation")
    list_filter = ("date_creation",)
    search_fields = ('article','auteur')
    date_hierarchy = 'date_creation'
    
admin.register(Commentaire,CategorieAdmin)

