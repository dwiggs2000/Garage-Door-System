import RPi.GPIO as GPIO
from time 
GPIO.setwarnings(False)

print("door opening")

servo = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT)

p = GPIO.PWM(servo, 75)

p.start(12.5)

try:
	p.ChangeDutyCycle(12.5)
	time.sleep(5)
	p.ChangeDutyCycle(2.5)
	gpio.stop()
	GPIO.cleanup()

except KeyboardInterrupt:
	p.ChangeDutyCycle(2.5)
	p.stop()
	GPIO.cleanup()
