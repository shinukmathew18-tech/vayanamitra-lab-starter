import os
from dotenv import load_dotenv
from flask import Flask, jsonify, redirect, url_for
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return redirect(url_for("health_check"))


@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "ok",
        "project": "vaynamitra-lab-starter",
        "message": "Flask backend is running smoothly."
    }), 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)