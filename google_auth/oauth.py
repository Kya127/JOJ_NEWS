from google_auth_oauthlib.flow import Flow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from django.shortcuts import redirect
from django.conf import settings
from django.urls import reverse
import requests
import json

def Google_oauth_flow(request):
    """Crée le flux OAuth2 pour Google"""
    flow = Flow.from_client_config(
        client_config={
            "web": {
                "client_id": settings.GOOGLE_OAUTH2_CLIENT_ID,
                "client_secret": settings.GOOGLE_OAUTH2_CLIENT_SECRET,
                "redirect_uris": [settings.GOOGLE_OAUTH2_REDIRECT_URI],
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token"
            }
        },
        scopes=[
            "openid",
            "https://www.googleapis.com/auth/userinfo.email",
            "https://www.googleapis.com/auth/userinfo.profile"
        ],
        redirect_uri=settings.GOOGLE_OAUTH2_REDIRECT_URI
    )
    return flow

def get_google_user_info(credentials):
    """Récupère les informations de l'utilisateur Google"""
    import google.auth.transport.requests
    transport = google.auth.transport.requests.Request()
    user_info = requests.get("https://www.googleapis.com/oauth2/v2/userinfo", headers={
        'Authorization': f'Bearer {credentials.token}'
    })
    return user_info.json()

def store_credentials(request, credentials):
    """Stocke les credentials en session"""
    request.session['google_credentials'] = credentials.to_json()

def get_stored_credentials(request):
    """Récupère les credentials stockés en session"""
    credentials_json = request.session.get('google_credentials')
    if credentials_json:
        return Credentials.from_authorized_user_info(json.loads(credentials_json))
    return None
