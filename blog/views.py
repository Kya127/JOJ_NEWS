from django.shortcuts import render,get_object_or_404,redirect

from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Article
from .forms import FormulaireCommentaire
from django.contrib.auth.decorators import login_required

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

@login_required
def DetailView(request,id):
    
     
     un_article=get_object_or_404(Article,id=id)
     commentaires = un_article.commentaires_article.all()
     if request.method  =='POST':
        form = FormulaireCommentaire(request.POST) 
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.auteur_commentaire = request.user
            commentaire.article_commentaire = un_article
            commentaire.save()
            return  redirect('detail',id=un_article.id)
     else:
         form = FormulaireCommentaire() 
     affichage={
             'article': un_article,
             'commentaires': commentaires,
             'form': form
         }
         
     return render(request,'detail.html',affichage)




   
         