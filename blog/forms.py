from django import forms
from .models import Commentaire

class FormulaireCommentaire(forms.ModelForm):
   class Meta:
       model = Commentaire
       fields = ['texte_commentaire']
       widgets = {
           
           'texte_commentaire' : forms.Textarea(attrs={
               'class': 'form-control' ,
               'placholder' : 'Mettre ici votre commentaire'
               
           })
       }
      