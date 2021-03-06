"""
Django settings for advanceDjango project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1m1f05vv0yzzyxjv6)l)1^+o)h3#fplxzlbxjc321s9xg@&ux1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',
    'stockapp',
    'django_celery_results',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.check_login.CheckLoginMiddleware',
    'middleware.cache_page.CachePageMiddleware',
]

ROOT_URLCONF = 'advanceDjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'advanceDjango.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'advance1',
        'HOST': '47.102.218.113',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '123456',
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"',
            'charset': 'utf8mb4'
        }
    }
}
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# ??????Django?????????
LOGGING = {
    'version': 1.0,
    'formatters': {
        'base': {
            'format': '[%(asctime)s %(name)s ] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'out': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'base'
        },
        'file': {
            'class': 'logging.FileHandler',
            'level': 'WARNING',
            'formatter': 'base',
            'filename': f'{BASE_DIR}/warn.log'
        }
    },
    'loggers': {
        # ??????????????? django.server
        'django.server': {
            'handlers': ['out', 'file'],
            'level': 'CRITICAL',
            'propagate': False
        },
        'mylogger': {
            'handlers': ['out', 'file'],
            'level': 'INFO',
            'propagate': True
        }
    }
}

# ????????????
CACHES = {
    'file': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': F'{BASE_DIR}/mycache',
        'TIMEOUT': 300,
        'OPTIONS': {
            'MAX_ENTRIES': 500,
            'CULL_FREQUENCY': 3
        }
    },
    'html': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    },
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        # "LOCATION": "redis://:????????????@???????????????:6379/0",
        'LOCATION': 'redis://:1qaz2wsx@47.102.218.113:6379/10',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'SOCKET_CONNECT_TIMEOUT': 10,
            'SOCKET_TIMEOUT': 10
        }
    }
}

# ??????SESSION
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_COOKIE_NAME = 'SESSION_ID'
SESSION_COOKIE_PATH = '/'
SESSION_CACHE_ALIAS = 'default'  # cache?????????
SESSION_COOKIE_AGE = 1209600  # ?????????????????????

# ??????Celery
CELERY_IMPORTS = ('stockapp.tasks',)
CELERY_RESULT_BACKEND = 'django-db'
CELERY_TASK_ALWAYS_EAGER = True
