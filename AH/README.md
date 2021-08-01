# IBM IOT를 이용한 난방 조절 시스템
### 시스템 시나리오
1. 시스템 첫 시작 시, 현재 온도와 설정 온도를 입력받는다. 
2. 현재 온도가 설정 온도보다 낮을 시, 난방 시스템 가동
   > 난방 시스템은 3초에 0.5도 씩 현재 온도를 높인다.
3. 현재 온도가 설정 온도보다 높을 시, 난방 시스템 작동 중단
   > 난방 시스템이 작동되지 않는 동안, 10초에 0.1도 씩 현재 온도가 낮아진다.

### Node-RED Flow
- Regulator & Actuator Node-RED
![image](https://user-images.githubusercontent.com/26236857/127771823-79489a54-7d33-4404-96dc-d8ed8f106475.png)
- Weather API Node-RED Flow
![image](https://user-images.githubusercontent.com/26236857/127771838-ae1945a0-0660-46d4-938f-adcb98d1f0dd.png)
- Data.go.kr API Node-RED Flow
![image](https://user-images.githubusercontent.com/26236857/127771850-e94cf8ff-c002-4dcf-a05a-44bb89d8b811.png)
- Node-RED UI
![image](https://user-images.githubusercontent.com/26236857/127771789-b3c3db31-2ea1-4614-b8d5-a27b44b2c1f0.png)


### Python Code
1. iotReg.py : Regulator(구동기) Python
2. iotActuatorBulb.py : GUI가 들어간 Python - Valve PNG 파일로 변경예정
