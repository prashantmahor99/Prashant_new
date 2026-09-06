import hashlib
import json
import os
import uuid

from dotenv import load_dotenv
from flask import Flask, jsonify, redirect, render_template, request, url_for
from pymongo import MongoClient

load_dotenv()

app = Flask(__name__)


def get_collection():
    mongo_uri = os.getenv("MONGO_URI")
    if not mongo_uri:
        raise RuntimeError("MONGO_URI is not configured. Copy .env.example to .env and add your MongoDB Atlas URI.")
    client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
    db = client[os.getenv("MONGO_DB", "devops_assignment")]
    return db[os.getenv("MONGO_COLLECTION", "todos")]


@app.route("/api", methods=["GET"])
def api():
    with open("data/api_data.json", "r", encoding="utf-8") as file:
        payload = json.load(file)
    return jsonify(payload)


@app.route("/", methods=["GET"])
def home():
    return render_template("todo.html", error=None)


@app.route("/submitto", methods=["POST"])
def submit_todo():
    item_name = request.form.get("item_name", "").strip()
    item_description = request.form.get("item_description", "").strip()
    item_id = request.form.get("item_id", "").strip()
    item_uuid = request.form.get("item_uuid", "").strip()
    item_hash = request.form.get("item_hash", "").strip()

    if not all([item_name, item_description, item_id, item_uuid, item_hash]):
        return render_template("todo.html", error="All fields are required."), 400

    document = {
        "item_name": item_name,
        "item_description": item_description,
        "item_id": item_id,
        "item_uuid": item_uuid,
        "item_hash": item_hash,
    }

    try:
        get_collection().insert_one(document)
        return redirect(url_for("success"))
    except Exception as exc:
        return render_template("todo.html", error=f"Database error: {exc}"), 500


@app.route("/success", methods=["GET"])
def success():
    return render_template("success.html")


@app.route("/generate-values", methods=["GET"])
def generate_values():
    generated_uuid = str(uuid.uuid4())
    generated_hash = hashlib.sha256(generated_uuid.encode("utf-8")).hexdigest()
    return jsonify({"uuid": generated_uuid, "hash": generated_hash})


if __name__ == "__main__":
    app.run(debug=True)
