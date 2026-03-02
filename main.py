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
        data = request.json
        prompt = data.get("prompt")

        response = requests.post(
            "https://gen.pollinations.ai/v1/chat/completions",
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

        return jsonify({
            "status_code": response.status_code,
            "raw_response": response.text
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
