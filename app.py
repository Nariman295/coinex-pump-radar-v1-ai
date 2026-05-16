from flask import Flask, jsonify
from engine import scan_market

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 CoinEx Pump Radar Web App is Running"

@app.route("/signals")
def signals():
    top3 = scan_market()

    return jsonify([
        {"coin": coin, "score": score}
        for coin, score in top3
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
