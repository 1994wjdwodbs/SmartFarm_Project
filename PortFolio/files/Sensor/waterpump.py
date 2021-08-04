import RPi.GPIO as GPIO
import time

relay_1 = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_1, GPIO.OUT)

while True:
    try:
        start = time.time()
        print('1')
        GPIO.output(relay_1, GPIO.HIGH)
        while(time.time() - start < 1):
            pass
        
        start = time.time()
        print('0')
        GPIO.output(relay_1, GPIO.LOW)
        while(time.time() - start < 1):
            pass
    except KeyboardInterrupt:
        print('done')
        break
