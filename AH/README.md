# IBM IOT를 이용한 난방 조절 시스템
### 시스템 시나리오
1. 시스템 첫 시작 시, 현재 온도와 설정 온도를 입력받는다. 
2. 현재 온도가 설정 온도보다 낮을 시, 난방 시스템 가동
   > 난방 시스템은 3초에 0.5도 씩 현재 온도를 높인다.
3. 현재 온도가 설정 온도보다 높을 시, 난방 시스템 작동 중단
   > 난방 시스템이 작동되지 않는 동안, 10초에 0.1도 씩 현재 온도가 낮아진다.

### Node-RED Flow
- Weather API Node-RED Flow
![image](https://user-images.githubusercontent.com/26236857/127735899-969379d0-67ac-4c29-b15f-847a3a7c008c.png)

### Python Code
iotReg.py : Regulator(구동기) Python
iotActuatorBulb.py : GUI가 들어간 Python - Valve PNG 파일로 변경예정
