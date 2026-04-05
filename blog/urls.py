from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.Accueil, name = 'accueil'),
    path('incrire/', views.Inscription.as_view(), name='inscrire'),
    path('liste/',views.ListView,name='liste_des_articles'),
    path('liste/<int:id>/',views.DetailView,name='detail'),

    path("commentaire/modifier/<int:id>/", views.modifier_commentaire, name="modifier_commentaire"),
    path("commentaire/supprimer/<int:id>/", views.supprimer_commentaire, name="supprimer_commentaire"),
]
