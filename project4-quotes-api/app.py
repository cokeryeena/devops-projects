from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "Stay hungry, stay foolish.",
    "Discipline equals freedom.",
    "What you do today matters.",
    "Boyyeena, born to create."
]

@app.route('/api/quote', methods=['GET'])
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
