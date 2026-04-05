from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Article, Commentaire
from .forms import FormulaireCommentaire
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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


@login_required
def modifier_commentaire(request, id):
    commentaire = get_object_or_404(Commentaire, id=id)
    
    # Vérification de sécurité : seul l'auteur peut modifier
    if commentaire.auteur != request.user:
        messages.error(request, "Vous n'êtes pas autorisé à modifier ce commentaire.")
        return redirect('articles:detail', id=commentaire.article.id)
    
    if request.method == 'POST':
        form = FormulaireCommentaire(request.POST, instance=commentaire)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre commentaire a été modifié.")
            return redirect('articles:detail', id=commentaire.article.id)
    else:
        form = FormulaireCommentaire(instance=commentaire)
    
    context = {
        'form': form,
        'commentaire': commentaire,
        'article': commentaire.article
    }
    return render(request, 'modifier_commentaire.html', context)



@login_required
def supprimer_commentaire(request, id):
    commentaire = get_object_or_404(Commentaire, id=id)
    article_id = commentaire.article.id
    
    # Vérification de sécurité : seul l'auteur peut supprimer
    if commentaire.auteur != request.user:
        messages.error(request, "Vous n'êtes pas autorisé à supprimer ce commentaire.")
        return redirect('articles:detail', id=article_id)
    
    if request.method == 'POST':
        commentaire.delete()
        messages.success(request, "Votre commentaire a été supprimé.")
        return redirect('articles:detail', id=article_id)
    
    context = {
        'commentaire': commentaire,
        'article': commentaire.article
    }
    return render(request, 'supprimer_commentaire.html', context)





   
         