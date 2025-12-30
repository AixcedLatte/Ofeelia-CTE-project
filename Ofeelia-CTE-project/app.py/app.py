from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "ofeelia-secret-key"

def detect_emotion(text):
    text = text.lower()

    if any(w in text for w in ["sad", "depressed", "empty", "hopeless"]):
        return "depression"
    elif any(w in text for w in ["stress", "pressure", "overwhelmed"]):
        return "stress"
    elif any(w in text for w in ["burnout", "exhausted", "tired"]):
        return "burnout"
    elif any(w in text for w in ["bullied", "harassed", "alone"]):
        return "bullying"
    elif any(w in text for w in ["happy", "okay", "fine", "good"]):
        return "happy"
    else:
        return "neutral"

def respond(emotion):
    responses = {
        "depression": [
            "I'm really glad you shared this. You're not weak for feeling this way.",
            "What you're feeling matters, and you deserve care and understanding."
        ],
        "stress": [
            "School pressure can be overwhelming. You're doing your best.",
            "It's okay to pause and take a breath."
        ],
        "burnout": [
            "Burnout happens when you've been strong for too long.",
            "Rest is not laziness — it's necessary."
        ],
        "bullying": [
            "What you're experiencing is not your fault.",
            "You deserve to feel safe and respected."
        ],
        "happy": [
            "I'm really happy to hear that!",
            "That's wonderful — thank you for sharing."
        ],
        "neutral": [
            "I'm here. You can tell me more if you'd like."
        ]
    }
    return random.choice(responses[emotion])

@app.route("/", methods=["GET", "POST"])
def home():
    if "chat" not in session:
        session["chat"] = []

    if request.method == "POST":
        user_msg = request.form["message"]
        emotion = detect_emotion(user_msg)
        bot_msg = respond(emotion)

        session["chat"].append(("You", user_msg))
        session["chat"].append(("Ofeelia", bot_msg))
        session.modified = True

    return render_template("index.html", chat=session["chat"])

if __name__ == "__main__":
    app.run()
