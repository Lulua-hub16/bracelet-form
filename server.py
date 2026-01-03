from flask import Flask, request, send_from_directory
import json
import os

app = Flask(__name__)

DATA_FILE = "orders.json"

# Ensure file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

@app.route("/")
def form():
    return send_from_directory("public", "index.html")

@app.route("/submit", methods=["POST"])
def submit():
    new_order = request.form.to_dict()

    with open(DATA_FILE, "r") as f:
        orders = json.load(f)

    orders.append(new_order)

    with open(DATA_FILE, "w") as f:
        json.dump(orders, f, indent=2)

    return "<h2>Order received! Thank you 💖</h2>"

@app.route("/orders")
def view_orders():
    with open(DATA_FILE, "r") as f:
        return json.dumps(json.load(f), indent=2)

app.run(host='0.0.0.0', port=10000)
