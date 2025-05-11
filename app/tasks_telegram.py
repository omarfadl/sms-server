from app.celery_worker import celery
import os
import requests

TELEGRAM_GATEWAY_TOKEN = os.getenv("TELEGRAM_GATEWAY_TOKEN")
END_POINT_SEND_VERIFICATION_MESSAGE="sendVerificationMessage"

@celery.task(name="app.tasks_telegram.send_via_telegram")
def send_via_telegram(to: str, code: str, account_id: str):
    print(f"[Telegram] Sending OTP to {to} | {account_id}: {code}")

    url = "https://gatewayapi.telegram.org/sendVerificationMessage"
    headers = {
        "Authorization": f"Bearer {TELEGRAM_GATEWAY_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "phone_number": to,
        "code": code,
        "ttl": 300,
        "payload": account_id
    }

    try:
        response = requests.post(url, headers=headers, json=data,timeout=10)
        response.raise_for_status()
        result = response.json()
        print(f"[Telegram] API response: {result}")
        return result
    except requests.RequestException as e:
        print(f"[Telegram] Failed to send OTP: {e}")
        return {"status": "error", "reason": str(e)}
