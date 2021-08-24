import RPi.GPIO as GPIO
import time
import drivers
import dht11

# GPIO 모듈별 핀 번호
LED_PIN = 23
FAN_IN_PIN = 27
FAN_OUT_PIN = 22
PUMP_PIN = 17
TEMP_HUMI_PIN = 24
SOIL_HUMI_PIN = 25

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

    # 센서 별로 Value에 따른 메소드 정의
    # Set Fan-In
    def SetFanIn(self, arg_val):
        if arg_val: # True
            GPIO.output(FAN_IN_PIN, GPIO.LOW)
            pass
        else: # False
            GPIO.output(FAN_IN_PIN, GPIO.HIGH)
            pass
    # Set Fan-Out
    def SetFanOut(self, arg_val):
        if arg_val: # True
            GPIO.output(FAN_OUT_PIN, GPIO.LOW)
            pass
        else: # False
            GPIO.output(FAN_OUT_PIN, GPIO.HIGH)
            pass

    def close(self):
        self.pwm.stop()
        self.display.lcd_clear()
        GPIO.cleanup()

def SetPump(arg_val):
    pass

def SetLedLight(arg_val):
    pass

def CheckTempHumi():
    pass

def CheckSoil():
    pass

# 센서 동작 체크
x = Sensors()
x.SetFanIn(True)
time.sleep(5)
x.SetFanIn(False)
x.SetFanOut(True)
time.sleep(5)
x.close()