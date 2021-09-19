from todolist import db
from datetime import datetime
class Tasks(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(80), unique=True, nullable=False)
    time_set = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    complete = db.Column(db.Boolean)

    def __repr__(self):
        return f"Task({self.task}, {self.time_set})"


