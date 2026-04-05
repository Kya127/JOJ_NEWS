from django.shortcuts import render,get_object_or_404

from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Article

# Create your views here.
def Accueil(request):
    return render(request,'index.html')


class Inscription(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('accueil')
    template_name = 'registration/signup.html'

def ListView(request):
    liste_article=Article.objects.all()
    context={
        'liste_article':liste_article
    }
    return render(request,'liste.html',context)

def DetailView(request,id):
    un_article=get_object_or_404(Article,id=id)
    article_recuperee={
        'un_article':un_article
    }
    return render(request,'detail.html',article_recuperee)