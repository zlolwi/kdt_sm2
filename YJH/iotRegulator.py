# iotRegulator.py: 설정 온도에 따라 Actuator 작동 제어
# 작성자: 

import wiotp.sdk
import sys
import json
import time

# ibm iot platform device credential here
deviceOptions = {
        "identity": {"orgId": "k0l446", "typeId": "vDev", "deviceId": "vRegulator"},
        "auth": {"token": "passw0rd"},
}

deviceCli = wiotp.sdk.device.DeviceClient(deviceOptions)
deviceCli.connect()

# temperature option
cur_temp = float(input(" Current temp? "))
tar_temp = float(input(" Target temp? "))

while True:
    if (cur_temp < tar_temp):
        data = {"d" : {"regulator" : "on"}}
        print("ACTING")
        time.sleep(3)
        cur_temp += 0.5
        print("Current temperature is %.1f"%(cur_temp))
        

        deviceCli.publishEvent("status", "json", data, qos=0)

        print("----------------------------------")
        if (cur_temp >= tar_temp):
            data = {"d" : {"regulator" : "off"}}
            deviceCli.publishEvent("status", "json", data, qos=0)
            time.sleep(1)
            continue

    else:
        data = {"d" : {"regulator" : "off"}}
        print("STOP")
        time.sleep(10)
        cur_temp -= 0.1
        print("Current temperature is %.1f"%(cur_temp))

        deviceCli.publishEvent("status", "json", data, qos=0)
    
        print("----------------------------------*")
        if (cur_temp < tar_temp):
            data = {"d" : {"regulator" : "on"}}
            deviceCli.publishEvent("status", "json", data, qos=0)
            continue;





