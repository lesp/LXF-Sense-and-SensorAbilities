from w1thermsensor import W1ThermSensor
import RPi.GPIO as GPIO
import dht11
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

sensor = W1ThermSensor()
instance = dht11.DHT11(pin = 14)

while True:
    result = instance.read()
    temperature = sensor.get_temperature()
    if result.is_valid():
        print('DHT11 temperature is: %.1f Celsius and the humidity is %.1f %%' % (result.temperature, result.humidity))
        print("DS18B20 temperature is %s celsius" % temperature)
    else:
        print("Error: %d" % result.error_code)
    sleep(1)
