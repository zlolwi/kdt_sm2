import paho.mqtt.client as mqtt
import multiprocessing as mp

task_queue = mp.Queue()

# 콜백 함수 정의하기
#  (mqttc.connect를 잘 되면) 서버 연결이 잘되면 on_connect 실행 (이벤트가 발생하면 호출)
def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))

# 브로커에게 메시지가 도착하면 on_message 실행 (이벤트가 발생하면 호출)
def on_message(client, obj, msg):
    print(str(msg.payload.decode("utf-8")))

# (mqttc.subscribe가 잘 되면) 구독(subscribe)을 완료하면
# on_subscrbie가 호출됨 (이벤트가 발생하면 호출됨)
def on_subscribe(client, obj, mid, granted_qos):
    print()

def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))

# (mqttc.publish가 잘 되면) 메시지를 publish하면 on_publish실행 (이벤트가 발생하면 호출)
def on_publish(client, obj, mid):
    # 용도 : publish를 보내고 난 후 처리를 하고 싶을 때
    # 사실 이 콜백함수는 잘 쓰진 않는다.
    print("mid: " + str(mid))

# 클라이언트 생성
mqttc = mqtt.Client()

# 콜백 함수 할당하기
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

# 브로커 연결 설정
url = "broker.hivemq.com"
port = 1883

topic1 = "Now/dev01"
topic2 = "Now/dev02"

# 클라이언트 설정 후 연결 시도
mqttc.connect(host=url, port=port)

# QoS level 0으로 구독 설정, 정상적으로 subscribe 되면 on_subscribe 호출됨
mqttc.subscribe(topic1, 0)
mqttc.subscribe(topic2, 0)
mqttc.publish(topic1,topic1)

# 네트워크 loop를 계속 실행. 종료 에러가 발생하기 전까지 계속 실행
# process all tasks on queue
try:
    while True:
        mqttc.loop_forever()
        task = task_queue.get()
        task()
except (KeyboardInterrupt, SystemExit):
    print("Received keyboard interrupt, quitting ...")
    exit(0)