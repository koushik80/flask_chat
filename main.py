import streamlit as st
from flask import Flask, render_template
from flask_socketio import SocketIO, send
#from flask_cors import CORS

app = Flask(__name__)
#socketio = SocketIO(app, cors_allowed_origins="*")


@app.route('/')
def hello():
    return render_template('index.html')
