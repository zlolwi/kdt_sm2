import wiotp.sdk
from time import sleep

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
<<<<<<< HEAD
            valve = 'on'
            print("Valve is On")
            data = {"d": {"valve": "on"}}
        else:
            valve = 'off'
=======
            lamp = 'on'
            print("Valve is On")
            data = {"d": {"valve": "on"}}
        else:
            lamp = 'off'
>>>>>>> main
            print("Valve is Off")
            data = {"d": {"valve": "off"}}
        deviceCli.publishEvent("status", "json", data, qos=0)


deviceCli = wiotp.sdk.device.DeviceClient(deviceOptions)
deviceCli.commandCallback = commandProcessor
deviceCli.connect()


def periodicPublish():
    data = {"d": {"valve": valve}}
    deviceCli.publishEvent("status", "json", data, qos=0)
    print("        Periodic update : Valve is " + valve)


while True:
    periodicPublish()
<<<<<<< HEAD
    sleep(3)
=======
    sleep(10)
>>>>>>> main
