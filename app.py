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
from google.auth.transport.requests import Request
import datetime
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
USERS_UPDATED_CHANNEL = 'users updated'

app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")
dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)
dotenv_path = join(dirname(__file__),'redirect.env')
load_dotenv(dotenv_path)
dotenv_path = join(dirname(__file__),'twilio.env')
load_dotenv(dotenv_path)
twilio_account_sid = os.environ['TWILIO_ACCOUNT_SID']
twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']

google_uri = os.environ['GOOGLE_URI']

database_uri = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

db = flask_sqlalchemy.SQLAlchemy(app)

def init_db(app):
    db.init_app(app)
    db.app = app
    models.createModels()
    db.session.commit()
import models


def message_emit(channel):
    
    #Pull database updated with new todo list for user
    
    #socketio.emit(channel, {
    #    'updateTodoList': fromDatabase['todoList for user']
    #})
    print("message emitted")

@app.route('/', methods=['GET', 'POST'])
def hello():
    return flask.render_template('index.html')

#twilio
#twilio
#ngrok http 5000

ADD_TODO = "add todo"
DELETE_TODO = "delete todo"
LIST_TODO = "list todo"
START_TODO = "start date"
DUE_DATE = "due date"
HELP_ME = 'help me'

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if HELP_ME in incoming_msg:
        msg.body("Hello! I'm the agendasync textbot! My know commands are: 'add todo', 'delete todo, 'list todo', 'start date', and 'due date'")
        responded = True
        
    if ADD_TODO in incoming_msg:
        message_body = incoming_msg[9:]
        add_new_todo_to_db(message_body)
        msg.body("Inserted: '" +  message_body + "' into your todolist!")
        responded = True
    # if DELETE_TODO in incoming_msg and incoming_msg[12:].isnumeric():
    #     delete_todo(int(incoming_msg[12:]))
    #     msg.body("Deleting from your todolist!")
    #     responded = True    
    # elif DELETE_TODO in incoming_msg:
    #     msg.body("Please reply with a todo id to delete: 'delete todo id'\n")
    #     msg.body(get_all_todos_values())
    #     responded = True
            
    if LIST_TODO in incoming_msg:
            msg.body("Your todo listt contents are as follows: " + get_all_todos_values())
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
    
def get_all_todos():
    # p = get_person_object(user_email)
    # all_todos = db.session.query(models.Todo).filter_by(person_id=p.id).all()
    # # all_todos = [db_todos.todo for db_todos in db.session.query(models.Person).all()]
    # return p.todos
    global user_email
    p = get_person_object(user_email)
    all_todos = db.session.query(models.Todo).filter_by(person_id=p.id).all()
    for todo in all_todos:
        print(todo.todo, todo.start_todo, todo.due_date)
        socketio.emit('all todos', todo.todo)
        socketio.emit('start date', str(todo.start_todo))
        socketio.emit('due date', str(todo.due_date))
        
def get_all_todos_values():
    global user_email
    p = get_person_object(user_email)
    all_todos = db.session.query(models.Todo).filter_by(person_id=p.id).all()
    todo_list = []
    for todo in all_todos:
        todo_list.append('Id: ' +str(todo.id) +'\nTodo: ' + todo.todo + '\nstart date: ' +str(todo.start_todo) + '\ndue date: ' +str(todo.due_date) + '\n')
    return ' '.join(map(str, todo_list))
    
def get_all_todos_ids():
    global user_email
    p = get_person_object(user_email)
    all_todos = db.session.query(models.Todo).filter_by(person_id=p.id).all()
    todo_list_ids = []
    for todo in all_todos:
        todo_list_ids.append(str(todo.id))
    return todo_list_ids
        

def get_person_object(email):
    some_person = db.session.query(models.Person).filter_by(email=email).first()
    return some_person


def add_new_person_to_db(email,cred):
    p = models.Person(email=email,cred=cred)
    db.session.add(p);
    db.session.commit();

def update_tokens_in_db(email,cred):
    p = get_person_object(email)
    p.cred = cred
    db.session.commit();
    
user_email = ""
cred = ""

def add_new_todo_to_db(todo,start="",end=""):
    some_person = db.session.query(models.Person).filter_by(email=user_email).first()
    if start == "" and end == "":
        t = models.Todo(todo=todo, person=some_person)
    else:
        t = models.Todo(todo=todo, person=some_person,start_todo = start, due_date = end)
    db.session.add(t);
    db.session.commit();
    
# def delete_todo(id):
#     global user_email
#     some_person = db.session.query(models.Person).filter_by(email=user_email).first()
#     t = db.session.query(models.Todo).filter_by(id=id, person=some_person)
#     db.session.delete(t);
#     db.session.commit();

@socketio.on("login with code")
def login(data):
    global cred
    global user_email
    auth_code = data['code']
    print(auth_code)
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        'client_secret.json',
        scopes=['openid', 'https://www.googleapis.com/auth/userinfo.email',
        'https://www.googleapis.com/auth/userinfo.profile',
        'https://www.googleapis.com/auth/calendar'],
        redirect_uri = google_uri
        )

    flow.fetch_token(code=auth_code)
    
    cred = flow.credentials

    service = build("calendar", "v3", credentials=cred)
    result = service.calendarList().list().execute()
    
    profileurl = "https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token={}".format(cred.token)
    profile = requests.get(profileurl)
    profile = profile.json()
    
    user_email = profile["email"]

    loginUser="https://calendar.google.com/calendar/embed?src={}&ctz=America%2FNew_York".format(user_email)
    socketio.emit('googleCalendar', {
        'url':loginUser
        })
    calendar_id = result['items'][0]['id']
    
    result = service.events().list(calendarId=calendar_id).execute()
    #print(result['items'])
    
    if user_email not in get_all_emails():
        add_new_person_to_db(user_email,cred)
    else:
        print(f"user {user_email} exists")
        update_tokens_in_db(user_email,cred)
    
    socketio.emit('connected', {
        'calendarUpdate': result['items']
    })

    
print("user email="+user_email)

@socketio.on("login with email")
def loginWithEmail(data):
    email = data['email']
    global user_email
    user_email = email
    print(email)
    loginUser="https://calendar.google.com/calendar/embed?src={}&ctz=America%2FNew_York".format(email)
    socketio.emit('googleCalendar', {
        'url':loginUser
        })
    person = get_person_object(user_email)
    global cred
    cred = person.cred
    print(cred)
    print(cred.token)
    get_all_todos()
    
    
    
@socketio.on("addCalendarEvent")
def addCalendarEvent(data):
    global cred
    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
            update_tokens_in_db(user_email,cred)
    print(data)
    title = data['title']
    date = data['date']
    event = {
      'summary': title,
      'location': '',
      'description': '',
      'start': {
        'dateTime': date,
        'timeZone': 'America/New_York',
      },
      'end': {
        'dateTime': date,
        'timeZone': 'America/New_York',
      },
      'attendees': [],
      'reminders': {
        'useDefault': True
      },
    }

    service = build("calendar", "v3", credentials=cred)
    event = service.events().insert(calendarId='primary',body=event).execute()
    
    
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
    add_new_todo_to_db(desc,startToDo,endToDo)
    
if __name__ == '__main__':
    init_db(app)
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )
