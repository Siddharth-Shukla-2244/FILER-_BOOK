from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/books")
def books():
    with open("books.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)

