from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advanceDjango.settings')

app = Celery('advanceDjango',
             broker='redis://:1qaz2wsx@47.102.218.113:6379//9',)
             # backend='redis://:1qaz2wsx@47.102.218.113:6379//8')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY') # 配置Celery， 加载settings.py

# Load task modules from all registered Django app configs.
app.autodiscover_tasks() # 自动发现task任务


