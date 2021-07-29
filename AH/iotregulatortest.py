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

# # temperature option

# print(now_temp)
# print(type(now_temp))
# tar_temp  = 1
#
# print("")
# if (int(now_temp) <= int(tar_temp)):
#     sys.argv[1] = "on"
#     data = {"d" : {"regulator" : sys.argv[1]}}
# else:
#     sys.argv[1] = "off"
#     data = {"d" : {"regulator" : sys.argv[1]}}
#
#
# deviceCli.publishEvent("status", "json", data, qos=0)
# print("Sending the Command => " + json.dumps(data))
# time.sleep(2)
