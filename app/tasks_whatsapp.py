# app/tasks_whatsapp.py
from app.celery_worker import celery

@celery.task(name="app.tasks_whatsapp.send_via_whatsapp")
def send_via_whatsapp(to: str, message: str, account_id: str):
    print(f"[WA] Sending to {to} | {account_id}: {message}")
    return {"status": "sent", "to": to, "account_id": account_id}