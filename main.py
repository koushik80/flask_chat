#Back-end (web-server)

#import streamlit as st
from flask import Flask, render_template
from flask_socketio import SocketIO, send
#from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET'] = "secret!"
socketio = SocketIO(app, cors_allowed_origins="*")
# cors_allowed_origins = list of origins authorized to make requests


@socketio.on('message')
def handle_message(msg):
    print(msg)
    if msg == 'save_to_db':
        save_to_db()
        send(msg, broadcast=True)


@app.route('/')
def index():
    return render_template("index.html")


def save_to_db():
    print("SAVING TO DB...")


if __name__ == '__main__':
    socketio.run(app, host='localhost',)
