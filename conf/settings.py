"""
- Made by nvd to order PNR Company
- Django settings for Persian Language Processing project.
"""

from pathlib import Path
import os
import logging
from nvd.base_dict import BaseDict

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-lb%y^a&#m4-t_a%+e(_7r(+ey)qj9l((d%k)l^*exba964^krx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'home.apps.PlpIndexConfig',
    'about_me.apps.PlpAboutMeConfig',
    'contact_me.apps.PlpContactMeConfig',

    'prerequisites.apps.PrerequisitesConfig',
    'classifications.apps.ClassificationsConfig',
    'keywords_extractions.apps.KeywordsExtractionsConfig',
    'stopwords_lists.apps.StopwordsListsConfig',
    'similarities.apps.SimilaritiesConfig',
    'template_views.apps.TemplateViewsConfig',
]

MIDDLEWARE = []
AUTH_PASSWORD_VALIDATORS = []

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'conf.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/


TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Add these new lines
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='.log',
    filemode='w',
    format='%(levelname)s - %(asctime)s - module: %(module)s - message: \"%(message)s\"'
)

# cashing
BASE_DICT = BaseDict()
