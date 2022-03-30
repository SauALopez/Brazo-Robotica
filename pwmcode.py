import RPi.GPIO as GPIO
from time import sleep
from CONSTANTES import *

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

p = GPIO.PWM(17, 100)
p.start(5)
try:
    while(1):
        angle = float(input('angulo:'))
        p.ChangeDutyCycle(2+(angle/18))
        sleep(0.1)
        p.ChangeDutyCycle(0)      
except KeyboardInterrupt: 
    print("Program stopped via keyboard interrupt")
    p.stop()
    GPIO.cleanup() 