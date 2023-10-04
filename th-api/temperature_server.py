import tinytuya
from tinytuya import Contrib
import os
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
# import time
import threading
from flask_cors import CORS


load_dotenv()

d = Contrib.ThermostatDevice(os.getenv("DEVICE_ID"), os.getenv("IP_ADDRESS"), os.getenv("LOCAL_KEY"))
d.set_version(3.4)
d.set_socketPersistent(True)

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

def get_temperature():
    print(" > Send Request for Payload < ")
    payload = d.generate_payload(tinytuya.DP_QUERY)
    d.send(payload)

    lastTemperature = 0
    
    print(" > Begin Sensor Monitoring <")
    while True:
        print(" > Send Request for Status < ")
        data = d.status()  
        print("Data from Status() call: %r" % data)

        if 'dps' in data:
            print(" > Read Temperature < ")
            print("Temperature: %r" % data['dps']['1'])

            if data['dps']['1'] & data['dps']['1'] != lastTemperature:
                lastTemperature = data['dps']['1']
                currentTemperature = data['dps']['1']
                socketio.emit('temperature_update', {'temperature': currentTemperature})
            else:
                print("Temperature Unchanged")
        
        else:
            print("No Temperature Data")
          

        # Send keyalive heartbeat
        # print(" > Send Heartbeat Ping < ")
        # payload = d.generate_payload(tinytuya.HEART_BEAT)
        # d.send(payload)

        # time.sleep(5)

@app.route('/ping')
def ping():
    return "pong"

if __name__ == "__main__":
    t = threading.Thread(target=get_temperature)
    t.start()
    socketio.run(app, debug=True)