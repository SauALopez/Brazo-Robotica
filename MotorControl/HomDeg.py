from time import sleep
import RPI.GPIO as GPIO
from PIN_LAYOUT import *

GPIO.setmode(GPIO.BCM)
BANDERAS = []
######################
##GPIO CONFIGURATION##
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_BASE, GPIO.OUT)
GPIO.setup(DIR_LINK1,GPIO.OUT)
GPIO.setup(DIR_LINK2,GPIO.OUT)
GPIO.setup(PASO_BASE, GPIO.OUT)
GPIO.setup(PASO_LINK1,GPIO.OUT)
GPIO.Setup(PASO_LINK2,GPIO.OUT)
GPIO.setup(HOM_BASE,  GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(HOM_LINK1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(HOM_LINK2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
######################
BANDERAS = [ False, False, False]
def Homming_Base(channel):
    print("BASE SE ENCUENTRA EN CASA")
    BANDERAS[1]= True

def Homming_LINK1(channel):
    print("LINK1 SE ENCUNETRA EN CASA")
    BANDERAS[2]= True

def Homming_LINK2(channel):
    print("LINK2 SE ENCUNETRA EN CASA")
    BANDERAS[3]= True   