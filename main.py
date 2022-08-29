#Back-end (web-server)

#import streamlit as st
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
# CORS_ALLOWED_ORIGINS is the list of origins authorized to make requests
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('message')  # pitää olla message
def handle_message(msg):
    if msg == 'get_messages':
        print("serveri sai viestin get_messages.")
        # haetaan tiedostosta viestit ja lähetetään ne clientille.


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    socketio.run(app, host="localhost")


# google cdn socket.io
# https://cdnjs.com/libraries/socket.io
