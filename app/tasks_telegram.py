from app.celery_worker import celery
import requests

@celery.task(name="app.tasks_telegram.send_via_telegram")
def send_via_telegram(to, message, account_id):
    print(f"[TG] Sending to {to} | {account_id}: {message}")
    # Replace with actual Telegram Bot API logic
