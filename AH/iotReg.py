import wiotp.sdk
import json
import paho.mqtt.client as mqtt
import time
import multiprocessing as mp

task_queue = mp.Queue()

# ibm iot platform device credential here
deviceOptions = {
    "identity": {"orgId": "90j0ad", "typeId": "vDev", "deviceId": "vRegulator"},
    "auth": {"token": "passw0rd"},
}

deviceCli = wiotp.sdk.device.DeviceClient(deviceOptions)
deviceCli.connect()

## get thermo values
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("thermo")  # sub topic 'thermo'


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

    # bytes to str
    msg.payload = msg.payload.decode('utf8').replace("'", '"')

    # str to dict
    msg.payload = json.loads(msg.payload)

    while True:
        if (msg.payload['d']['cur_temp'] < msg.payload['d']['tar_temp']):
            data = {'d': {'regulator': "on",
                          "cur_temp": msg.payload['d']['cur_temp'],
                          "tar_temp": msg.payload['d']['tar_temp']}}
            print("")
            print("ACTING")
            time.sleep(10)
            msg.payload['d']['cur_temp'] += 0.5
            print("Current temperature is %.1f" % (msg.payload['d']['cur_temp']))

            deviceCli.publishEvent("status", "json", data, qos=0)

            print("----------------------------------")

            if (msg.payload['d']['cur_temp'] >= msg.payload['d']['tar_temp']):
                data = {'d': {'regulator': "off",
                              "cur_temp": msg.payload['d']['cur_temp'],
                              "tar_temp": msg.payload['d']['tar_temp']}}
                print("Current temperature is %.1f" % (msg.payload['d']['cur_temp']))
                deviceCli.publishEvent("status", "json", data, qos=0)
                time.sleep(1)
                continue

        else:
            data = {'d': {'regulator': "off",
                          "cur_temp": msg.payload['d']['cur_temp'],
                          "tar_temp": msg.payload['d']['tar_temp']}}
            print("")
            print("STOP")
            time.sleep(3)
            msg.payload['d']['cur_temp'] -= 0.1
            print("Current temperature is %.1f" % (msg.payload['d']['cur_temp']))

            deviceCli.publishEvent("status", "json", data, qos=0)

            print("----------------------------------")

            if (msg.payload['d']['cur_temp'] < msg.payload['d']['tar_temp']):
                data = {'d': {'regulator': "on",
                              "cur_temp": msg.payload['d']['cur_temp'],
                              "tar_temp": msg.payload['d']['tar_temp']}}
                deviceCli.publishEvent("status", "json", data, qos=0)
                print("Current temperature is %.1f" % (msg.payload['d']['cur_temp']))
                time.sleep(1)
                continue

    return msg

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org")

#---------------------------------------:sub slider values
# process all tasks on queue
try:
    while True:
        client.loop_forever()
        task = task_queue.get()
        task()
except (KeyboardInterrupt, SystemExit):
    print("Received keyboard interrupt, quitting ...")
    exit(0)
    




    
    
