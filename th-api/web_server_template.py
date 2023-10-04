from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import random
import time
import threading
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

def number_generator():
    # This function simulates changes in the value you're reading from another device
    number = 1
    while True:
        print(f"Number changed: {number}")
        socketio.emit('number_update', {'number': number})
        number += 1
        time.sleep(5)

if __name__ == "__main__":
    t = threading.Thread(target=number_generator)
    t.start()
    socketio.run(app, debug=True)
