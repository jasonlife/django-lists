# -*- coding:utf-8 -*-
import os

DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADMINS = (
    ('Admin', 'admin@example.com'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'sqlite.db'),
        },
    }

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

USE_TZ = True
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: '/home/media/media.lawrence.com/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: 'http://media.lawrence.com/media/', 'http://example.com/media/'
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' 'static/' subdirectories and in STATICFILES_DIRS.
# Example: '/home/media/media.lawrence.com/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# URL prefix for static files.
# Example: 'http://media.lawrence.com/static/'
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: 'http://foo.com/static/admin/', '/static/admin/'.

# Additional locations of static files
STATICFILES_DIRS = (

    # Put strings here, like '/home/html/static' or 'C:/www/django/static'.
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '__PUT_SUPER_SECRET_RANDOM_STRING_HERE__'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

ROOT_URLCONF = 'proj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'dcf.context_processors.common_values'
            ],
        },
    },
]

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'dcf', 'locale'),
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'social.apps.django_app.default',
    'sorl.thumbnail',
    'bootstrapform',

    'dcf',

    'rest_framework',
]

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'login'

FORCE_SCRIPT_NAME = ''

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

AUTH_USER_MODEL = 'dcf.CustomUser'

# DCF specific settings
DCF_SITE_NAME = u'Django DCF App'
DCF_SITE_DESCRIPTION = u'Demo Classified Advertisements web site Powered by Django DCF app'
DCF_ITEM_PER_USER_LIMIT = 20
DCF_SITEMAP_LIMIT = 1000
DCF_RSS_LIMIT = 100
DCF_RELATED_LIMIT = 6
DCF_ITEM_PER_PAGE = 10
DCF_LOGIN_TO_CONTACT = True

GOOGLE_ANALYTICS_PROPERTY_ID = ''
GOOGLE_SITE_VERIFICATION_ID = ''

SOCIAL_AUTH_LOGIN_ERROR_URL = '/'

SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'

SOCIAL_AUTH_FACEBOOK_KEY = 'YOUR_FACEBOOK_OAUTH2_KEY_HERE'
SOCIAL_AUTH_FACEBOOK_SECRET = 'YOUR_FACEBOOK_OAUTH2_SECRET_HERE'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

CORS_ORIGIN_ALLOW_ALL = True

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

# Try to load local or prod settings if such exists
try:
    from settings_local import *
except ImportError as e:
    try:
        from settings_prod import *
    except ImportError as e:
        pass


ACCOUNT_ACTIVATION_DAYS = 7 # for django-regitration

# email BACKEND

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.mail.com'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 
#EMAIL_HOST_PASSWORD = 

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 
EMAIL_HOST_PASSWORD = 
