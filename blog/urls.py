from django.urls import path
from . import views

urlpatterns = [
    path('', views.Accueil, name = 'accueil'),
    path('incrire/', views.Inscription.as_view(), name='inscrire'),
    path('liste/',views.ListView,name='liste_des_articles'),
]
