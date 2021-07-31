import wiotp.sdk
from utils import bulb

# ibm iot platform device credential here
deviceOptions = {
    "identity": {"orgId": "90j0ad", "typeId": "vDev", "deviceId": "vActuator"},
    "auth": {"token": "passw0rd"},
}

actuator = 'off'


def commandProcessor(cmd):
    global actuator
    if cmd.data["d"]["actuator"]:
        data = {}
        if cmd.data["d"]["actuator"] == "on":
            actuator = 'on'
            bulb.bulbOn()
            data = {"d": {"actuator": "on"}}
        else:
            actuator = 'off'
            bulb.bulbOff()
            data = {"d": {"actuator": "off"}}
        deviceCli.publishEvent("status", "json", data, qos=0)


deviceCli = wiotp.sdk.device.DeviceClient(deviceOptions)
deviceCli.commandCallback = commandProcessor
deviceCli.connect()


def periodicPublish():
    data = {"d": {"actuator": actuator}}
    deviceCli.publishEvent("status", "json", data, qos=0)
    print("        Periodic update : Actuator is " + actuator)
    bulb.after(3000, periodicPublish)


try:
    while True:
        bulb.after(3000, periodicPublish)
        bulb.mainloop()
except (KeyboardInterrupt, SystemExit):
    print("Received keyboard interrupt, quitting ...")
    exit(0)
