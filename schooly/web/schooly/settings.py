import os

ENVIRONMENT = os.getenv('ENV', 'DEV')

USE_HTTPS = os.getenv('HTTPS', False)

# Is it actually on the live server?
IS_PROD = (ENVIRONMENT == 'PROD')

# Enable Django's built in debugging features when not on live server
DEBUG = not IS_PROD


# Base Settings
# Find the directory path on our file system
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname((__file__))))
PROGRAM_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname((__file__)))))

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


# Database Settings
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_BACKEND'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', '5432'),
    },
}



# Base Security
ALLOWED_HOSTS = ['schoolyweb', 'localhost', '192.168.99.100']

if IS_PROD:
    # When it breaks, it'll send an email to these people
    ADMINS = [
        ('Yasmeen Hmaidan', 'yasmeenhmaidan@hotmail.com'),
    ]

    # When it breaks in a different way, it'll send an email to the same people
    MANAGERS = ADMINS

# Some special security things are only activated over HTTPS
if USE_HTTPS:
    CSRF_COOKIE_SECURE = True

    SECURE_CONTENT_TYPE_NOSNIFF = True

    SESSION_COOKIE_SECURE = True

    SECURE_BROWSER_XSS_FILTER = True


# Settings that are always on
CSRF_COOKIE_SAMESITE = 'Strict'

SESSION_COOKIE_SAMESITE = 'Strict'

CSRF_COOKIE_HTTPONLY = True

SESSION_COOKIE_HTTPONLY = True


# Request Processing

# Every request and response is sent through these functions. They modify it on the way in and out
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Where do we define our url structure?
ROOT_URLCONF = 'schooly.urls'

# Configuration for the template system
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + '/templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
            'builtins': [
                'django.contrib.staticfiles.templatetags.staticfiles',
            ],
        },
    },
]

# Where the builtin web server (inefficient) is stored
WSGI_APPLICATION = 'schooly.wsgi.application'


# Static and Media Files
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'globalstatic/'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Authentication
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

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

LOGOUT_REDIRECT_URL = '/'


# Django's Secret Key
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
