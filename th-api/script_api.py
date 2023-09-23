import tinytuya
import time

# Connect to Tuya Cloud
# c = tinytuya.Cloud()  # uses tinytuya.json 
c = tinytuya.Cloud(
        apiRegion="eu", 
        apiKey="uk3wsg8saxacp95chnku", 
        apiSecret="bab4631e3f984c9b8655c42002420916", 
        apiDeviceID="bfec304bf01111acebqu2i")

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