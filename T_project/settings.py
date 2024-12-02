from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h3ebzhsziedg9!(fsr!uu97r4r39z65g197qd25(qap_8x_j#z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'admin_interface',
    'colorfield',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'admin_tools_stats',
    'django_nvd3',
    'userapp',
    'TTT',
    'blog',
    'gallery',
    'destinations',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'T_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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


WSGI_APPLICATION = 'T_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('en', 'English'),
    ('th', 'ไทย'),
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static',]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/create-post/'

# Jazzmin settings
JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Your Site",
    "site_header": "Your Site",
    "site_brand": "Dashboard",
    "welcome_sign": "Welcome to the Dashboard",
    "copyright": "Your Company © 2024",
    
    # Theme settings
    "theme": "lumen",  # More gentle on the eyes
    "dark_mode_theme": "darkly",
    
    # UI Tweaks
    "ui_tweaks": {
        "navbar_small_text": False,
        "footer_small_text": False,
        "body_small_text": False,
        "brand_small_text": False,
        "brand_colour": False,
        "accent": "accent-primary",
        "navbar": "navbar-white navbar-light",
        "no_navbar_border": True,
        "navbar_fixed": True,
        "layout_boxed": False,
        "footer_fixed": False,
        "sidebar_fixed": True,
        "sidebar": "sidebar-light-primary",
        "sidebar_nav_small_text": False,
        "sidebar_disable_expand": False,
        "sidebar_nav_child_indent": True,
        "sidebar_nav_compact_style": False,
        "sidebar_nav_legacy_style": False,
        "sidebar_nav_flat_style": True,
        "theme": "default",
        "dark_mode_theme": None,
        "button_classes": {
            "primary": "btn-outline-primary btn-rounded",
            "secondary": "btn-outline-secondary btn-rounded",
            "info": "btn-outline-info btn-rounded",
            "warning": "btn-outline-warning btn-rounded",
            "danger": "btn-outline-danger btn-rounded",
            "success": "btn-outline-success btn-rounded"
        },
    },
    
    # Custom theme colors
    "custom_css": None,
    "custom_js": None,
    
    # Theme colors
    "theme_colors": {
        "primary": "#2B3A67",     # Dark blue
        "secondary": "#6B7AA1",   # Light blue
        "success": "#1C7C54",     # Green
        "info": "#1974D2",        # Blue
        "warning": "#FFC107",     # Yellow
        "danger": "#DC3545",      # Red
        "light": "#F8F9FA",       # Light gray
        "dark": "#343A40",        # Dark gray
        "white": "#FFFFFF",
        "black": "#000000",
    },
    "language_chooser": True,
}

# Additional UI tweaks for better readability
JAZZMIN_UI_TWEAKS = {
    "theme": "lumen",
    "dark_mode_theme": "darkly",
    "light_mode_theme": {
        "primary": "#2E4057",
        "secondary": "#748CAB",
        "accent": "#4C6885",
    }
}

# Additional settings for modern look
JAZZMIN_SETTINGS["show_ui_builder"] = True
JAZZMIN_SETTINGS["language_chooser"] = True
JAZZMIN_SETTINGS["use_google_fonts_cdn"] = True
JAZZMIN_SETTINGS["show_filters"] = True
JAZZMIN_SETTINGS["order_with_respect_to"] = ["auth", "gallery"]

# Admin Interface Theme Settings
X_FRAME_OPTIONS = 'SAMEORIGIN'
SILENCED_SYSTEM_CHECKS = ['security.W019']

# Admin Charts Configuration
ADMIN_CHARTS_NVD3_JS_PATH = 'admin/js/nvd3/nv.d3.min.js'
ADMIN_CHARTS_NVD3_CSS_PATH = 'admin/css/nvd3/nv.d3.min.css'
ADMIN_CHARTS_D3_JS_PATH = 'admin/js/d3/d3.min.js'