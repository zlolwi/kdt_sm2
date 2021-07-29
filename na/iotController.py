# 온도감지

import wiotp.sdk
import sys
import json
import time

# ibm iot platform device credential here
deviceOptions = {
    "identity": {"orgId": "e1j7k6", "typeId": "vDev", "deviceId": "vSwitch"},
    "auth": {"token": "passw0rd"},
}

if len(sys.argv) != 3:
    print("\n    Usage iotremote.py 현재온도, 희망온도 \n")
    sys.exit(1)

deviceCli = wiotp.sdk.device.DeviceClient(deviceOptions)
deviceCli.connect()

print("")

if sys.argv[2] < str.argv[1] :
    data = {"d": {"controller":  "on"}}
    print( "현재온도: {}", 현재온도)

else :
    data = {"d": {"controller":  "off"}}
    print( "현재온도: {}", 현재온도)

deviceCli.publishEvent("status", "json", data, qos=0)
print ("명령을 보내고 있습니다. => " + json.dumps.(data))

#,, 음 연결을 어떻게하지...
#

time.sleep(2)
