import flask_sqlalchemy
from app import db
import datetime

start_date = datetime.datetime.utcnow()
end_date = start_date + datetime.timedelta(days=1)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    todos = db.relationship('Todo', backref='person', lazy=True)
    
    def __init__(self, email):
        self.email = email
        
    def __repr__(self):
        return '<Person email %s>' % self.email

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'),
        nullable=False)
    todo = db.Column(db.String(255), nullable=False)
    start_todo = db.Column(db.DateTime, default=start_date)
    due_date = db.Column(db.DateTime, default=end_date)
    
    def __init__(self, todo, start_todo, due_date):
        self.todo = todo
        self.start_todo = start_todo
        self.due_date = due_date
        
    def __repr__(self):
        return '<Todo %s>' % self.todo

