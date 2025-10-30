import os
import requests
from flask import Flask

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")
NTFY_TOPIC = os.environ.get("NTFY_TOPIC")
LAST_UPDATE_ID = 0  # deploy sonrası resetlenir

def send_notification(title, message):
    requests.post(f"https://ntfy.sh/{NTFY_TOPIC}", json={"title": title, "message": message})

def check_updates():
    global LAST_UPDATE_ID
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    params = {"timeout": 10, "offset": LAST_UPDATE_ID + 1}
    response = requests.get(url, params=params).json()

    for update in response.get("result", []):
        LAST_UPDATE_ID = update["update_id"]
        if "channel_post" in update:
            post = update["channel_post"]
            text = post.get("text", "")
            if "Son 6 Ayın En Düşük Fiyatı" in text or "Son 1 Yılın En Düşük Fiyatı" in text:
                send_notification("Yeni Telegram Paylaşımı", text)

@app.route("/api/check")
def api_check():
    check_updates()
    return {"status": "ok"}
