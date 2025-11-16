from flask import Flask, request, jsonify
from services import chat

app = Flask(__name__)
# localhost:3001

@app.route("/", methods=["POST"])
def prompt():
    user_input = request.json["data"]
    return jsonify(chat(user_input))
    






















# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from openai import OpenAI


# # מאתחל את Flask
# app = Flask(__name__)
# CORS(app)

# # יוצר לקוח של OpenAI
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# @app.route("/chat", methods=["POST"])
# def chat():
#     data = request.get_json()
#     user_message = data.get("message", "")

#     if not user_message:
#         return jsonify({"error": "No message provided"}), 400

#     try:
#         # שולח בקשה למודל GPT
#         response = client.chat.completions.create(
#             model="gpt-3.5-turbo",  # או "gpt-4o-mini" אם יש לך גישה
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": user_message}
#             ],
#             max_tokens=100,
#             temperature=0.7
#         )

#         bot_reply = response.choices[0].message.content.strip()
#         return jsonify({"reply": bot_reply})

#     except Exception as e:
#         print("Error:", e)
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(port=3001)
