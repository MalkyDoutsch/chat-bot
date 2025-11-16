from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# כתובת ה-backend שלך
BACKEND_URL = "http://localhost:3001/"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send_message():
    user_msg = request.json.get("message", "")
    try:
        # שולח את ההודעה ל-backend שלך
        res = requests.post(BACKEND_URL, json={"data": user_msg})
        data = res.json()
        return jsonify({"reply": data.get("msg", "No response")})
    except Exception as e:
        return jsonify({"reply": f"Error: {e}"})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
