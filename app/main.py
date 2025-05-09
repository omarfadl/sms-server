from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.tasks_whatsapp import send_via_whatsapp
from app.tasks_telegram import send_via_telegram
from app.tasks_google import send_via_google
from app.tasks_sms import send_via_sms

app = FastAPI()

class MessageRequest(BaseModel):
    to: str
    message: str
    account_id: str
    channel: str  # "whatsapp", "telegram", "sms"

@app.post("/send")
async def send_message(req: MessageRequest):
    if req.channel == "whatsapp":
        send_via_whatsapp.apply_async((req.to, req.message, req.account_id), queue="whatsapp_queue")
    elif req.channel == "telegram":
        send_via_telegram.apply_async((req.to, req.message, req.account_id), queue="telegram_queue")
    elif req.channel=="google":
        send_via_google.apply_async((req.to, req.message, req.account_id), queue="google_queue")
    elif req.channel == "sms":
        send_via_sms.apply_async((req.to, req.message, req.account_id), queue="sms_queue")
    else:
        raise HTTPException(status_code=400, detail="Unsupported channel")

    return {"status": "queued", "to": req.to, "channel": req.channel}
