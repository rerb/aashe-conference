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

from memcacheify import memcacheify

# Import authentication settings
from integration_settings.authentication import *

# Import google analytics
from integration_settings.google_analytics import *

# Import logging settings
from integration_settings.logging.sentry import *

import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'notsosecretkey')

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
    'compressor',
    'tinymce_browser',

    'conference',
    'conference.content',
    'aashe.aasheauth',
    'aashe_theme',
    'block_content',
    'django_markup',
    'integration_settings.authentication',
    'integration_settings.google_analytics',
)

MIDDLEWARE_CLASSES = (
    'minidetector.Middleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    # 'aashe.aasheauth.middleware.AASHEAccountMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
)

CACHES = memcacheify()

CACHE_MIDDLEWARE_SECONDS = 86400

ROOT_URLCONF = 'conference.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(__file__), "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.core.context_processors.request',
                'django.template.context_processors.debug',
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



# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

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
    AWS_S3_SECURE_URLS = False
    FEINCMS_MEDIALIBRARY_UPLOAD_TO = os.path.join(
        DEFAULT_S3_PATH, 'medialibrary')

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

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

FEINCMS_RICHTEXT_INIT_TEMPLATE = 'init_tinymce.html'

COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', False)

THUMBNAIL_PRESERVE_FORMAT = True

SITE_ID = 1
USE_X_FORWARDED_HOST = True

# Add a flag to override a few settings in a local development environment
if os.environ.get('LOCAL'):
    TEMPLATES[0]['OPTIONS']['debug'] = True
    THUMBNAIL_DEBUG = True
    DATABASES = {
        'default': {
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            'ENGINE': 'django.db.backends.sqlite3',
            },
        }
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }

if os.environ.get('HEROKU_DEV'):
    TEMPLATES[0]['OPTIONS']['debug'] = True
    THUMBNAIL_DEBUG = True
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

HTML_MINIFY = os.environ.get('HTML_MINIFY', False)

GOOGLE_ANALYTICS_PROPERTY_ID = os.environ.get(
    'GOOGLE_ANALYTICS_PROPERTY_ID', None)
GOOGLE_ANALYTICS_DOMAIN = os.environ.get('GOOGLE_ANALYTICS_DOMAIN', None)
