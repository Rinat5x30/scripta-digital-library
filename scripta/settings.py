from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key from environment
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-change-this-key-in-env')

# Debug mode from environment (default False for production)
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Allowed hosts from environment
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
]


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'scripta.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                    'main.context_processors.genres_context',
            ],
        },
    },
]


WSGI_APPLICATION = 'scripta.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_TZ = True


# Static files

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]


# Media files

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'



# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# CORS (для разработки)
CORS_ALLOW_ALL_ORIGINS = os.getenv('CORS_ALLOW_ALL_ORIGINS', 'False') == 'True'

if not CORS_ALLOW_ALL_ORIGINS:
    CORS_ALLOWED_ORIGINS = os.getenv('CORS_ALLOWED_ORIGINS', 'http://localhost:8000').split(',')

# X Frame
X_FRAME_OPTIONS = 'SAMEORIGIN'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

CSRF_TRUSTED_ORIGINS = [
    "https://scripta-digital-library-production.up.railway.app",
    "https://*.up.railway.app",
    "https://rinataghayev.ru",
    "https://www.rinataghayev.ru",
    "http://localhost:8000",
]

# ===== Security Settings =====
# HTTPS and SSL
SECURE_SSL_REDIRECT = os.getenv('SECURE_SSL_REDIRECT', 'False') == 'True'
SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE', 'False') == 'True'
CSRF_COOKIE_SECURE = os.getenv('CSRF_COOKIE_SECURE', 'False') == 'True'

# Security Headers
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_SECURITY_POLICY = True
X_FRAME_OPTIONS = 'DENY'

# HSTS
SECURE_HSTS_SECONDS = 31536000 if not DEBUG else 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = not DEBUG
SECURE_HSTS_PRELOAD = not DEBUG

# Additional security
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'
PERMISSIONS_POLICY = {
    "accelerometer": [],
    "ambient-light-sensor": [],
    "autoplay": [],
    "camera": [],
    "geolocation": [],
    "gyroscope": [],
    "magnetometer": [],
    "microphone": [],
    "payment": [],
    "usb": [],
}