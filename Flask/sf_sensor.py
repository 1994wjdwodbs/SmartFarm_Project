import RPi.GPIO as GPIO

# GPIO 모듈별 핀 번호
LED = 
FAN_IN =
FAN_OUT =
PUMP =
TEMP_HUMI =
SOIL_HUMI =

# GPIO 초기 세팅
def Init():
    pass

# GPIO 종료 (Clean) ##
def Close():
    GPIO.cleanup()

# 센서 별로 Value에 따른 메소드 정의
def SetFanIn(arg_val):
    if arg_val: # True
        pass
    else: # False
        pass

def SetFanOut(arg_val):
    if arg_val: # True
        pass
    else: # False
        pass

def SetPump(arg_val):
    pass

def SetLedLight(arg_val):
    pass

def SetLedLight(arg_val):
    pass

def CheckTempHumi():
    pass

def CheckSoil():
    pass
