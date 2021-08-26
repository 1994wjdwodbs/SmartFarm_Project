import RPi.GPIO as GPIO
import time
import drivers

import spidev
import dht11

import threading

# SF_machine database 제어용 py
import sf_db

# GPIO 모듈별 핀 번호
LED_PIN = 23
FAN_IN_PIN = 27
FAN_OUT_PIN = 22
PUMP_PIN = 17
TEMP_HUMI_PIN = 24
SOIL_HUMI_PIN = 25

# Thread용 변수(GLOBAL)
temp_humi_flag = True
check_level_flag = True

class Sensors:
    def __init__(self):
        GPIO.cleanup()
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        # GPIO 세팅
        GPIO.setup(PUMP_PIN, GPIO.OUT)
        GPIO.setup(FAN_IN_PIN, GPIO.OUT)
        GPIO.setup(FAN_OUT_PIN, GPIO.OUT)
        GPIO.setup(SOIL_HUMI_PIN, GPIO.OUT)

        # 릴레이값 초기화
        GPIO.output(PUMP_PIN, GPIO.HIGH)
        GPIO.output(FAN_IN_PIN, GPIO.HIGH)
        GPIO.output(FAN_OUT_PIN, GPIO.HIGH)
        GPIO.output(SOIL_HUMI_PIN, GPIO.HIGH)

        GPIO.setup(LED_PIN, GPIO.OUT)
        self.pwm = GPIO.PWM(LED_PIN, 100)
        self.pwm.start(0)

        # LCD 초기화
        self.display = drivers.Lcd()

        # 온습도 센서 초기화
        self.instance = dht11.DHT11(TEMP_HUMI_PIN)

        # 아날로그 측정 초기화
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 1350000

    # 센서 별로 Value에 따른 메소드 정의
    # Set Fan-In
    def SetFanIn(self, arg_val):
        if arg_val: # True
            GPIO.output(FAN_IN_PIN, GPIO.LOW)
        else: # False
            GPIO.output(FAN_IN_PIN, GPIO.HIGH)

    # Set Fan-Out
    def SetFanOut(self, arg_val):
        if arg_val: # True
            GPIO.output(FAN_OUT_PIN, GPIO.LOW)
        else: # False
            GPIO.output(FAN_OUT_PIN, GPIO.HIGH)

    # Set Pump
    def SetPump(self, arg_val):
        if arg_val: # True
            GPIO.output(PUMP_PIN, GPIO.LOW)
        else: # False
            GPIO.output(PUMP_PIN, GPIO.HIGH)

    # Set LED LIGHT
    def SetLedLight(self, arg_val):
        self.pwm.ChangeDutyCycle(arg_val)

    # 온/습도 센서 체크 + DB값 갱신 + LCD 출력
    def CheckTempHumi(self):
        global temp_humi_flag
        instance = dht11.DHT11(TEMP_HUMI_PIN)

        while temp_humi_flag:
            result = instance.read()
            time.sleep(5)
            
            if result.is_valid():
                sf_db.SetProperty("temp", result.temperature)
                sf_db.SetProperty("humi", result.humidity)

                print("Temp : %-3.1f C" % result.temperature)
                print("Hum  : %-3.1f %%" % result.humidity)
                # 전압이 부족하거나 전선이 빠져있을 경우 I/O ERROR 일어남
                self.display.lcd_display_string("Temp : %-3.1f C" % result.temperature, 1)
                self.display.lcd_display_string("Hum  : %-3.1f %%" % result.humidity, 2)
            else:
                print("Error: %d" % result.error_code)

    # 토양 센서 측정용 전원
    def SetSoil(self, arg_val):
        if arg_val: # True
            GPIO.output(SOIL_HUMI_PIN, GPIO.LOW)
        else: # False
            GPIO.output(SOIL_HUMI_PIN, GPIO.HIGH)
            
    # 아날로그 센서 체크
    def CheckLevel(self):
        global check_level_flag

        while check_level_flag:
            for ch in range(0, 3):
                r = self.spi.xfer2([1, (8 + ch) << 4, 0])
                reading = ((r[1]&3) << 8) + r[2]
                voltage = reading * 3.3 / 1024
                print("Readed data[%d] : %d\t Voltage %f V" % (ch, reading, voltage))
            time.sleep(1)

    def close(self):
        self.pwm.stop()
        self.display.lcd_clear()
        GPIO.cleanup()
        print("GPIO CLEANUP!")

# 센서 동작 체크
# x = Sensors()
# x.SetLedLight(0)
# temp_humi_t = threading.Thread(target=x.CheckTempHumi)
# temp_humi_t.start()
# check_level_t = threading.Thread(target=x.CheckLevel)
# check_level_t.start()
# x.SetFanIn(True)
# x.SetPump(True)
# x.SetSoil(True)
# time.sleep(10)
# x.SetFanIn(False)
# x.SetFanOut(True)
# x.SetPump(False)
# x.SetSoil(False)
# print(sf_db.GetAllProperty())
# x.SetLedLight(70)
# time.sleep(5)
# temp_humi_flag = False
# check_level_flag = False
# x.close()