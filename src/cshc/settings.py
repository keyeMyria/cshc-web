"""
Django settings for cshc project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import raven
from os.path import abspath, dirname, join, normpath
from easy_thumbnails.conf import Settings as thumbnail_settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = dirname(dirname(abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lw*s+7y@xsrl-9f(f^%wm(_!8choix2%ljvoccf9(^mh*uckk5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

VERSION_FILE = normpath(join(BASE_DIR, '..', 'version.txt'))
VERSION = open(VERSION_FILE).read().lstrip('v').rstrip()

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'core.CshcUser'

# Application definition

INSTALLED_APPS = [
    'core.apps.CoreConfig',
    'venues.apps.VenuesConfig',
    'competitions.apps.CompetitionsConfig',
    'opposition.apps.OppositionConfig',
    'teams.apps.TeamsConfig',
    'members.apps.MembersConfig',
    'training.apps.TrainingConfig',
    'matches.apps.MatchesConfig',
    'awards.apps.AwardsConfig',
    'documents.apps.DocumentsConfig',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.humanize',
    'webpack_loader',
    'debug_toolbar',
    'django_extensions',
    'django_user_agents',
    'geoposition',
    'django_bootstrap_breadcrumbs',
    'easy_thumbnails',
    'image_cropping',
    'ckeditor',
    'ckeditor_uploader',
    'graphene_django',
    'django_filters',
    'disqus',
    'taggit',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.linkedin_oauth2',
    'raven.contrib.django.raven_compat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
]

ROOT_URLCONF = 'cshc.urls'

SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [join(BASE_DIR, 'cshc', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cshc.context_processors.utils',
            ],
        },
    },
]

WSGI_APPLICATION = 'cshc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


SERVER_EMAIL = 'website@cambridgesouthhockeyclub.co.uk'

# MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(BASE_DIR, 'media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
# END MEDIA CONFIGURATION

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = join(BASE_DIR, 'assets')

STATICFILES_DIRS = (
    # We do this so that django's collectstatic copies our bundles to the
    # STATIC_ROOT or syncs them to whatever storage we use.
    join(BASE_DIR, 'frontend'),
    join(BASE_DIR, 'static'),
)

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': join(BASE_DIR, '..', 'webpack-stats.json'),
    }
}

CORS_ORIGIN_ALLOW_ALL = True

# Used by DJANGO_DEBUG_TOOLBAR - DEV ONLY
INTERNAL_IPS = ['127.0.0.1']


# Django User Agents
# https://github.com/selwin/django-user_agents

# Name of cache backend to cache user agents. If it not specified default
# cache alias will be used. Set to `None` to disable caching.
USER_AGENTS_CACHE = 'default'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

GMAPS_API_KEY = os.environ['GMAPS_API_KEY']
GEOPOSITION_GOOGLE_MAPS_API_KEY = GMAPS_API_KEY
GEOPOSITION_MAP_OPTIONS = {
    'minZoom': 3,
    'maxZoom': 15,
    'scrollwheel': True,
    'lat': 52.206133926014665,
    'lng': 0.12531280517578125,
}


# Django Bootstrap Breadcrumbs
# Ref: http://django-bootstrap-breadcrumbs.readthedocs.io/en/latest/
BREADCRUMBS_TEMPLATE = "core/_breadcrumbs.html"


# Django Image Cropping
# Ref: https://github.com/jonasundderwolf/django-image-cropping
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS
IMAGE_CROPPING_BACKEND = 'core.backends.image_backend.ResizedImageEasyThumbnailsBackend'

THUMBNAIL_ALIASES = {
    '': {
        'avatar': {'size': (50, 50), 'crop': True},
        'member-link': {'size': (30, 30), 'crop': True},
        'squad-list': {'size': (255, 255), 'crop': True},
    },
}

# ckeditor
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_FILENAME_GENERATOR = 'core.models.make_unique_filename'

# Graphene
GRAPHENE = {
    'SCHEMA': 'cshc.schema.schema',  # Where your Graphene schema lives
    'SCHEMA_INDENT': 2,
    'MIDDLEWARE': [
        'graphene_django.debug.DjangoDebugMiddleware',
    ]
}

# Django-AllAuth
# Ref: http://django-allauth.readthedocs.io/en/latest
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_SIGNUP_FORM_CLASS = 'core.forms.SignupForm'

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'js_sdk',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time',
        ],
        'EXCHANGE_TOKEN': True,
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.10',
    },
    'linkedin': {
        'SCOPE': [
            'r_emailaddress',
        ],
        'PROFILE_FIELDS': [
            'id',
            'first-name',
            'last-name',
            'email-address',
            'picture-url',
            'public-profile-url',
        ]
    }
}

# Ref: https://github.com/vintasoftware/django-templated-email
TEMPLATED_EMAIL_TEMPLATE_DIR = 'emails/'
TEMPLATED_EMAIL_FILE_EXTENSION = 'html'

# raven CONFIGRATION
# Ref: https://sentry.io/onboarding/cambridge-south-hockey-club/cshc-django/configure/python-django
RAVEN_CONFIG = {
    'dsn': os.environ['SENTRY_DNS'],
    'release': VERSION,
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            # To capture more than ERROR, change to WARNING, INFO, etc.
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {'custom-tag': 'x'},
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

# django-disqus CONFIGURATION
# Ref: https://django-disqus.readthedocs.io/en/latest

DISQUS_API_KEY = os.environ['DISQUS_API_KEY']
DISQUS_WEBSITE_SHORTNAME = 'cshc-local'     # Need to change for prod

# END django-disqus CONFIGURATION
