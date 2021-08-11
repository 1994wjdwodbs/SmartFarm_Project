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

## Smart Farm Project Members (5명)

__- 강동훈__ <br/>
__- 정재윤__ <br/>
__- 하진우__ <br/>
__- 허상현__ <br/>
__- 조희지__ <br/>

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

- Ajax 코드 (웹 컨트롤러 버튼 동작), JS 코드 작성<br/>
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

<p align="center">
    <img width="60%" height="60%" src="PortFolio/images/임시_배치도.jpg" ><br/>
    <span><b>임시 핀 배치</b></span>
    <img width="60%" height="60%" src="PortFolio/images/모듈_임시_고정.jpg" ><br/>
    <span><b>모듈 일부 고정</b></span>
</p> 

- Raspberry Pi 핀 / Bread Board 임시 배치, Smart Farm 모듈 일부 고정<br/>

<p align="center">
    <img width="60%" height="60%" src="PortFolio/images/UI_변경_210809.jpg" ><br/>
    <span><b>UI 일부 수정</b></span>
</p> 

- UI 부분 삭제, 생성 및 변경<br/>
> 1. FAN 버튼 우측 상단과 하단측 중복<br/>
> 2. UI 부분 리프레시 버튼 추가<br/>

---

### 21.08.10 (화)

<p align="center">
    <img width="60%" height="60%" src="PortFolio/images/릴레이_작동.webp" ><br/>
    <span><b>릴레이 센서 동작 확인</b></span>
</p> 

- 배치도에 따른 동작 확인<br/>

<p align="center">
    <img width="60%" height="60%" src="PortFolio/images/smart_farm_db.jpg><br/>
    <span><b>Smart Farm Database & SQL</b></span>
</p> 

- Smart Farm Database 및 SQL 작성<br/>

---

### 21.08.11 (수)

- UI 재배치 및 버튼(토양 수분 센서 측정) 추가<br/>
- GPIO 코드 (웹 UI 위젯 클릭 시 센서 제어 기능, 주기적인 측정), JS 코드 작성<br/>


---

### 21.08.12 (목)

- 배선 작업<br/>
