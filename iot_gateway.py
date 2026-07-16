from flask import Flask, jsonify

app = Flask(__name__)
relay_status = 0

@app.route('/')
def home():
    return "IoT Gateway is Live"

@app.route('/hardware/api')
def get_status():
    return jsonify({"relay_status": relay_status})

@app.route('/turn_on')
def turn_on():
    global relay_status
    relay_status = 1
    return jsonify({"message": "Relay ON", "relay_status": relay_status})

@app.route('/turn_off')
def turn_off():
    global relay_status
    relay_status = 0
    return jsonify({"message": "Relay OFF", "relay_status": relay_status})
