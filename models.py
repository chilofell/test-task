from sqlalchemy import Column, Integer, String

from .database import Base


# модель дaнных
class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    task_uuid = Column(String)
    description = Column(String)
    param_1 = Column(String)
    param_2 = Column(Integer)


# def print(self):
#     print(
#         str(self.id) + " --- " + self.task_uuid + " --- " + self.description + " --- " + self.param_1 + " --- " + str(
#             self.param_2))
