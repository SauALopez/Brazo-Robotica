from time import sleep
import RPi.GPIO as GPIO
from PIN_LAYOUT import *

CW = 0
CCW = 1

PaXRev = 200
delay = 1/(PaXRev)
pasos = 30      #max, 360. For a complete turn in one second
######################
##GPIO CONFIGURATION##
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_BASE, GPIO.OUT)
GPIO.setup(DIR_LINK1,GPIO.OUT)
GPIO.setup(DIR_LINK2,GPIO.OUT)
GPIO.setup(PASO_BASE, GPIO.OUT)
GPIO.setup(PASO_LINK1,GPIO.OUT)
GPIO.setup(PASO_LINK2,GPIO.OUT)
######################

while 1:
    print("CW")
    GPIO.output(DIR_BASE, CW)           ##CLOCK WISE
    GPIO.output(DIR_LINK1,CW)
    GPIO.output(DIR_LINK2,CW)
    for x in range(pasos):
        GPIO.output(PASO_BASE, GPIO.HIGH)
        GPIO.output(PASO_LINK1, GPIO.HIGH)
        GPIO.output(PASO_LINK2, GPIO.HIGH)
        sleep(delay)
        GPIO.output(PASO_BASE, GPIO.LOW)
        GPIO.output(PASO_LINK1, GPIO.LOW)
        GPIO.output(PASO_LINK2, GPIO.LOW)
        sleep(delay)
    #########################################
    sleep(10)
    print("CCW")
    GPIO.output(DIR_BASE, CCW)          ##COUNTER CLOCK WISE
    GPIO.output(DIR_LINK1,CCW)
    GPIO.output(DIR_LINK2,CCW)
    for x in range(pasos):
        GPIO.output(PASO_BASE, GPIO.HIGH)
        GPIO.output(PASO_LINK1, GPIO.HIGH)
        GPIO.output(PASO_LINK2, GPIO.HIGH)
        sleep(delay)
        GPIO.output(PASO_BASE, GPIO.LOW)
        GPIO.output(PASO_LINK1, GPIO.LOW)
        GPIO.output(PASO_LINK2, GPIO.LOW)
        sleep(delay)
    ##########################################
    sleep(10)
