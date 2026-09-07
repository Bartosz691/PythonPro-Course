import environ


env = environ.Env(
    USE_REDIS_CACHE=(bool, False),
)


USE_REDIS_CACHE = env.bool(
    'USE_REDIS_CACHE',
    default=False,
)

if USE_REDIS_CACHE:
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': env(
                'REDIS_CACHE_URL',
                default='redis://redis:6379/1',
            ),
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            },
        }
    }
else:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': 'music-fun-beats-local-cache',
        }
    }