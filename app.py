from flask import Flask, jsonify
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)

@app.route("/")
def time():
    now = datetime.now(ZoneInfo("Europe/Stockholm"))
    return jsonify({
        "datetime": now.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "timezone": "Stockholm, Sweden",
        "unixtime": int(now.timestamp())
    })

app.run(host="0.0.0.0", port=81)
