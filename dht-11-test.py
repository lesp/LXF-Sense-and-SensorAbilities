import RPi.GPIO as GPIO
import dht11
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

instance = dht11.DHT11(pin = 14)
while True:
    result = instance.read()
    if result.is_valid():
        print('The temperature is: %.1f Celsius and the humidity is %.1f %%' % (result.temperature, result.humidity))
    else:
        print("Error: %d" % result.error_code)
    sleep(1)
