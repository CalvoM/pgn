import os

from celery import Celery

_ = os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pgn_web.settings")

app = Celery("pgn_web")
_ = app.config_from_object("django.conf:settings", namespace="CELERY")
_ = app.autodiscover_tasks()
