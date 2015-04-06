# -*- coding: utf-8 -*-
"""
Django settings for djbook project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# TODO: remove all secret keys from settings and store them in OS environment variables
SECRET_KEY = 'gqar1u(#-+*2037wsa*e^)*c70+to!q+h3l@uljtk1t7zv@g2t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

# registration
ACCOUNT_ACTIVATION_DAYS = 3 # days count for storing activation key
REGISTRATION_AUTO_LOGIN = True # Automatically log the user in.

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL=' '

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
#SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/login/'
#SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/login/'

# Mail sending definition
AUTH_USER_EMAIL_UNIQUE = True
# EMAIL_HOST = 'smtp.ukr.net'
# EMAIL_PORT = 465
# EMAIL_HOST_USER = 'fog'
# EMAIL_HOST_PASSWORD = '1'
# EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'fog@ukr.net'

EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'rg@i.ua'
EMAIL_HOST_PASSWORD = 'ydN2-WUPFGfK0NGYQL7sTg'  
EMAIL_USE_TLS = True

# EMAIL_TIMEOUT = 10

SITE_ID = 1



# Backends for social auth
AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.contrib.vk.VKOAuth2Backend',
    'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
    'social_auth.backends.browserid.BrowserIDBackend',
    'social_auth.backends.contrib.livejournal.LiveJournalBackend',
    'social_auth.backends.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)


FACEBOOK_APP_ID='303143433227300'
FACEBOOK_API_SECRET='dcc487a1da117a5f5d6c21e9f231b0d9'

VK_APP_ID = '4644862'
VK_API_SECRET = 'oEseX8QI2q8OnnTuTzDz'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',
    'social_auth.context_processors.social_auth_by_name_backends',
)

# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django.contrib.auth.context_processors.auth',
#     'django.core.context_processors.request',
#     'social_auth.context_processors.social_auth_by_name_backends',
# )


import random
# Если имя не удалось получить, то можно его сгенерировать
SOCIAL_AUTH_DEFAULT_USERNAME = lambda: random.choice(['Darth_Vader', 'Obi-Wan_Kenobi', 'R2-D2', 'C-3PO', 'Yoda'])
# Разрешаем создавать пользователей через social_auth
SOCIAL_AUTH_CREATE_USERS = True

# Перечислим pipeline, которые последовательно буду обрабатывать респонс
SOCIAL_AUTH_PIPELINE = (
    # Получает по backend и uid инстансы social_user и user
    'social_auth.backends.pipeline.social.social_auth_user',
    # Получает по user.email инстанс пользователя и заменяет собой тот, который получили выше.
    # Кстати, email выдает только Facebook и GitHub, а Vkontakte и Twitter не выдают
    'social_auth.backends.pipeline.associate.associate_by_email',
    # Пытается собрать правильный username, на основе уже имеющихся данных
    'social_auth.backends.pipeline.user.get_username',
    # Создает нового пользователя, если такого еще нет
    'social_auth.backends.pipeline.user.create_user',
    # Пытается связать аккаунты
    'social_auth.backends.pipeline.social.associate_user',
    # Получает и обновляет social_user.extra_data
    'social_auth.backends.pipeline.social.load_extra_data',
    # Обновляет инстанс user дополнительными данными с бекенда
    'social_auth.backends.pipeline.user.update_user_details'
)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'registration',
    'social_auth',
    'djcelery',

    'registr',
    'questions',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'djbook.urls'

WSGI_APPLICATION = 'djbook.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS = ()
for root, dirs, files in os.walk(BASE_DIR):
    if 'static' in dirs: STATICFILES_DIRS += (os.path.join(root, 'static'),)

# TEMPLATE_DIRS = (
#     os.path.join(BASE_DIR,  'templates'),
#
# )
TEMPLATE_DIRS = ()
for root, dirs, files in os.walk(BASE_DIR):
    if 'templates' in dirs: TEMPLATE_DIRS += (os.path.join(root, 'templates'),)


# адрес redis сервера
BROKER_URL = 'redis://localhost:6379/0'
# храним результаты выполнения задач так же в redis
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
# в течение какого срока храним результаты, после чего они удаляются
CELERY_TASK_RESULT_EXPIRES = 7*86400  # 7 days
# это нужно для мониторинга наших воркеров
CELERY_SEND_EVENTS = True
# место хранения периодических задач (данные для планировщика)
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"

# в конец settings.py добавляем строчки
import djcelery
djcelery.setup_loader()

TEST_RUNNER = 'django_coverage.coverage_runner.CoverageRunner'