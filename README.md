# Smart Farm Project 🌱

실내, 홈 가드닝을 위한 Smart Farm Project 입니다.

> __Smart Farm 기능__ <br/>
>> 1. 조도에 따른 LED센서 ON/OFF <br/>
>> 2. LED센서 밝기 단계별 조절 기능(UI) <br/>
>> 3. 현재 대기 온도에 따른 FAN ON/OFF <br/>
>> 4. 토양 습도 값에 따른 Water Pump ON/OFF <br/>
>> 5. 온습도 센서 측정 값 Smart Farm Kit LCD에 출력 <br/>
>> 6. 수위 센서를 통한 수통 잔여 물 양 확인(UI) <br/>
>> 7. 카메라 모듈로 실시간 식물 상태 확인 기능(UI) <br/>
>> 8. FAN, LED, Water Pump, 토양 습도 센서 수동 조작(UI) <br/>

## 진척상황

### MileStone

<p align="center">
    <img width="80%" height="80%" src="PortFolio/images/smartfarm_milestone.jpg"><br/>
    <span><b>SmartFarm DEMO</b></span>
</p>

---

### 21.08.02 (월)

<p align="center">
    <img width="70%" height="70%" src="PortFolio/images/210802_smartfarm_demo_01.JPG"><br/>
    <img width="70%" height="70%" src="PortFolio/images/210802_smartfarm_demo_03.JPG"><br/>
    <span><b>SmartFarm DEMO</b></span>
</p>

- Flask Demo 파이썬 코드 작성<br/>
- 실시간 스트리밍 코드 작성<br/>
- CSS, HTML 작성<br/>

---

### 21.08.03 (화)

- Ajax 데모 코드 작성<br/>

<p align="center">
    <img width="70%" height="70%" src="PortFolio/images/waterpump.jpg" ><br/>
    <img width="70%" height="70%" src="PortFolio/images/mcp3008_and_light.jpg" ><br/>
    <span><b>워터펌프, 조도센서</b></span>
</p>

- 워터 펌프 가동 확인 및 데모 코드 (릴레이 모듈 제어) 작성<br/>
- 조도 센서 확인 및 데모 코드 (밝기별 전압) 작성<br/>

---

### 21.08.04 (수)

<p align="center">
    <img width="30%" height="30%" src="PortFolio/images/led_light.jpg" ><br/>
    <span><b>LED 센서</b></span>
</p>

- LED 센서 확인 및 데모 코드 (단계별 조절) 작성<br/>

<p align="center">
    <img width="65%" height="65%" src="PortFolio/images/ajax_sensor.jpg" ><br/>
    <span><b>센서 버튼 동작 확인</b></span>
</p>

- Ajax 코드 (웹 컨트롤러 버튼 동작) 작성<br/>
- js, css 파일 캐싱 문제 해결<br/>

---

### 21.08.05 (목)

<p align="center">
    <img width="30%" height="20%" src="PortFolio/images/sensor_lcd.jpg" ><br/>
    <span><b>온습도 센서 및 결과 LCD 출력</b></span>
</p>

- 온습도 센서 및 I2C LCD 모듈 확인 및 데모 코드 (온습도 표기) 작성<br/>

---

### 21.08.06 (금)

<p align="center">
    <img width="30%" height="20%" src="PortFolio/images/dc_adapter_5v.jpg" ><br/>
    <span><b>DC 5V 전원 공급 장치 튜닝</b></span>
</p>

- DC 5V 전원 공급 어댑터 튜닝<br/>

<p align="center">
    <img width="30%" height="20%" src="PortFolio/images/water_level_and_soil_moisture.jpg" ><br/>
    <span><b>수위 측정 센서 및 토양 수분 센서</b></span>
</p>

- 수위 센서 확인 및 데모 코드 (전위차) 작성<br/>
- 토양 수분 센서 확인 및 데모 코드 (전위차) 작성<br/>

<p align="center">
    <img width="60%" height="60%" src="PortFolio/images/배치도_1.png" ><br/>
    <span><b>라즈베리파이 핀 배치도</b></span>
</p>

<p align="center">
    <img width="60%" height="60%" src="PortFolio/images/배치도_2.png" ><br/>
    <span><b>브레드 보드 #1 배치도</b></span>
</p> 

<p align="center">
    <img width="60%" height="60%" src="PortFolio/images/배치도_3.png" ><br/>
    <span><b>브레드 보드 #2 배치도</b></span>
</p> 
    
    
    


- 라즈베리파이 GPIO 핀 배치도 구성<br/>


#### Issue
> - MCP3008 모듈 고장, 다음 주 수요일(21-08-11)까지 배송 예정<br/>
> - 센서 측정 값 비일관적, 해결 방법 모색<br/>

---

### 21.08.09 (월)

> __일정__ <br/>
> - Raspberry Pi 핀 / Bread Board 배치<br/>
> - UI 부분 삭제, 생성 및 변경<br/>
>> 1. FAN 버튼 우측 상단과 하단측 중복<br/>
>> 2. 토양 수분 측정 ON/OFF 버튼 추가-ON상태 유지일 시 고장<br/>

---

### 21.08.10 (화)

> __일정__ <br/>
> - 배치도에 따른 동작 확인<br/>
> - Smart Farm Database 및 SQL 작성<br/>
> - UI 부분 리프레시 버튼 추가<br/>
