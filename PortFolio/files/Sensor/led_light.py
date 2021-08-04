import RPi.GPIO as GPIO
import time

ledPin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

p = GPIO.PWM(ledPin, 100)
duty = 0 #(1~100)
p.start(duty)

try :
    # GPIO.output(ledPin, True)
    while duty < 100:
        duty += 1
        p.ChangeDutyCycle(duty)
        print("duty : " + str(duty))
        time.sleep(0.1)
    p.stop()
finally :
    GPIO.cleanup()