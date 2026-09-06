from pathlib import Path

import environ


BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DJANGO_DEBUG=(bool, False),
    USE_SQLITE=(bool, True),
)

environ.Env.read_env(BASE_DIR / '.env')


SECRET_KEY = env('DJANGO_SECRET_KEY')

DEBUG = env.bool(
    'DJANGO_DEBUG',
    default=False,
)

ALLOWED_HOSTS = env.list(
    'DJANGO_ALLOWED_HOSTS',
    default=['127.0.0.1', 'localhost'],
)


USE_SQLITE = env.bool(
    'USE_SQLITE',
    default=True,
)

if USE_SQLITE:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env('POSTGRES_DB'),
            'USER': env('POSTGRES_USER'),
            'PASSWORD': env('POSTGRES_PASSWORD'),
            'HOST': env(
                'POSTGRES_HOST',
                default='db',
            ),
            'PORT': env(
                'POSTGRES_PORT',
                default='5432',
            ),
        }
    }