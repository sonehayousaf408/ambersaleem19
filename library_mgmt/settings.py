# ShopHub / settings.py  – replace the entire file with this
import os
from pathlib import Path

# ───────────────────────────────────────────────────────
# BASE SETTINGS
# ───────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your-secret-key'

# SECURITY WARNING: don’t run with DEBUG = True in production!
DEBUG = True

ALLOWED_HOSTS = []          # add your domain / IP here when you deploy

# ───────────────────────────────────────────────────────
# Applications
# ───────────────────────────────────────────────────────
INSTALLED_APPS = [
    # Django core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your apps
    'library',      # inventory / catalog
    'analytics',    # dashboards & reports
    'customers',    # customer management
    'sales',        # sales & POS   ← keep this line
]

# ───────────────────────────────────────────────────────
# Middleware
# ───────────────────────────────────────────────────────
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ───────────────────────────────────────────────────────
# URL Configuration
# ───────────────────────────────────────────────────────
ROOT_URLCONF = 'library_mgmt.urls'   # leave as‑is unless you renamed the project pkg

# ───────────────────────────────────────────────────────
# Templates
# ───────────────────────────────────────────────────────
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],   # global templates folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ───────────────────────────────────────────────────────
# WSGI
# ───────────────────────────────────────────────────────
WSGI_APPLICATION = 'library_mgmt.wsgi.application'

# ───────────────────────────────────────────────────────
# Database (SQLite for dev; swap for Postgres when ready)
# ───────────────────────────────────────────────────────
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ───────────────────────────────────────────────────────
# Password Validation (enable in prod)
# ───────────────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = []

# ───────────────────────────────────────────────────────
# Internationalization
# ───────────────────────────────────────────────────────
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Karachi'   # changed to your local zone
USE_I18N = True
USE_TZ = True

# ───────────────────────────────────────────────────────
# Static & Media
# ───────────────────────────────────────────────────────
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']   # optional: remove if not using

# ───────────────────────────────────────────────────────
# Primary Key Field Type
# ───────────────────────────────────────────────────────
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ───────────────────────────────────────────────────────
# Authentication: login / logout redirects
# ───────────────────────────────────────────────────────
# All three expect the **named URL patterns** below to exist
LOGIN_URL = 'login'                  # where to send unauthenticated users
LOGIN_REDIRECT_URL = 'home'          # after successful login
LOGOUT_REDIRECT_URL = 'login'        # after logout
