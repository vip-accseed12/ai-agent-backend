from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Agent Backend Running 🚀"


@app.route("/v1/chat/completions", methods=["POST"])
def chat_completions():
    try:
        data = request.get_json()

        messages = data.get("messages", [])

        response = requests.post(
            "https://gen.pollinations.ai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('POLLINATIONS_API_KEY')}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai",
                "messages": messages
            }
        )

        return jsonify(response.json())

    except Exception as e:
        return jsonify({"error": str(e)}), 500
