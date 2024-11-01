from pathlib import Path
from decouple import config  # Jos käytät python-decouple tai os jos dotenv käytössä
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY ja DEBUG .env-tiedostosta
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'rest_framework',
    'corsheaders',
    'bootstrap5',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'mysocialapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'mysocialapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# HTTPS-asetukset
SECURE_SSL_REDIRECT = not DEBUG



# AZURE DATABASE .env-tiedostosta
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 18 for SQL Server',
        },
    }
}

'''

#local mssms
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'socialapp',  # Tietokannan nimi
        'HOST': 'localhost',  # Palvelimen nimi tai IP, esim. 'localhost' tai '127.0.0.1'
        'PORT': '1433',  # SQL Serverin portti
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',  # SQL Server -ajuri
            'extra_params': 'TrustServerCertificate=yes;'  # (valinnainen) turvallisuusparametri
        },
    }
}

'''


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ALLOWED_HOSTS
ALLOWED_HOSTS = [
    'localhost', 
    '127.0.0.1', 
    '[::1]', 
    '10.0.2.2', 
    '10.98.100.250',
    '192.168.22.225' 
    'your_custom_domain',
    'djangosocialapp-dveccddwfda6cghe.northeurope-01.azurewebsites.net',
]

# CORS-asetukset
CORS_ALLOW_ALL_ORIGINS = False  # Tietoturvasyistä tuotantoympäristössä
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173", 
    "http://localhost:3000",  
    "https://yourdomain.com",
    "http://localhost:5000",
]

# CSRF-asetukset
CSRF_TRUSTED_ORIGINS = [
    "https://your_custom_domain"
]

# DRF-asetukset
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        # Lisää muita autentikaatioluokkia tarpeen mukaan
    ),
}