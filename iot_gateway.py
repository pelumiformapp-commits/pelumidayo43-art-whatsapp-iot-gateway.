from flask import Flask, jsonify

app = Flask(__name__)
relay_status = 0  # Start at 0

@app.route('/')
def home():
    return jsonify({"relay_status": relay_status})

@app.route('/api/relay_status', methods=['GET'])
def get_status():
    return jsonify({"relay_status": relay_status})

@app.route('/api/relay_status', methods=['POST'])
def update_status():
    global relay_status
    relay_status = 1 if relay_status == 0 else 0  # Toggles 0↔1
    return jsonify({"message": "Updated", "new_status": relay_status})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
