"""
Django settings for App42PaaS_Python_CouchDB_Sample project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b0e2nby0@$$59b(me4!zyl^*(s_$a!%!vymna6i%1kbb@x^f#t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'sample',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'App42PaaS_Python_CouchDB_Sample.urls'

WSGI_APPLICATION = 'App42PaaS_Python_CouchDB_Sample.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


COUCHDB_DATABASES = {
    'default': {
        #'ENGINE': 'django_mongodb_engine',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		'ENGINE': 'couchdbkit.ext.django', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'sample',                      # Or path to database file if using sqlite3.
        'USER': 'allnau5ed7nnkj01',                      # Not used with sqlite3.
        'PASSWORD': 'a1lzfukva9kmh8l9y5zcdxiuugoikt4j',                  # Not used with sqlite3.
        'HOST': '54.208.130.57',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '61792',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
