from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Agent Backend Running 🚀"


@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()

        if not data or "prompt" not in data:
            return jsonify({"error": "Prompt is required"}), 400

        prompt = data["prompt"]

        response = requests.post(
            "https://gen.pollinations.ai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('POLLINATIONS_API_KEY')}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai",
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }
        )

        pollination_response = response.json()

        return jsonify({
            "reply": pollination_response["choices"][0]["message"]["content"]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
