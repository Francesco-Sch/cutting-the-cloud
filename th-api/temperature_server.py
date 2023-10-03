import tinytuya
from tinytuya import Contrib
import os
from dotenv import load_dotenv

load_dotenv()

d = Contrib.ThermostatDevice(os.getenv("DEVICE_ID"), os.getenv("IP_ADDRESS"), os.getenv("LOCAL_KEY"))
d.set_version(3.4)
d.set_socketPersistent(True)

print(" > Send Request for Status < ")
payload = d.generate_payload(tinytuya.DP_QUERY)
d.send(payload)

print(" > Begin Monitor Loop <")
while(True):
    # See if any data is available
    # data = d.receive()
    # print('Received Payload: %r' % data)

    print(" > Send Request for Status < ")
    data = d.status()  
    print("Data from Status() call: %r" % data)

    if 'dps' in data:
        print(" > Read Temperature < ")
        print("Temperature: %r" % data['dps']['1'])

    # Send keyalive heartbeat
    print(" > Send Heartbeat Ping < ")
    payload = d.generate_payload(tinytuya.HEART_BEAT)
    d.send(payload)


    print(" > Send Request for DPS < ")
    dps = d.detect_available_dps()
    print("Available DPS: %r" % dps)

    # NOTE If you are not seeing updates, you can force them - uncomment:
    # print(" > Send Request for Status < ")
    # payload = d.generate_payload(tinytuya.DP_QUERY)
    # d.send(payload)

    # NOTE Some smart plugs require an UPDATEDPS command to update power data
    # print(" > Send DPS Update Request < ")
    # payload = d.generate_payload(tinytuya.UPDATEDPS)
    # d.send(payload)    