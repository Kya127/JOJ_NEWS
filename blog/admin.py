from django.contrib import admin
from .models import Categorie, Article

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


