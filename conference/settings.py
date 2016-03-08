"""
Django settings for conference project.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8pfgju!ijy$s4^9r6=8*!1pwj-l(b6k6y$&6_-ao-&5k3v)1d5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', False)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'dj_database_url',
    'dj_static',
    'gunicorn',
    'psycopg2',
    'raven.contrib.django.raven_compat',
    'feincms',
    'mptt',
    'feincms.module.page',
    'feincms.module.medialibrary',
    'sorl.thumbnail',
    'gallery',

    'conference',
    'conference.content',
    'aashe.aasheauth',
    'aashe_theme',
    'block_content',
    'integration_settings.authentication',
    'integration_settings.logging',
    'integration_settings.google_analytics',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    # 'aashe.aasheauth.middleware.AASHEAccountMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'conference.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(__file__), "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'conference.wsgi.application'

AUTHENTICATION_BACKENDS = ('aashe.aasheauth.backends.AASHEBackend',
                           'django.contrib.auth.backends.ModelBackend',)

# Import authentication settings
from integration_settings.authentication import *

# Import google analytics
from integration_settings.google_analytics import *

# Import logging settings
from integration_settings.logging import *

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

import dj_database_url
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL', None)),
}

# Production Drupal Services settings
AASHE_DRUPAL_URI = os.environ.get('AASHE_DRUPAL_URI', None)
AASHE_DRUPAL_KEY = os.environ.get('AASHE_DRUPAL_KEY', None)
AASHE_DRUPAL_KEY_DOMAIN = os.environ.get('AASHE_DRUPAL_KEY_DOMAIN', None)
AASHE_DRUPAL_COOKIE_SESSION = os.environ.get(
    'AASHE_DRUPAL_COOKIE_SESSION', None)
AASHE_DRUPAL_COOKIE_DOMAIN = os.environ.get('AASHE_DRUPAL_COOKIE_DOMAIN', None)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Media
USE_S3 = os.environ.get('USE_S3', None)

if USE_S3:
    INSTALLED_APPS += ('s3_folder_storage',)
    from integration_settings.media.s3 import *
    print MEDIA_URL
    AWS_QUERYSTRING_AUTH = True
    FEINCMS_MEDIALIBRARY_UPLOAD_TO = os.path.join(DEFAULT_S3_PATH, 'medialibrary')
else:
    MEDIA_ROOT = os.environ.get("MEDIA_ROOT", os.path.join(BASE_DIR, 'media'))
    STATIC_ROOT = os.environ.get(
        "STATIC_ROOT", os.path.join(BASE_DIR, 'staticfiles'))
    FEINCMS_MEDIALIBRARY_UPLOAD_TO = 'medialibrary'

MEDIA_URL = "/media/"
STATIC_URL = "/conference/staticfiles/"

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), 'static'),
)

SITE_ID = 1
USE_X_FORWARDED_HOST = True

# Add a flag to override a few settings in a local development environment
if os.environ.get('LOCAL'):
    TEMPLATES[0]['OPTIONS']['debug'] = True
    THUMBNAIL_DEBUG = True
    DATABASES = {
    'default': {
        'NAME': 'conference',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'postgres',
        'PASSWORD': 'sonofmogh86',
        'HOST': 'localhost',
        'PORT': 5433,
    }}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True