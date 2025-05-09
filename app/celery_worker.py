from celery import Celery

celery = Celery(
    "worker",
    broker="amqp://guest:guest@rabbitmq:5672//",
    backend="rpc://"
)

celery.conf.task_routes = {
    'app.tasks_whatsapp.send_via_whatsapp': {'queue': 'whatsapp_queue'},
    'app.tasks_telegram.send_via_telegram': {'queue': 'telegram_queue'},
    'app.tasks_sms.send_via_sms': {'queue': 'sms_queue'},
}
