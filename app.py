"""
To-Do List Web App — Python / Flask backend
===========================================
Routes:
  GET    /               → serve the HTML UI
  GET    /api/tasks       → list all tasks  (Read)
  POST   /api/tasks       → create a task   (Create)
  PUT    /api/tasks/<id>  → update a task   (Update)
  DELETE /api/tasks/<id>  → delete a task   (Delete)

Storage: tasks.json  (same format as the original CLI script)
Run:     python app.py        → http://127.0.0.1:5000
"""

import json
import os
from datetime import datetime
from flask import Flask, jsonify, request, render_template, abort

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")


# ─── Storage helpers (same logic as original CLI) ───────────────────────────

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def next_id(tasks):
    return max((t["id"] for t in tasks), default=0) + 1


def find_task(tasks, task_id):
    return next((t for t in tasks if t["id"] == task_id), None)


# ─── Routes ─────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    """Serve the main HTML UI."""
    return render_template("index.html")


# READ – list all tasks
@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks)


# CREATE – add a new task
@app.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.get_json(silent=True) or {}
    title = (data.get("title") or "").strip()
    if not title:
        return jsonify({"error": "Title is required."}), 400

    tasks = load_tasks()
    task = {
        "id":         next_id(tasks),
        "title":      title,
        "done":       False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    tasks.append(task)
    save_tasks(tasks)
    return jsonify(task), 201


# UPDATE – edit title and/or status
@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    tasks = load_tasks()
    task  = find_task(tasks, task_id)
    if not task:
        abort(404)

    data = request.get_json(silent=True) or {}

    new_title = (data.get("title") or "").strip()
    if new_title:
        task["title"] = new_title

    if "done" in data and isinstance(data["done"], bool):
        task["done"] = data["done"]

    save_tasks(tasks)
    return jsonify(task)


# DELETE – remove a task
@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks = load_tasks()
    task  = find_task(tasks, task_id)
    if not task:
        abort(404)

    tasks.remove(task)
    save_tasks(tasks)
    return jsonify({"message": f"Task #{task_id} deleted."})


# ─── Entry point ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("\n  ✅ To-Do List running → http://127.0.0.1:5000\n")
    app.run(debug=True, port=5000)
