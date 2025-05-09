from app.celery_worker import celery
import requests

@celery.task(name="app.tasks_whatsapp.send_via_whatsapp")
def send_via_whatsapp(to, message, account_id):
    print(f"[WA] Sending to {to} | {account_id}: {message}")
    # Replace with actual WhatsApp API logic
