import tinytuya
import time
import os
from dotenv import load_dotenv

load_dotenv()

# Connect to Tuya Cloud
c = tinytuya.Cloud(
        apiRegion=os.getenv("API_REGION"), 
        apiKey=os.getenv("API_KEY"), 
        apiSecret=os.getenv("API_SECRET"), 
        apiDeviceID=os.getenv("API_DEVICE_ID"))

# Display list of devices
devices = c.getdevices()
print("Device List: %r" % devices)

# Select a Device ID to Test
id = "bfec304bf01111acebqu2i"

# Display Properties of Device
result = c.getproperties(id)
print("Properties of device:\n", result)

# Display Status of Device
result = c.getstatus(id)
print("Status of device:\n", result)

# Send Command - Turn on switch
commands = {
    "commands": [
        {"code": "temp_current", "values": {"max": 200}},
    ]
}
print("Sending command...")
result = c.sendcommand(id,commands)
print("Results\n:", result)


while True:


    properties = c.getstatus(id)
    temperature = properties['result'][0]['value']
    print("Current temperature:", temperature)
    time.sleep(5)