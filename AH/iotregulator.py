import wiotp.sdk
import sys
import json
import time

# ibm iot platform device credential here
deviceOptions = {
    "identity": {"orgId": "90j0ad", "typeId": "vDev", "deviceId": "vRegulator"},
    "auth": {"token": "passw0rd"},
}

deviceCli = wiotp.sdk.device.DeviceClient(deviceOptions)
deviceCli.connect()

# 온도를 받고 온도 비교하는 단순 python code 
room_temp = float(input("현재 방 온도: "))
setting_temp = float(input("셋팅 온도 설정: "))

regulator = "off"

while True:
    if room_temp < setting_temp:
        regulator = "on"
        print("구동기가 {} 되었습니다.".format(regulator))
        room_temp += 0.5
        print("room_temp: {:.2f}".format(room_temp))
        data = {"d": {"regulator": regulator}}
        deviceCli.publishEvent("status", "json", data, qos=0)
        json.dumps(data)
        print("")
        time.sleep(3)
        if room_temp >= setting_temp:
            regulator = "off"
            print("구동기가 {} 됩니다.".format(regulator))
            data = {"d": {"regulator": regulator}}
            deviceCli.publishEvent("status", "json", data, qos=0)
            json.dumps(data)
            print("")
            time.sleep(3)
            continue
    if room_temp >= setting_temp:
        regulator = "off"
        print("구동기가 {} 되었습니다.".format(regulator))
        room_temp -= 0.2
        print("room_temp: {:.2f}".format(room_temp))
        data = {"d": {"regulator": regulator}}
        deviceCli.publishEvent("status", "json", data, qos=0)
        json.dumps(data)
        print("")
        time.sleep(3)
        if room_temp < setting_temp:
            regulator = "on"
            print("구동기가 {} 됩니다.".format(regulator))
            data = {"d": {"regulator": regulator}}
            deviceCli.publishEvent("status", "json", data, qos=0)
            json.dumps(data)
            print("")
            time.sleep(3)
            continue