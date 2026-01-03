from flask import Flask, request, jsonify, send_from_directory
import random
import os

app = Flask(__name__)

# 😃 Emotion detection + responses
EMOTIONS = {
    "happy": {
        "keywords": ["happy", "great", "awesome", "excited", "good"],
        "responses": [
            "That’s wonderful to hear! 😄",
            "I’m glad you’re feeling happy! 🌟",
            "Nice! Positive vibes only 🚀"
        ]
    },
    "sad": {
        "keywords": ["sad", "down", "unhappy", "low", "depressed"],
        "responses": [
            "I’m sorry you’re feeling this way 😔",
            "It’s okay to feel sad sometimes. You’re not alone 🤍",
            "Want to talk about what’s bothering you?"
        ]
    },
    "stress": {
        "keywords": ["stressed", "tired", "pressure", "overwhelmed"],
        "responses": [
            "That sounds stressful 😞",
            "Take a deep breath — you’re doing your best 💙",
            "Short breaks can really help during stress."
        ]
    },
    "angry": {
        "keywords": ["angry", "mad", "frustrated", "annoyed"],
        "responses": [
            "I sense some frustration 😕",
            "That sounds upsetting. Want to vent?",
            "Let’s slow things down for a moment."
        ]
    },
    "anxious": {
        "keywords": ["anxious", "worried", "nervous", "scared"],
        "responses": [
            "It’s okay to feel anxious 🤍",
            "You’re safe here. Want to talk it out?",
            "Slow breathing can help calm anxiety."
        ]
    }
}

# 🧠 General intents
INTENTS = {
    "greeting": {
        "keywords": ["hi", "hello", "hey"],
        "responses": [
            "Hello! 👋 How are you feeling today?",
            "Hi there! 😊",
            "Hey! Hope you’re doing well."
        ]
    },
    "name": {
        "keywords": ["your name", "who are you"],
        "responses": [
            "I’m an emotion-aware demo chatbot 🤖",
            "You can call me DemoBot."
        ]
    },
    "capabilities": {
        "keywords": ["what can you do", "help"],
        "responses": [
            "I can respond to emotions and demo questions.",
            "I simulate an empathetic chatbot for demos."
        ]
    },
    "thanks": {
        "keywords": ["thanks", "thank you"],
        "responses": [
            "You’re welcome 😊",
            "Anytime! Glad I could help."
        ]
    },
    "bye": {
        "keywords": ["bye", "goodbye"],
        "responses": [
            "Goodbye 👋 Take care!",
            "See you soon. Stay well 🤍"
        ]
    }
}

# 🌐 Routes
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/style.css")
def style():
    return send_from_directory(".", "style.css")

@app.route("/get", methods=["POST"])
def chatbot_response():
    data = request.get_json(silent=True)
    if not data or "msg" not in data:
        return jsonify({"reply": "I didn’t catch that 🤔"})

    user_msg = data["msg"].lower().strip()

    # 🔍 Emotion detection
    for emotion in EMOTIONS.values():
        for keyword in emotion["keywords"]:
            if keyword in user_msg:
                return jsonify({
                    "reply": random.choice(emotion["responses"])
                })

    # 🔍 Intent detection
    for intent in INTENTS.values():
        for keyword in intent["keywords"]:
            if keyword in user_msg:
                return jsonify({
                    "reply": random.choice(intent["responses"])
                })

    # 🤖 Fallback
    return jsonify({
        "reply": random.choice([
            "I’m here to listen 🤍",
            "Tell me more about how you’re feeling.",
            "This is a demo chatbot, but I care 😊"
        ])
    })

# 🚀 Deployment-ready run
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
