# iotActuator.py: iotRegulator에 따라 on/off 제어
# 작성자: 윤지희
# 최초 작성일: 2021년 7월 29일
# 최근 수정일: 2021년 7월 29일


import wiotp.sdk
from time import sleep

# ibm iot platform device credential here
deviceOptions = {
    "identity": {"orgId": "k0l446", "typeId": "vDev", "deviceId": "vActuator"},
    "auth": {"token": "passw0rd"},
}

actuator = 'off'

def commandProcessor(cmd):
    global actuator
    if cmd.data["d"]["actuator"]:
        data = {}
        if cmd.data["d"]["actuator"] == "on":
            actuator = 'on'
            print("Actuator is On")
            data = {"d" : {"actuator" : "on"}}
        else:
            actuator = 'off'
            print("Actuator is Off")
            data = {"d" : {"actuator" : "off"}}
        deviceCli.publishEvent("status", "json", data, qos=0)

deviceCli = wiotp.sdk.device.DeviceClient(deviceOptions)
deviceCli.commandCallback = commandProcessor
deviceCli.connect()

def periodicPublish():
    data = {"d":{"actuator": actuator}}
    deviceCli.publishEvent("status", "json", data, qos=0)
    print("        Periodic update : Actuator is " + actuator )
    
while True:
    periodicPublish()
    sleep(10)

