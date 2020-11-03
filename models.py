import flask_sqlalchemy
from app import db


class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    todo = db.Column(db.String(255))
    profile_picture = db.Column(db.String(200))
    id_token = db.Column(db.String(255))
    
    def __init__(self, name, email, todo, profile_picture, id_token):
        self.name = name
        self.email = email
        self.todo = todo
        self.profile_picture = profile_picture
        self.id_token = id_token
        
    def __repr__(self):
        return '<Todo %s>' % self.todo 