# ✅ To-Do List App

A full-stack **To-Do List** web application built with **Python (Flask)** as the backend and **HTML/CSS/JavaScript** as the frontend. Tasks are stored in a local `tasks.json` file.

## 🚀 Features

- ➕ **Create** — Add new tasks
- 📋 **Read** — View all tasks with filter tabs (All / Pending / Done)
- ✏️ **Update** — Edit title or toggle status (done / pending)
- 🗑️ **Delete** — Remove tasks with confirmation
- 🔍 **Search** — Live search through tasks
- 📊 **Stats** — Total / Pending / Done counters + progress bar
- 💾 **Persistent** — Data saved to `tasks.json`
- 🔔 **Toast Notifications** — Instant feedback on every action

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3 + Flask |
| Frontend | HTML5, CSS3, JavaScript |
| Storage | JSON file (`tasks.json`) |
| API | REST (GET / POST / PUT / DELETE) |

## 📁 Project Structure

```
DO-LIST/
├── app.py                 # Flask backend — CRUD routes + JSON storage
├── tasks.json             # Auto-created on first task add
├── templates/
│   └── index.html         # Frontend UI
├── .gitignore
└── README.md
```

## ⚙️ Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/Darshil64/todo-list-app.git
cd todo-list-app
```

### 2. Install Flask
```bash
pip install flask
```

### 3. Run the app
```bash
python app.py
```

### 4. Open in browser
```
http://127.0.0.1:5000
```

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/tasks` | List all tasks |
| `POST` | `/api/tasks` | Create a new task |
| `PUT` | `/api/tasks/<id>` | Update title / status |
| `DELETE` | `/api/tasks/<id>` | Delete a task |

## 📸 Screenshot

> A clean, modern UI with gradient background, stats bar, filter tabs, live search, and smooth animations.

---

Made with 🐍 Python + Flask
