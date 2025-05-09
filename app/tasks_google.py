# app/tasks_whatsapp.py
from app.celery_worker import celery

@celery.task(name="app.tasks_google.send_via_google")
def send_via_google(to: str, message: str, account_id: str):
    print(f"[Google] Sending to {to} | {account_id}: {message}")
    return {"status": "sent", "to": to, "account_id": account_id}