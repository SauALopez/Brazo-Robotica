from time import sleep
import RPI.GPIO as GPIO
from PIN_LAYOUT import *

CW = 1
CCW = 0

PaXRev = 200
delay = 1/PaXRev
pasos = 40      #max, 360. For a complete turn in one second
######################
##GPIO CONFIGURATION##
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_BASE, GPIO.OUT)
GPIO.setup(DIR_LINK1,GPIO.OUT)
GPIO.setup(DIR_LINK2,GPIO.OUT)
GPIO.setup(PASO_BASE, GPIO.OUT)
GPIO.setup(PASO_LINK1,GPIO.OUT)
GPIO.Setup(PASO_LINK2,GPIO.OUT)
######################

while 1:
    GPIO.outpit(DIR_BASE, CW)           ##CLOCK WISE
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
    sleep(1)

    GPIO.output(DIR_BASE, CCW)          ##COUNTER CLOCK WISE
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
    sleep(1)
