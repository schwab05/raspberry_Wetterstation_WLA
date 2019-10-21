import RPi.GPIO as GPIO

temp = 0
preassure = 0
humidity = 0
buttonpin = 17
ledpin = 18


reset = False
refresh = False


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(buttonpin, GPIO.IN)
GPIO.setup(ledpin, GPIO.OUT)

while True:
    if  GPIO.input(buttonpin) == 1:
        GPIO.output(ledpin, GPIO.HIGH)


