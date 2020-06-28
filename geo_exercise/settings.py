"""
Django settings for geo_exercise project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")  #')+7d&f^cbra$1n76()kd_odp(deb9--dvnx4btyc$khck$zx3h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG")

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'leaflet',
    'djgeojson',
    'django.contrib.gis',
    'crispy_forms',
    'django_forms_bootstrap',
    'django.contrib.sites',

    'core',
    'exercises',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

SITE_ID = 2
CRISPY_TEMPLATE_PACK = 'bootstrap4'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGIN_REDIRECT_URL = '/'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = False

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
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

ROOT_URLCONF = 'geo_exercise.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates"),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

WSGI_APPLICATION = 'geo_exercise.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# Initially I used two database with dbrouters to redirect or select db
# to use. However, I left this commented just to explain how I deal
# with multiple databases
#
# 'default': {
#     'ENGINE': 'django.db.backends.postgresql_psycopg2',
#     'NAME': 'geo_exercise',
#     'USER': 'admin',
#     'PASSWORD': 'admin',
#     'HOST': os.getenv("DATABASE_HOST"),  # 'localhost',
#     'PORT': '5433',
#     'TEST': {
#        'DEPENDENCIES': [],
#     }
#     },
#     'geo': {
#    'ENGINE': os.getenv("GET_DATABASE_ENGINE"),  # 'django.contrib.gis.db.backends.postgis',
#    'NAME': os.getenv("GEO_DATABASE_NAME"),  # 'geodjango',
#    'USER': os.getenv("GEO_DATABASE_USERNAME"),  # 'admin',
#    'PASSWORD': os.getenv("GEO_DATABASE_PASSWORD"),  # 'admin',
#    'HOST': os.getenv("GEO_DATABASE_HOST"),  # 'localhost',
#    'PORT': os.getenv("GEO_DATABASE_PORT"),  # '5432',
#    'TEST': {
#        'DEPENDENCIES': ['default'],
#    }
#},

DATABASES = {
    'default': {
         'ENGINE': os.getenv("GET_DATABASE_ENGINE"),
         'NAME': os.getenv("GEO_DATABASE_NAME"),
         'USER': os.getenv("GEO_DATABASE_USERNAME"),
         'PASSWORD': os.getenv("GEO_DATABASE_PASSWORD"),
         'HOST': os.getenv("GEO_DATABASE_HOST"),
         'PORT': os.getenv("GEO_DATABASE_PORT"),
         'TEST': {}
    },
}

# used when I used two databases
# DATABASE_ROUTERS = ['exercises.dbrouters.MyDBRouter']


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# CELERY STUFF
BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Africa/Nairobi'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "core/static"),
]

# Logging settings
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s - %(levelname)s %(module)s %(process)d ] %(message)s'
        },
        'simple': {
            'format': '%(message)s',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'dataflair-debug.log',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file", "console"],
            "level": "ERROR",
            'propagate': True,
            'level': os.getenv('DJANGO_LOGLEVEL', 'DEBUG')
        },
        "celery": {
            "handlers": ["console"],
            "level": "ERROR",
        },
    },
}

# Leaflet config
LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (35, -9),
    'DEFAULT_ZOOM': 3,
    'MIN_ZOOM': 2,
    'MAX_ZOOM': 18
}