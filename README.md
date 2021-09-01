# Smart Farm Project 🌱

실내, 홈 가드닝을 위한 Smart Farm Project 입니다.

> __Smart Farm 기능__ <br/>
>> 1. 회원 가입 및 로그인 (검증, 확인, 유효성 검사) <br/>
>> 2. 카메라 모듈로 식물 상태 확인 (실시간 스트리밍) <br/>
>> 3. LED 센서 밝기 단계별 조절 (UI) <br/>
>> 4. 온습도 측정 (XX.X°C , XX.X%) 및 Smart Farm Kit LCD 출력<br/>
>> 5. FAN-IN, FAN-OUT 팬 모듈 ON/OFF<br/>
>> 6. 수위 센서를 통한 수통 잔여 청수량 (%) 확인 <br/>
>> 7. 토양 수분 센서를 통한 토양 습도 측정 (%) <br/>
>> 8. 조도 센서를 통한 밝기 측정 (lx) <br/>
>> 9. 실시간 채팅 및 센서 작동 로그 출력 (날짜별 log.txt 작성됨) <br/>
>> 10. Log-out, Refresh, Shutdown 기능 제공 <br/>


## Smart Farm Project Members (5명)

__- 강동훈 😊 (https://github.com/Kang0325)__ <br/>
__- 정재윤 😃 (https://github.com/1994wjdwodbs)__ <br/>
__- 하진우 😏 (https://github.com/WhiteHair-H)__ <br/>
__- 편상현 😁 (https://github.com/vustkdgus)__ <br/>
__- 조희지 😆 (https://github.com/zizi0308)__ <br/>

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

- 파이썬 코드 (Flask Demo, 실시간 스트리밍) 작성<br/>
- CSS, HTML 코드 (기본 구조) 작성<br/>

---

### 21.08.03 (화)

- Ajax 데모 코드 작성<br/>

<p align="center">
    <img width="70%" height="70%" src="PortFolio/images/waterpump.jpg" ><br/>
    <img width="70%" height="70%" src="PortFolio/images/mcp3008_and_light.jpg" ><br/>
    <span><b>워터펌프, 조도센서</b></span>
</p>

- 파이썬 코드 (워터 펌프 가동 확인 및 데모, 릴레이 모듈 제어) 작성<br/>
- 파이썬 코드 (조도 센서 확인 및 데모 (밝기별 전압)) 작성<br/>

---

### 21.08.04 (수)

<p align="center">
    <img width="30%" height="30%" src="PortFolio/images/led_light.jpg" ><br/>
    <span><b>LED 센서</b></span>
</p>

- 파이썬 코드(LED 센서 확인 및 데모(단계별 조절)) 작성<br/>

<p align="center">
    <img width="65%" height="65%" src="PortFolio/images/ajax_sensor.jpg" ><br/>
    <span><b>센서 버튼 동작 확인</b></span>
</p>

- Ajax 코드 (웹 컨트롤러 버튼 동작), JS 코드 작성<br/>
- JS, CSS 파일 캐싱 문제 해결<br/>

---

### 21.08.05 (목)

<p align="center">
    <img width="30%" height="20%" src="PortFolio/images/sensor_lcd.jpg" ><br/>
    <span><b>온습도 센서 및 결과 LCD 출력</b></span>
</p>

- 파이썬 코드(온습도 센서 및 I2C LCD 모듈 확인 및 데모 (온습도 표기)) 작성<br/>

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

- 파이썬 코드 (수위 센서 확인 및 데모 (전위차)) 작성<br/>
- 파이썬 코드 (토양 수분 센서 확인 및 데모 (전위차)) 작성<br/>

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
> - MCP3008 모듈 고장, 다음 주 수요일(21-08-11)까지 배송 예정 __(Solved)__ <br/>
> - 센서 측정 값 비일관적, 해결 방법 모색 __(Solved)__ <br/>

---

### 21.08.09 (월)

<p align="center">
    <img width="60%" height="60%" src="PortFolio/images/임시_배치_.jpg" ><br/>
    <span><b>임시 핀 배치</b></span><br/>
    <img width="60%" height="60%" src="PortFolio/images/모듈_임시_고정_.jpg" ><br/>
    <span><b>모듈 일부 고정</b></span>
</p> 

- Raspberry Pi 핀 / Bread Board 임시 배치, Smart Farm 모듈 일부 고정<br/>

<p align="center">
    <img width="60%" height="60%" src="PortFolio/images/UI_변경_210809.jpg" ><br/>
    <span><b>UI 일부 수정</b></span>
</p> 

- HTML, CSS 코드 (UI 부분 삭제, 생성 및 변경) 수정<br/>
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
    <img width="60%" height="60%" src="PortFolio/images/smart_farm_db.jpg"><br/>
    <span><b>Smart Farm Database & Init SQL</b></span>
</p> 

- Smart Farm Database 및 테이블 작성/초기화 SQL 작성<br/>
- 파이썬 코드 (로그인/회원가입/세션 별 접근) 작성<br/>
- HTML, JS 코드 (로그인/회원가입 연결) 작성<br/>
---

### 21.08.11 (수)

<p align="center">
    <img width="60%" height="60%" src="PortFolio/images/ui개편.webp" ><br/>
    <span><b>Smart Farm UI 최종 변경</b></span>
</p> 

- UI 재배치 및 필요 없는 버튼 삭제<br/>
- GPIO 코드 (웹 UI 위젯 클릭 시 센서 제어 및 주기적인 측정 & DB 기록)
- Ajax 코드, JS 코드 (웹 UI) 작성<br/>

---

### 21.08.12 (목)

<p align="center">
    <img width="60%" height="60%" src="PortFolio/images/Smart_Farm_모듈_센서_배치_완료.jpg" ><br/>
    <span><b>Smart Farm 모듈 및 센서 배치 완료</b></span>
</p> 

- Smart Farm 전체 모듈 고정 & 일부 배선 작업<br/>
- 모듈 별 동작 확인<br/>

---

### 21.08.13 (금)

<p align="center">
    <img width="33%" height="60%" src="PortFolio/images/최종_배치도_1.jpg" >
    <img width="33%" height="60%" src="PortFolio/images/최종_배치도_2.jpg" >
    <img width="33%" height="60%" src="PortFolio/images/최종_배치도_3.jpg" ><br/>
    <span><b>Smart Farm 모듈 및 센서 최종 배치 완료</b></span>
</p> 

- Smart Farm 최종 배치 작업<br/>
- (DEMO) 전체 동작 점검 및 확인<br/>

#### Issue
> -  워터 펌프 및 LCD 모니터 충돌 문제 (전압) 발생 __(Solved)__ <br/>
> - 센서 측정 값 비일관적, 해결 방법 모색 __(Solved)__ <br/>

---

### 21.08.14 (토)

<p align="center">
    <img src="PortFolio/images/smartfarm_socket코드_클라.JPG"><
    <span><b>Smart Farm Ajax 및 Socket.io 코드 부분</b></span>
</p> 

- Ajax 코드 (일정 주기(3초) 마다 측정 값/센서 리프레시) 작성<br/>
- JS 코드 (Web-Socket 클라이언트 부분) 작성<br/>

<p align="center">
    <img width="60%" height="60%" src="PortFolio/images/smartfarm_윗면.JPG" ><br/>
    <span><b>Smart Farm 최종 외관</b></span>
</p> 

- Smart Farm 재배치 및 외관 수정<br/>

---

### 21.08.15 (일)

<p align="center">
    <img width="60%" height="60%" src="PortFolio/images/smartfarm_socket코드.JPG" ><br/>
    <span><b>Python Socket.io 코드</b></span>
</p> 

- 파이썬 코드 (Web-socket 서버 부분) 작성<br/>

<p align="center">
    <img width="60%" height="60%" src="PortFolio/images/smartfarm_ui_02.png" ><br/>
    <span><b>채팅 및 로그 확인</b></span>
</p> 

- 실시간 채팅 및 로그 전달 테스트<br/>

<p align="center">
    <img src="PortFolio/images/smartfarm_실기동작_01.webp" ><br/>
    <span><b>Smart Farm 작동 확인</b></span>
</p> 

- Smart Farm 최종 작동 확인<br/>
