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
    prev_number = None
    while True:
        number = random.randint(1, 100)
        if number != prev_number:  # checks if the number has changed
            print(f"Number changed: {number}")
            socketio.emit('number_update', {'number': number})
            prev_number = number
        time.sleep(5)

if __name__ == "__main__":
    t = threading.Thread(target=number_generator)
    t.start()
    socketio.run(app, debug=True)
