import os
from flask import Flask, jsonify, request

app = Flask("iot_gateway")

# Global variable to store the relay state (0 = OFF, 1 = ON)
relay_state = 0

@app.route('/hardware/api', methods=['GET', 'POST'])
def hardware_api():
    global relay_state
    
    # 1. ESP32 checks this to see if it should turn ON or OFF
    if request.method == 'GET':
        return jsonify({"relay_status": relay_state}), 200

    # 2. WhatsApp sends a POST command to change the state
    if request.method == 'POST':
        data = request.get_json(silent=True) or request.form
        command = data.get('command', '').upper() or data.get('Body', '').upper()
        
        if 'ON' in command:
            relay_state = 1
            return jsonify({"status": "success", "relay_status": 1, "message": "Relay turned ON"}), 200
        elif 'OFF' in command:
            relay_state = 0
            return jsonify({"status": "success", "relay_status": 0, "message": "Relay turned OFF"}), 200
        else:
            return jsonify({"status": "error", "message": "Invalid command"}), 400

app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

