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
    
@app.route('/bot', methods=['POST'])
def bot():
    #twilio
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


if __name__ == '__main__':
    #init_db(app)
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )
