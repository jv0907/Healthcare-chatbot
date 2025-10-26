from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.json["message"].lower()

    # --- Rule-based symptom logic (can be replaced with Dialogflow/ML) ---
    if "fever" in user_input:
        reply = "🌡️ It seems like a mild fever. Stay hydrated, take rest, and consult a doctor if it persists for 3+ days."
    elif "headache" in user_input:
        reply = "😣 Try to rest, drink water, and avoid bright screens. If severe or recurring, consult a doctor."
    elif "cough" in user_input:
        reply = "🤧 It could be a common cold or allergy. Drink warm fluids and avoid cold exposure."
    elif "stomach" in user_input or "pain" in user_input:
        reply = "🥴 Possibly indigestion. Eat light, avoid spicy food, and drink plenty of water."
    elif "tired" in user_input or "fatigue" in user_input:
        reply = "💤 You might be lacking sleep or nutrients. Rest well and maintain a healthy diet."
    elif "cold" in user_input:
        reply = "🌬️ Sounds like a common cold. Rest, drink warm liquids, and stay cozy."
    elif "thank" in user_input:
        reply = "😊 You're very welcome! Take care of your health."
    elif "help" in user_input:
        reply = "💬 Sure! Tell me your symptoms like 'I have a fever' or 'My head hurts'."
    else:
        reply = "⚕️ Could you please describe your symptoms a bit more clearly?"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
