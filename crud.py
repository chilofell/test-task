# import json
# from uuid import UUID

from sqlalchemy.orm import Session

from fast_api import models, schemas


def get_tasks(db: Session):
    return db.query(models.Task).all()


def get_task(db: Session, task_id: int) -> models.Task:
    return db.query(models.Task).get(task_id)


# создание новой задачи в базе данных на основе данных из объекта task
def create_task(db: Session, task: schemas.TaskBase):
    db_task = models.Task(task_uuid=task.uuid, description=task.description, param_1=task.params.param_1,
                          param_2=task.params.param_2)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


# обновить элемент базы данных по идентификатору task_id
def update_task(db: Session, task_id: int, task_update: schemas.TaskBase):
    db_task = get_task(db, task_id)
    if db_task is None:
        return None

    db_task.task_uuid = task_update.uuid
    db_task.description = task_update.description
    db_task.param_1 = task_update.params.param_1
    db_task.param_2 = task_update.params.param_2

    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

