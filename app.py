import os
from os.path import join, dirname
from dateutil import parser
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
    
import bot as Bot
import models

@app.route('/', methods=['GET', 'POST'])
def hello():
    return flask.render_template('index.html')
#twilio

ADD_TODO = "add todo"
LIST_TODO = "list todo"
START_TODO = "start date"
DUE_DATE = "due date"

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')
    return str(resp)
    

def add_new_person_to_db(email):
        db.session.add(models.Person(email));
        db.session.commit();

def add_new_todo_to_db(todo, start_todo, due_date):
        db.session.add(models.Todo(todo, start_todo, due_date));
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
        #TODO: will probably need to put redirect_uri in an env file at some point
    flow.fetch_token(code=auth_code)
    cred = flow.credentials
    print(cred.token)
    print(cred.refresh_token)
    #TODO: retreive user email,name (and profilepic?) and send to frontend
    # use email in add_new_person_to_db(email) if theyre new
    # do google calendar stuff

@socketio.on("login with email")
def loginWithEmail(data):
    email = data['email']
    print(email)
    #add_new_person_to_db(email)
    #TODO: use email to retreive user info and tokens from database 
    # send stuff to frontend
    # do google calendar stuff
    
    
@socketio.on("sendCalendar")
def sendCalendar(data): #when calendar api code is finished it will have to send this in the data sent back to client
        loginUser="https://calendar.google.com/calendar/embed?src={}&ctz=America%2FNew_York".format(data['email'])
        socketio.emit('googleCalendar', {
            'url':loginUser
            })

@socketio.on("addCalendarEvent")
def addCalendarEvent(data):
    print(data)
    
@socketio.on("addToDoList")
def addToDoList(data):
    print(data)
    startToDo = data["startDate"] #currently both times are in UTC
    endToDo = data["endDate"]
    desc = data["description"]
    startToDo = parser.isoparse(startToDo)
    endToDo = parser.isoparse(endToDo)
    print(startToDo)
    print(endToDo)
    #add_new_todo_to_db(desc,startToDo,endToDo)
if __name__ == '__main__':
    init_db(app)
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )
