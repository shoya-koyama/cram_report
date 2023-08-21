from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

CHANNEL_ACCESS_TOKEN = "YOUR_CHANNEL_ACCESS_TOKEN"
API_URL = "https://api.line.me/v2/bot/message/reply"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    reply_token = data["events"][0]["replyToken"]
    user_message = data["events"][0]["message"]["text"]
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}"
    }
    
    payload = {
        "replyToken": reply_token,
        "messages": [{
            "type": "text",
            "text": f"You said: {user_message}"
        }]
    }
    
    response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
    return jsonify({}), 200

if __name__ == "__main__":
    app.run(port=8000)
