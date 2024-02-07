import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cfehome.settings')

app = Celery()

