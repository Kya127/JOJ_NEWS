# JOJ NEWS - Plateforme d'actualités et de commentaires

Une plateforme moderne pour la publication d'articles et la gestion de commentaires avec notifications email.

##  Fonctionnalités

- **Gestion des articles** : Création, modification, suppression
- **Système de commentaires** : Commentaires avec notifications email
- **Authentification utilisateur** : Inscription, connexion classique et Google OAuth2
- **Design moderne** : Interface responsive avec Bootstrap 5
- **Base de données MySQL** : Support MySQL pour la production

### Étapes d'installation

1. **Cloner le projet**
```bash
git clone https://github.com/Kya127/JOJ_NEWS.git
cd JOJ_NEWS
```

2. **Installer les dépendances**
```bash
pip install -r requierement.txt
```

3. **Configurer l'environnement**
```bash
cp .env.template .env
# Modifier le fichier .env avec vos informations
```

4. **Créer la base de données MySQL**
```sql
CREATE DATABASE joj_news;
```

5. **Appliquer les migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Créer un superutilisateur**
```bash
python manage.py createsuperuser
```

7. **Lancer le serveur**
```bash
python manage.py runserver
```

## Configuration

### Base de données MySQL
Le projet utilise MySQL avec les variables d'environnement suivantes :

```env
# Base de données MySQL
DB_NAME=joj_news
DB_USER=root
DB_PASSWORD=root
DB_HOST=localhost
DB_PORT=3306
```

### Configuration Email (Gmail)
```env
# Email configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=votre_email@gmail.com
EMAIL_HOST_PASSWORD=votre_mot_de_passe_app
DEFAULT_FROM_EMAIL=votre_email@gmail.com
```

### Configuration Google OAuth2
Pour activer l'authentification Google, configurez les variables suivantes :

```env
# Configuration Google OAuth2
GOOGLE_OAUTH2_CLIENT_ID=votre_client_id_google
GOOGLE_OAUTH2_CLIENT_SECRET=votre_client_secret_google
GOOGLE_OAUTH2_REDIRECT_URI=http://127.0.0.1:8000/google/callback/
```

#### Étapes de configuration Google OAuth2

1. **Créer un projet Google Cloud Console**
   - Allez sur [Google Cloud Console](https://console.cloud.google.com/)
   - Créez un nouveau projet ou utilisez un projet existant

2. **Activer les APIs requises**
   - Activez "Google+ API" ou "People API"
   - Activez "OAuth2 API"

3. **Créer des identifiants OAuth2**
   - Allez dans "APIs & Services" > "Credentials"
   - Cliquez sur "Create Credentials" > "OAuth 2.0 Client IDs"
   - Choisissez "Web application"
   - Ajoutez l'URI de redirection : `http://127.0.0.1:8000/google/callback/`

4. **Configurer les variables d'environnement**
   - Copiez le Client ID et Client Secret dans votre fichier `.env`
   - Assurez-vous que le redirect_uri correspond exactement

#### URLs d'authentification Google
- **Connexion Google** : `/google/login/`
- **Callback OAuth2** : `/google/callback/`
- **Déconnexion** : `/google/logout/`

#### Fonctionnalités de l'authentification Google
- **Connexion rapide** : Un clic avec votre compte Google
- **Création automatique** : Les utilisateurs sont créés automatiquement
- **Sécurité** : Utilise le protocole OAuth2 sécurisé
- **Intégration** : Fonctionne avec le système d'authentification Django existant

##  Personnalisation

### Variables CSS
Le thème utilise les couleurs "Dakar" :
- `--dakar-blue: #00A3E0` (Bleu turquoise)
- `--dakar-yellow: #FFD100` (Jaune vif)
- `--dakar-white: #FFFFFF` (Blanc)
- `--dakar-black: #1A1A1A` (Noir)

### Structure des fichiers
- `templates/` : Templates HTML avec Bootstrap 5
- `static/css/` : Feuilles de style personnalisées
- `static/img/` : Images et logos

##  Développement

### Architecture du projet
```
JOJ_NEWS/
|
|   blog/                    # Application principale (articles, commentaires)
|   |   models.py           # Modèles de données
|   |   views.py            # Vues Django
|   |   forms.py            # Formulaires
|   |   urls.py             # Routes URL
|   |   signals.py           # Signaux Django
|   |   templates/          # Templates HTML
|
|   google_auth/            # Application Google OAuth2
|   |   views.py            # Vues OAuth2 (login, callback, logout)
|   |   oauth.py            # Logique OAuth2 (flow, user info)
|   |   urls.py             # URLs OAuth2
|   |   templates/          # Templates Google OAuth2
|
|   config/                  # Configuration Django
|   |   settings.py         # Paramètres principaux
|   |   urls.py            # URLs globales
|   |   wsgi.py            # Déploiement
|
|   static/                   # Fichiers statiques
|   |   css/              # Styles CSS
|   |   img/              # Images
|
|   templates/                # Templates globaux
|   .env.template            # Template variables
|   .env                    # Variables d'environnement
|   requierement.txt         # Dépendances Python
```

### Fonctionnalités clés

#### Système de notifications email
- **Signal Django** : Déclenché automatiquement lors de la création d'un commentaire
- **Expéditeur** : Email de l'utilisateur qui commente
- **Destinataire** : Administrateur (`votre@email.com`)
- **Reply-To** : Permet de répondre directement à l'utilisateur

#### Formulaires d'authentification
- **Inscription** : Capture `email`, `first_name`, `last_name`
- **Connexion classique** : Interface moderne avec validation
- **Connexion Google OAuth2** : Authentification en un clic
- **Styles** : Design responsive avec animations

#### Application Google OAuth2
- **Séparation claire** : Logique OAuth2 dans application dédiée `google_auth`
- **Sécurité** : Utilisation des scopes `openid`, `userinfo.email`, `userinfo.profile`
- **Intégration** : Compatible avec le système d'authentification Django existant
- **Templates** : Interface dédiée pour le flow OAuth2

## Sécurité

### Variables d'environnement
- Fichier `.env` protégé par `.gitignore`
- Configuration email avec python-decouple
- Mots de passe non stockés en clair dans le code

### Recommandations
- Utiliser des mots de passe forts pour le superutilisateur
- Configurer HTTPS en production
- Activer `DEBUG=False` en production

## Contribuer

### Guide de contribution
1. **Forker le projet**
2. **Créer une branche** : `git checkout -b fonctionnalite`
3. **Commiter les changements** : Messages clairs et descriptifs
4. **Pull Request** : Demander une revue du code

### Normes de code
- **PEP 8** : Style de code Python
- **Bootstrap 5** : Classes CSS cohérentes
- **Django Best Practices** : Sécurité et performance

## Support

### Problèmes courants
- **Erreur MySQL 2002** : Vérifier que le serveur MySQL est démarré
- **Module manquant** : `pip install -r requierement.txt`
- **Permission refusée** : Vérifier les permissions de la base de données
- **Erreur redirect_uri_mismatch** : Vérifier que l'URI dans Google Cloud Console correspond exactement à `http://127.0.0.1:8000/google/callback/`
- **Erreur 400 invalid_request** : Assurez-vous que le Client ID et Client Secret sont corrects dans le fichier `.env`
- **Erreur NoReverseMatch** : Vérifier que l'application `google_auth` est bien dans `INSTALLED_APPS`

**Développé par [Kya127](https://github.com/Kya127), [anf692](https://github.com/anf692) et [Aby01](https://github.com/Aby01)**

*Dernière mise à jour : Avril 2026*
