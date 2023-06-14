import uvicorn
# import psycopg2
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from fast_api import crud, models, schemas
from fast_api.database import SessionLocal, engine

# создание таблиц
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# создание задачи
@app.post("/task/add")
async def post_task(task: schemas.TaskBase, db: Session = Depends(get_db)):
    return crud.create_task(db, task)


# получение задач
@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db)
    if not tasks:
        raise HTTPException(status_code=404, detail="Tasks not found")
    return tasks


# изменение задачи
@app.put("/task/{task_id}")
def put_task(task_id: int, task: schemas.TaskBase, db: Session = Depends(get_db)):
    return crud.update_task(db, task_id, task)



if __name__ == '__main__':
    uvicorn.run("fast_api.main:app", host="127.0.0.1", port=8000, reload=True)
