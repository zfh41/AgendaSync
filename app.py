import os
from os.path import join, dirname
import flask
import flask_socketio
import flask_sqlalchemy
from dotenv import load_dotenv
import google.oauth2.credentials
import google_auth_oauthlib.flow

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


@socketio.on("login")
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
    # auth_uri = flow.authorization_url()
    # print(auth_uri)
    flow.fetch_token(code=auth_code)
    cred = flow.credentials
    print(cred.token)
    print(cred.refresh_token)


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
