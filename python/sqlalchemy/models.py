# Example file on how to use SQLAlchemy

from sqlalchemy import (
                        create_engine, ForeignKey, Column,
                        Integer, String, Boolean)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# This is the engine instance, here is where
# we can configure different Storage vendors
engine = create_engine('sqlite:///todos.sqlite3')

# This is declarative base kind of like models.Model
# All the classes that we will be using for mapping 
# will inherit from this
Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    completed = Column(Boolean, default=False)
    log = relationship("TaskLog", back_populates="log")

    def __repr__(self):
        return "<Todo: id=%s, title=%s, completed=%s>" % (self.id, self.title, self.completed)

class TaskLog(Base):
    __tablename__ = "task_logs"

    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey('tasks.id'))
    log = relationship("Task", back_populates="log")
    logged_hours = Column(Integer, default=1)

    def __repr__(self):
        return "<TaskLog: id=%s, task_id=%s, logged_hours=%s>" % (self.id, self.task_id, self.logged_hours)

def init():
    """
    this function is used for initialising all DB tables
    """
    Base.metadata.create_all(engine)