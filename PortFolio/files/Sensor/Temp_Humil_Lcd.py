import RPi.GPIO as GPIO
import dht11
import drivers
import time

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# initialize LCD
display = drivers.Lcd()

# read data using pin 21
instance = dht11.DHT11(pin = 24)
try:
	while True:
		result = instance.read()
		time.sleep(1)
		
		if result.is_valid():
			print("Temp : %-3.1f C" % result.temperature)
			print("Hum  : %-3.1f %%" % result.humidity)
			display.lcd_display_string("Temp : %-3.1f C" % result.temperature, 1)
			display.lcd_display_string("Hum  : %-3.1f %%" % result.humidity, 2)
		else:
			print("Error: %d" % result.error_code)
		
except KeyboardInterrupt:
    print("Cleaning up!!")
    display.lcd_clear()
    GPIO.cleanup()
