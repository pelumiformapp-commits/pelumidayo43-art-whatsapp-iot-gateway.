from flask import Flask, request, jsonify
app = Flask(__name__)
relay_status = 0

@app.route("/")
def home():
    return jsonify({"relay_status": relay_status})

@app.route("/api/relay_status", methods=["POST"])
def update():
    global relay_status
    relay_status = 1
    return jsonify({"message": "Updated"}), 200

if __name__ == "__main__":
    app.run()
