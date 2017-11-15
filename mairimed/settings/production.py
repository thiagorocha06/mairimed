# pythonanywhere
# mairimed

"""
Django settings for mairimed project.

Generated by 'django-admin startproject' using Django 1.10.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
from django.conf import settings

if not settings.DEBUG:
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
        'mairimed.herokuapp.com',
        'mairimed.pythonanywhere.com',
        'mairimed.com',
        'www.mairimed.com',
    ]


    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'artigos',
        'contas',
        'exercicios',
        'dicionario_medico',
        'dicionario_farmaceutico',
        'hitcount',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        #'whitenoise.middleware.WhiteNoiseMiddleware',
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
            'PASSWORD': os.environ['PG_PASSWORD'],
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

    import dj_database_url

    db_from_env = dj_database_url.config()
    DATABASES['default'].update(db_from_env)

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

    AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET']
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
        #os.path.join(BASE_DIR, "static_in_env"),
        #'/var/www/static/',
    ]

    STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'live-static', 'static-root')
    #os.path.join(os.path.dirname(BASE_DIR), 'static_in_env', 'static_root')

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'live-static', 'media-root')
    #os.path.join(os.path.dirname(BASE_DIR), 'static_in_env', 'media_root')

    LOGIN_REDIRECT_URL	=	'/'

    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025

    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/

    #STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
