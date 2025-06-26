# Task Manager API

A simple FastAPI-based task management API that supports creating, reading, updating, and deleting tasks. Tasks are stored in memory (Python list) and validated using Pydantic models and Enums.

## Features
- List all tasks
- Create a new task with title, description, status, and priority
- Update an existing task by ID
- Delete a task by ID
- Data validation for status and priority fields
- Interactive API docs via Swagger UI

## Requirements
- Python 3.10+
- FastAPI
- Uvicorn

## Installation & Running
1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/task-manager-api.git
   cd task-manager-api
   ```
2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the server:**
   ```sh
   uvicorn main:app --reload
   ```
5. **Open your browser to:**
   [http://localhost:8000/docs](http://localhost:8000/docs) (Swagger UI)

## Example API Usage
### Create a Task
```json
POST /tasks
{
  "title": "Buy groceries",
  "description": "Milk, Bread, Eggs",
  "status": "pending",
  "priority": "medium"
}
```

### List All Tasks
```http
GET /tasks
```

### Update a Task
```json
PUT /tasks/1
{
  "status": "completed"
}
```

### Delete a Task
```http
DELETE /tasks/1
```

## Status & Priority Values
- **Status:** `pending`, `in_progress`, `completed`
- **Priority:** `low`, `medium`, `high`

---

## License
MIT
