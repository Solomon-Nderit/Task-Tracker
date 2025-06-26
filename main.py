from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"

class TaskPriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class TaskCreate(BaseModel):
  title:str
  description:str | None
  status: TaskStatus
  priority: TaskPriority
 
class TaskUpdate(BaseModel):
  title:str | None
  description:str | None
  status: TaskStatus | None
  priority: TaskPriority | None

class Task(BaseModel):
    id: int
    title: str
    description: str | None = None
    status: TaskStatus
    priority: TaskPriority

tasks: list[Task] = []
next_id=1


@app.get('/tasks')
def get_all_tasks():
  return tasks

@app.post('/tasks', response_model=Task, status_code=status.HTTP_201_CREATED)
def post_tasks(task: TaskCreate):
    global next_id
    new_task = Task(
        id=next_id,
        title=task.title,
        description=task.description,
        status=task.status,
        priority=task.priority
    )
    tasks.append(new_task)
    next_id += 1
    return new_task



@app.put('/tasks/{id}', response_model=Task)
def update_task(id: int, task_update: TaskUpdate):
    for idx, task in enumerate(tasks):
        if task.id == id:
            updated_data = task.dict()
            update_fields = task_update.dict(exclude_unset=True)
            updated_data.update(update_fields)
            updated_task = Task(**updated_data)
            tasks[idx] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

# Delete a task by ID
@app.delete('/tasks/{id}', status_code=204)
def delete_task(id: int):
    for idx, task in enumerate(tasks):
        if task.id == id:
            tasks.pop(idx)
            return
    raise HTTPException(status_code=404, detail="Task not found")
  
 