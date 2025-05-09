# app/celery_worker.py
from celery import Celery
import os

# Ensure the working directory is correctly set in the container
celery = Celery(
    "worker",
    broker="amqp://guest:guest@rabbitmq:5672//",
    backend="rpc://"
)

celery.conf.task_routes = {
    'app.tasks_whatsapp.send_via_whatsapp': {'queue': 'whatsapp_queue'},
    'app.tasks_telegram.send_via_telegram': {'queue': 'telegram_queue'},
    'app.tasks_telegram.send_via_google': {'queue': 'google_queue'},
    'app.tasks_sms.send_via_sms': {'queue': 'sms_queue'},
}

# Automatically discover tasks based on the 'app' module path
celery.autodiscover_tasks(['app.tasks_whatsapp', 'app.tasks_telegram', 'app.tasks_google','app.tasks_sms'])
