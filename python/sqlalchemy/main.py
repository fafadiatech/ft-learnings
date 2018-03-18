from models import init, engine, Task, TaskLog
from sqlalchemy.orm import sessionmaker

# create a session {this will be used to storing objects onto DB}
Session = sessionmaker(bind=engine)
session = Session()

# initialize the model {this will create DB}
init()

# create an object and persist to DB via session

dummy_task = Task(id=1, title="Some Fancy Task", completed=True)
dummy_task.log = [TaskLog(logged_hours=2)]
session.add(dummy_task)

# add some more data
for i in range(2, 5):
    task_title = "Some Fancy Task:%s" % i
    dummy_task = Task(id=i, title=task_title, completed=False)
    dummy_task.log = [TaskLog(logged_hours=i)]
    session.add(dummy_task)

# note without this the persistance won't happen
session.commit()

# To query DB this is how its done
print "Pending Tasks:"
for task in session.query(Task).filter_by(completed=False):
    print task

