from app.celery_worker import celery

@celery.task(name="app.tasks_sms.send_via_sms")
def send_via_sms(to, message, account_id):
    print(f"[SMS] Sending to {to} | {account_id}: {message}")
    # Replace with actual SMS gateway (e.g., Jasmin) logic
