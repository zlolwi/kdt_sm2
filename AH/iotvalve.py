import wiotp.sdk
from time import sleep
# import RPi.GPIO as g
# g.setmode(g.BCM)
# g.setup(15, g.OUT)

# ibm iot platform device credential here
deviceOptions = {
    "identity": {"orgId": "90j0ad", "typeId": "vDev", "deviceId": "vValve"},
    "auth": {"token": "passw0rd"},
}

valve = 'off'


def commandProcessor(cmd):
    global valve
    if cmd.data["d"]["valve"]:
        data = {}
        if cmd.data["d"]["valve"] == "on":
            valve = 'on'
            print("Valve is On")
            data = {"d": {"valve": "on"}}
            # g.output(15, g.HIGH)
        else:
            valve = 'off'
            print("Valve is Off")
            data = {"d": {"valve": "off"}}
            # g.output(15, g.LOW)
        deviceCli.publishEvent("status", "json", data, qos=0)


deviceCli = wiotp.sdk.device.DeviceClient(deviceOptions)
deviceCli.commandCallback = commandProcessor
deviceCli.connect()

def periodicPublish():
    data = {"d":{"valve": valve}}
    deviceCli.publishEvent("status", "json", data, qos=0)
    print("        Periodic update : Valve is " + valve)

while True:
    periodicPublish()
    sleep(3)