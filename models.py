import flask_sqlalchemy
import app
# from app import db
import datetime
db = app.db
start_date = datetime.datetime.utcnow()
end_date = start_date + datetime.timedelta(days=1)
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    todos = db.relationship('Todo', backref='person', lazy='dynamic' ) #uselist=False
    cred = db.Column(db.PickleType)
    phone = db.Column(db.String(20))
    
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    todo = db.Column(db.String(255), nullable=False)
    start_todo = db.Column(db.DateTime, default=start_date)
    due_date = db.Column(db.DateTime, default=end_date)

db.create_all()