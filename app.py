import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Configure Gemini
genai.configure(api_key=api_key)

# Initialize model (UPDATED MODEL NAME)
model = genai.GenerativeModel("models/gemini-2.5-flash")

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()

        genre = data.get("genre")
        characters = data.get("characters")
        setting = data.get("setting")
        tone = data.get("tone")
        length = data.get("length")

        if not all([genre, characters, setting, tone, length]):
            return jsonify({"error": "All fields are required"}), 400

        prompt = f"""
You are a professional comic script writer.

Create a structured comic story script with the following details:

Genre: {genre}
Characters: {characters}
Setting: {setting}
Tone: {tone}
Story Length: {length}

Format the output clearly as:

Title:

Characters:
- Name:
  Description:

Comic Script:

Panel 1:
Scene Description:
Dialogue:

Panel 2:
Scene Description:
Dialogue:

Continue appropriately based on story length.
"""

        response = model.generate_content(prompt)

        return jsonify({
            "success": True,
            "comic": response.text
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)