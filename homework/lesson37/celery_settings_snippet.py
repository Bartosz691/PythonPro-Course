import environ

env = environ.Env(
    CELERY_TASK_ALWAYS_EAGER=(bool, True),
)

CELERY_BROKER_URL = env(
    'CELERY_BROKER_URL',
  default='redis://localhost:6379/0'
  
)

CELERY_RESULT_BACKEND = env(
    'CELERY_RESULT_BACKEND',
  default='redis://localhost:6379/2',
)

CELERY_TASK_ALWAYS_EAGER = env.bool(
    'CELERY_TASK_ALWAYS_EAGER',
  default=True,
)

CELERY_TASK_ROUTES = {
    'order.tasks.process_order': {
        'queue': 'orders',
    },
    'orders.tasks.send_order_notification': {
        'queue': 'notifications ',
    },
    'products.tasks.check_low_stock':{
        'queue': 'orders',
    },
}

CELERY_BEAT_SCHEDULE = {
    'check-low-stock-every-minute': {
        'task': 'products.tasks.check_low_stock',
        'schedule': 60.0,
        'options': {
          'queue': 'orders ',  
        },
    },
}