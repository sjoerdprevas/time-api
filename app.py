from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def get_time():
    now = datetime.utcnow()
    return jsonify({
        "datetime": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "unixtime": int(now.timestamp())
    })

if __name__ == "__main__":
    app.run()
