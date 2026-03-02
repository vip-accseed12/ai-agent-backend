from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Agent Backend Running 🚀"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt")

    response = requests.post(
        "https://api.pollinations.ai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('POLLINATIONS_API_KEY')}",
            "Content-Type": "application/json"
        },
        json={
            "model": "kimi-k2",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )

    return jsonify(response.json())

if __name__ == "__main__":
    app.run()
