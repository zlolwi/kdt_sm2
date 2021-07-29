import wiotp.sdk
import sys
import json
import time

# ibm iot platform device credential here
deviceOptions = {
    "identity": {"orgId": "90j0ad", "typeId": "vDev", "deviceId": "vRegulator"},
    "auth": {"token": "passw0rd"},
}

# 온도를 받고 온도 비교하는 단순 python code
room_temp = float(input("현재 방 온도: "))
setting_temp = float(input("셋팅 온도 설정: "))

while True:
    if room_temp < setting_temp:
        print("구동기가 on 되었습니다.")
        room_temp += 0.5
        print("room_temp: {:.2f} \n".format(room_temp))
        time.sleep(5)
        if room_temp >= setting_temp:
            print("구동기가 off 됩니다. \n")
            continue
    if room_temp >= setting_temp:
        print("구동기가 off 되었습니다.")
        room_temp -= 0.2
        print("room_temp: {:.2f} \n".format(room_temp))
        time.sleep(5)
        if room_temp < setting_temp:
            print("구동기가 on 됩니다. \n")
            continue

deviceCli = wiotp.sdk.device.DeviceClient(deviceOptions)
deviceCli.connect()

print("")
data = {"d" : {"regulator" : sys.argv[1]}}
deviceCli.publishEvent("status", "json", data, qos=0)
print("Sending the Command => " + json.dumps(data))
time.sleep(1)
