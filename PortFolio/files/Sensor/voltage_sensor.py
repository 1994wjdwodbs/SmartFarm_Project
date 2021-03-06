# 정확한 측정을 하려면 MCP3008이 필요하다.
# 나머지 측정 센서들도 동일한 방식으로 전위차 값을 대조하면 된다.
# readad.py
import spidev, time
import RPi.GPIO as GPIO

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1350000

relay = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay, GPIO.OUT)

GPIO.output(relay, GPIO.LOW)

def analog_read(channel):
	r = spi.xfer2([1, (8 + channel) << 4, 0])
	adc_out = ((r[1]&3) << 8) + r[2]
	return adc_out

while True:
	try:
		for i in range(2, 4):
			reading = analog_read(i)
			voltage = reading * 3.3 / 1024
			print("Readed data[%d] : %d\t Voltage %f V" % (i, reading, voltage))
		time.sleep(1)

	except KeyboardInterrupt:
		GPIO.cleanup()
		break
