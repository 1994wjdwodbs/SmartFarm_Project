import RPi.GPIO as GPIO
import time

# relay_1 = 17
# relay_2 = 27
# relay_3 = 22
relay_4 = 25
GPIO.setmode(GPIO.BCM)
# GPIO.setup(relay_1, GPIO.OUT)
# GPIO.setup(relay_2, GPIO.OUT)
# GPIO.setup(relay_3, GPIO.OUT)
GPIO.setup(relay_4, GPIO.OUT)

while True:
    try:
        start = time.time()
        print('1')
        # GPIO.output(relay_1, GPIO.HIGH)
        # GPIO.output(relay_2, GPIO.HIGH)
        # GPIO.output(relay_3, GPIO.HIGH)
        GPIO.output(relay_4, GPIO.HIGH)
        while(time.time() - start < 1):
            pass
        
        start = time.time()
        print('0')
        # GPIO.output(relay_1, GPIO.LOW)
        # GPIO.output(relay_2, GPIO.LOW)
        # GPIO.output(relay_3, GPIO.LOW)
        GPIO.output(relay_4, GPIO.LOW)
        while(time.time() - start < 1):
            pass
    except KeyboardInterrupt:
        print('done')
        break
