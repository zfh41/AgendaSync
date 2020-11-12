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

from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")
dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)

twilio_account_sid = os.environ['TWILIO_ACCOUNT_SID']
twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']

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
    if 'help me' in incoming_msg:
        msg.body("Hello! I'm the agendasync textbot! My know commands are: 'quote' and 'cat'")
        responded = True
    if 'add todo' in incoming_msg:
        try:
            if incoming_msg[8] == ' ' and incoming_msg[9] != ' ':
                message_body = incoming_msg[9:]
                
                # Database Insertion Code/Method goes here
                
                message_emit("todolist update")
                
                msg.body("Inserted: '" +  message_body + "' into your todolist!")
                responded = True
            else:
                msg.body("The proper add command is: add todo 'insert event here'")
                responded = True
        except:
            msg.body("The proper add command is: add todo 'insert event here'")
            responded = True
    if 'list todo' in incoming_msg:
        try:
            msg.body("Your todolsit contents are as follows:")
            todoListString = ""
            
            # query database tables for todolist
            #for item in database:
            #    todoListString += (" * " + db.item + "\n")
            
            msg.body(todoListString)
            responded = True
            
        except:
            msg.body("The proper add command is: list todo")
            responded = True     
    '''
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
    '''
    if not responded:
        msg.body("I'm not sure I understand that, could you try again?")
    return str(resp)
    



@socketio.on("login with code")
def login(data):
    auth_code = data['code']
    print(auth_code)
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        'credentials.json',
        scopes=['openid', 'https://www.googleapis.com/auth/userinfo.email',
        'https://www.googleapis.com/auth/userinfo.profile',
        'https://www.googleapis.com/auth/calendar.events',
        'https://www.googleapis.com/auth/calendar'],
        redirect_uri = "https://a1cbac3aed844b74bb46bf3b83eaaca8.vfs.cloud9.us-east-1.amazonaws.com"
        )

    flow.fetch_token(code=auth_code)
    cred = flow.credentials
    
    service = build("calendar", "v3", credentials=cred)
    result = service.calendarList().list().execute()
    
    calendar_id = result['items'][0]['id']
    result = service.events().list(calendarId=calendar_id).execute()
    
    print(result['items'])
    
    socketio.emit('connected', {
        'calendarUpdate': result['items']
    })


@socketio.on("login with email")
def loginWithEmail(data):
    email = data['email']
    print(email)

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
