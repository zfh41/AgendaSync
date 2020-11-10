import flask_sqlalchemy
from app import db
from datetime import datetime


class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    todo = db.Column(db.String(255))
    start_todo = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.DateTime)
    profile_picture = db.Column(db.String(200))
    id_token = db.Column(db.String(255))
    
    def __init__(self, name, email, todo, start_todo, due_date, profile_picture, id_token):
        self.name = name
        self.email = email
        self.todo = todo
        self.start_todo = start_todo
        self.due_date = due_date
        self.profile_picture = profile_picture
        self.id_token = id_token
        
    def __repr__(self):
        return '<Todo %s>' % self.todo 