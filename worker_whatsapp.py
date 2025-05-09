# worker_whatsapp.py
from app.celery_worker import celery
from app import tasks_whatsapp  # Required for registration!