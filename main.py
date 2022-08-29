# BACK-END
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
# CORS_ALLOWED_ORIGINS is the list of origins authorized to make requests
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('message')  # pitää olla message
def handle_message(msg):
    if msg == "get_messages":
        with open('viestit.txt') as f:
            viestit = f.readlines()
            viestit.insert(0, 'KAIKKI VIESTIT')
            send(viestit, broadcast=True)
    else:
        if msg:
            with open('viestit.txt', 'a') as f:
                f.write(msg+'\n')
            with open('viestit.txt') as f:
                viestit = f.readlines()
                send(viestit[-1], broadcast=True)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    socketio.run(app, host="localhost")
