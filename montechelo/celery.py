import os

from celery import Celery
from celery.schedules import crontab

from django.conf import settings

# this code copied from manage.py
# set the default Django settings module for the 'celery' app.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'montechelo.settings')

# you can change the name here
celery_app = Celery("montechelo-api")

# read config from Django settings, the CELERY namespace would make celery
# config keys has `CELERY` prefix
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# discover and load tasks.py from all registered Django apps
celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

celery_app.conf.beat_schedule = {
    
}
