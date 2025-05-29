import os
from pathlib import Path

# Шлях до кореневої директорії проєкту
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретний ключ (не публікуйте його в реальних проєктах)
SECRET_KEY = 'django-insecure-замініть-на-ваш-секретний-ключ'

# Налаштування для розробки (вимкніть DEBUG у продакшн)
DEBUG = True

ALLOWED_HOSTS = []

# Встановлені додатки
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haircare_app',  # Ваш додаток для догляду за волоссям

]

# Мідлвери
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Кореневий URL конфігурації
ROOT_URLCONF = 'haircare.urls'

# Налаштування шаблонів
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Шлях до папки з шаблонами
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

# Налаштування WSGI
WSGI_APPLICATION = 'haircare.wsgi.application'

# Налаштування бази даних (SQLite для розробки)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Налаштування автентифікації
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

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/profile/'  # Або іншу сторінку, куди має потрапити користувач після входу
LOGOUT_REDIRECT_URL = '/welcome/'


# Налаштування для локалізації
LANGUAGE_CODE = 'uk'  # Українська мова

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_TZ = True

# Налаштування для статичних файлів
STATIC_URL = '/static/'

# Додаткові шляхи для статичних файлів
STATICFILES_DIRS = [BASE_DIR / 'static']

# Статичні файли для продакшн
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Файли медіа (якщо потрібно)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Налаштування за замовчуванням для primary key полів
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
