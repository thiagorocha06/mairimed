"""
Django settings for mairimed project.

Generated by 'django-admin startproject' using Django 1.10.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1',
    '0.0.0.0:5000',
    'localhost',
    'mairimed.pythonanywhere.com',
    'mairimed.herokuapp.com',
    'mairimed.com',
    'www.mairimed.com',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.sites',
    'registration',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'site_mairimed',
    'artigos',
    'contas',
    'dicionario_doencas',
    'dicionario_farmacos',
    'dicionario_alimentos',
    'dicionario_termos',
    'hitcount',
    'quiz',
    'multichoice',
    'true_false',
    'essay',
    'pagedown',
    'contactus',
    'portal_saude',
    'channels',
    'chatbot',
    'chatterbot.ext.django_chatterbot',
]

# ChatterBot settings

CHATTERBOT = {
    'name': 'Django ChatterBot Example',
    'trainer': 'chatterbot.trainers.ChatterBotCorpusTrainer',
    'training_data': [
        'chatterbot.corpus.english.greetings'
    ],
    'django_app_name': 'django_chatterbot',
    "read_only": "True"

}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mairimed.urls'

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

WSGI_APPLICATION = 'mairimed.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mairimed',
        'USER': 'thiagorocha',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    #os.path.join(BASE_DIR, "static_in_env"),
    #'/var/www/static/',
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'live-static', 'static-root', 'our_static')
#os.path.join(os.path.dirname(BASE_DIR), 'static_in_env', 'static_root')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'live-static', 'media-root', 'our_static')
#os.path.join(os.path.dirname(BASE_DIR), 'static_in_env', 'media_root')

LOGIN_REDIRECT_URL	=	'/mairimed/interno/'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mairimedcontato@gmail.com'
EMAIL_HOST_PASSWORD = 'EMAIL_HOST_PASSWORD'
DEFAULT_FROM_EMAIL = 'mairimedcontato@gmail.com'
DEFAULT_TO_EMAIL = 'mairimedcontato@gmail.com'
SITE_ID = 1

CONTACT_US_EMAIL = 'mairimed.com@gmail.com'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgiref.inmemory.ChannelLayer",
        "ROUTING": "chatbot.routing.channel_routing",
    },
}
