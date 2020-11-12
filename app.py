import os
from os.path import join, dirname
from twilio.rest import Client
import flask
from flask import request
import requests
import flask_socketio
import flask_sqlalchemy
from dotenv import load_dotenv
from twilio.twiml.messaging_response import MessagingResponse
import google.oauth2.credentials
import google_auth_oauthlib.flow
import datetime

USERS_UPDATED_CHANNEL = 'users updated'

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")
dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)
database_uri = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

db = flask_sqlalchemy.SQLAlchemy(app)
def init_db(app):
    db.init_app(app)
    db.app = app
    db.create_all()
    db.session.commit()

import models

@app.route('/', methods=['GET', 'POST'])
def hello():
    return flask.render_template('index.html')
#twilio
#ngrok http 5000

ADD_TODO = "add todo"
DELETE_TODO = "delete todo"
LIST_TODO = "list todo"
START_TODO = "start date"
DUE_DATE = "due date"

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'help me' in incoming_msg:
        msg.body("Hello! I'm the agendasync textbot! My know commands are: 'add todo', 'delete todo, 'list todo', 'start date', and 'due date'")
        responded = True
    if ADD_TODO in incoming_msg:
        message_body = incoming_msg[9:]
        add_new_todo_to_db(message_body)
        msg.body("Inserted: '" +  message_body + "' into your todolist!")
        responded = True
    if DELETE_TODO in incoming_msg:
        message_body = incoming_msg[12:]
        #TODO - delete 
        msg.body("Deleted: '" +  message_body + "' from your todolist!")
        responded = True
        
        #query for message_body in todolist table
        #if message_body not in table:
            #msg.body("The event '" + message_body "' cannot be found in your todo list!")
            #responded = True
        #else:
            #delete item from db todolist
        
        #message_emit("todolist update")
            
    if LIST_TODO in incoming_msg:
            msg.body("Your todolsit contents are as follows:")
            todoListString = ""
            #query database tables for todolist
            #for item in database:
            #    todoListString += (" * " + db.item + "\n")
            msg.body(todoListString)
            responded = True
            
    if START_TODO in incoming_msg:
        message_body = incoming_msg[11:]
        # query for message_body in todolist table
        #if message_body not in table:
            #msg.body("The event '" + message_body "' cannot be found in your todo list!")
            #responded = True
        #dbQuery = db.query
        msg.body("The start date of the event '" + message_body + "' is: ") # database query would go here
        responded = True
    
    if DUE_DATE in incoming_msg:
        message_body = incoming_msg[9:]
        # query for message_body in todolist table
        #if message_body not in table:
            #msg.body("The event '" + message_body "' cannot be found in your todo list!")
            #responded = True
        #dbQuery = db.query
        msg.body("The due date of the event '" + message_body + "' is ") # database query would go here
        responded = True
    if not responded:
        msg.body("I'm not sure I understand that, could you try again?")
    return str(resp)
    
def get_all_emails():
    all_emails = [db_emails.email for db_emails in db.session.query(models.Person).all()]
    return all_emails

def get_person_object(email):
    some_person = db.session.query(models.Person).filter_by(email=email).first()
    return some_person


def add_new_person_to_db(email):
    p = models.Person(email=email)
    db.session.add(p);
    db.session.commit();
        
def add_new_todo_to_db(todo):
    some_person = db.session.query(models.Person).filter_by(email=user_email).first()
    t = models.Todo(todo=todo, person=some_person)
    db.session.add(t);
    db.session.commit();


@socketio.on("login with code")
def login(data):
    auth_code = data['code']
    print(auth_code)
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        'client_secret.json',
        scopes=['openid', 'https://www.googleapis.com/auth/userinfo.email',
        'https://www.googleapis.com/auth/userinfo.profile',
        'https://www.googleapis.com/auth/calendar.events',
        'https://www.googleapis.com/auth/calendar'],
        redirect_uri = "https://66b3860890e243e18ab6f0967df663ca.vfs.cloud9.us-east-1.amazonaws.com"
        )

    flow.fetch_token(code=auth_code)
    cred = flow.credentials
    print(cred.token)
    print(cred.refresh_token)

user_email = ""

@socketio.on("login with email")
def loginWithEmail(data):
    email = data['email']
    global user_email
    user_email = email
    print(email)
    print(user_email)
    if email not in get_all_emails():
        add_new_person_to_db(email)
    else:
        print(f"user {email} exists")
    
    
print("user email="+user_email)

@socketio.on("sendCalendar")
def sendCalendar(data): #when calendar api code is finished it will have to send this in the data sent back to client
        loginUser="https://calendar.google.com/calendar/embed?src={}&ctz=America%2FNew_York".format(data['email'])
        socketio.emit('googleCalendar', {
            'url':loginUser
            })

if __name__ == '__main__':
    init_db(app)
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )
