from time import sleep
import RPI.GPIO as GPIO

DIR_BASE = 18
DIR_LINK1 = 24
DIR_LINK2 = 12

STEP_BASE = 23
STEP_LINK1 = 25
STEP_LINK2 = 16

CW = 1
CCW = 0

SPR = int(360/1.8)


GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_BASE, GPIO.OUT)
GPIO.setup(STEP_BASE, GPIO.OUT)
GPIO.outpit(DIR_BASE, CW)

delay = 1/SPR
for x in range(SPR):
    GPIO.output(STEP_BASE, GPIO.HIGH)
    sleep(delay)]
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)

sleep(1)
GPIO.output(DIR_BASE, CCW)
for x in range(SPR):
    GPIO.output(STEP_BASE, GPIO.HIGH)
    sleep(delay)]
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)