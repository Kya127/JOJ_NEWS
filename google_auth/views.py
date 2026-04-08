from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import JsonResponse
from .oauth import Google_oauth_flow, get_google_user_info, store_credentials, get_stored_credentials
import json

def google_login(request):
    """Vue pour la connexion Google OAuth2"""
    flow = Google_oauth_flow(request)
    authorization_url, _ = flow.authorization_url(prompt='consent')
    
    return render(request, 'google_auth/google_login.html', {
        'google_auth_url': authorization_url
    })

def google_callback(request):
    """Callback pour Google OAuth2"""
    flow = Google_oauth_flow(request)
    code = request.GET.get('code')
    
    if not code:
        return redirect('login')
    
    try:
        flow.fetch_token(code=code)
        credentials = flow.credentials
        store_credentials(request, credentials)
        
        # Récupérer les informations utilisateur
        user_info = get_google_user_info(credentials)
        
        # Créer ou récupérer l'utilisateur
        user, created = User.objects.get_or_create(
            email=user_info['email'],
            defaults={
                'username': user_info['email'].split('@')[0],
                'first_name': user_info.get('given_name', ''),
                'last_name': user_info.get('family_name', ''),
            }
        )
        
        # Connecter l'utilisateur
        login(request, user)
        
        return redirect('articles:accueil')
        
    except Exception as e:
        return render(request, 'google_auth/google_callback.html', {
            'error': f"Erreur lors de la connexion Google: {str(e)}"
        })

def logout_view(request):
    """Déconnexion"""
    logout(request)
    return redirect('login')
