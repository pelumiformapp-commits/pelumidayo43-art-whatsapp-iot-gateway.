from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
relay_status = 0  # Start at 0

# Green API details
GREEN_API_ID = "710722686160"
GREEN_API_TOKEN = "540ff7115d1f4c769b9ea7bddcf0433c17b73f8a5035492385"
GREEN_API_URL = f"https://7107.api.greenapi.com/waInstance{GREEN_API_ID}"

def send_whatsapp_reply(chat_id, message):
    url = f"{GREEN_API_URL}/sendMessage/{GREEN_API_TOKEN}"
    payload = {"chatId": chat_id, "message": message}
    requests.post(url, json=payload)

@app.route('/')
def home():
    return jsonify({"relay_status": relay_status})

@app.route('/api/relay_status', methods=['GET'])
def get_status():
    return jsonify({"relay_status": relay_status})

@app.route('/api/relay_status', methods=['POST'])
def update_status():
    global relay_status
    relay_status = 1 if relay_status == 0 else 0  # Toggles 0->1
    return jsonify({"message": "Updated", "new_status": relay_status})

@app.route('/webhook', methods=['POST'])
def webhook():
    global relay_status
    data = request.get_json()

    try:
        message_data = data.get('messageData', {})
        text_data = message_data.get('textMessageData', {})
        text = text_data.get('textMessage', '').lower().strip()
        chat_id = data.get('senderData', {}).get('chatId')

        if text == 'relay on':
            relay_status = 1
            send_whatsapp_reply(chat_id, "✅ Relay turned ON")
        elif text == 'relay off':
            relay_status = 0
            send_whatsapp_reply(chat_id, "✅ Relay turned OFF")
    except Exception as e:
        print("Webhook error:", e)

    return jsonify({"ok": True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
