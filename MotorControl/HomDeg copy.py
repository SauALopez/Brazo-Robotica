from time import sleep
import RPi.GPIO as GPIO
from CONSTANTES import *

def GPIO_SETUP():
    ######################
    ##GPIO CONFIGURATION##
    GPIO.setmode(GPIO.BCM)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR_BASE, GPIO.OUT)
    GPIO.setup(DIR_LINK1,GPIO.OUT)
    GPIO.setup(DIR_LINK2,GPIO.OUT)
    GPIO.setup(PASO_BASE, GPIO.OUT)
    GPIO.setup(PASO_LINK1,GPIO.OUT)
    GPIO.setup(PASO_LINK2,GPIO.OUT)
    GPIO.setup(HOM_BASE,  GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(HOM_LINK1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(HOM_LINK2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    ######################

BANDERAS = []
BANDERAS = [ False, False, False]

def Homming_Base(channel):
    print("BASE SE ENCUENTRA EN CASA")
    BANDERAS[0] = True
    pass

def Homming_LINK1(channel):
    print("LINK1 SE ENCUNETRA EN CASA")
    BANDERAS[1] = True
    pass

def Homming_LINK2(channel):
    print("LINK2 SE ENCUNETRA EN CASA")  
    BANDERAS[2] = True
    pass
def Interrupt_Setup():
    GPIO.add_event_detect(HOM_BASE, GPIO.FALLING, callback=Homming_Base, bouncetime=1000)
    GPIO.add_event_detect(HOM_LINK1, GPIO.FALLING, callback=Homming_LINK1, bouncetime=1000)
    GPIO.add_event_detect(HOM_LINK2, GPIO.FALLING, callback=Homming_LINK2, bouncetime=1000)

def MOVE_HOME_BASE():
    GPIO.output(DIR_BASE,DIR_HOME_BASE)
    while 1:
        if(BANDERAS[0]):
            break
        else:
            GPIO.output(PASO_BASE,GPIO.HIGH)
            sleep(delay)
            GPIO.output(PASO_BASE,GPIO.LOW)
            sleep(delay)
def MOVE_HOME_LINK1(pasos):
    x=0
    GPIO.output(DIR_LINK1,DIR_HOME_LINK1)
    while 1:
        if x > pasos:
            break
        if(BANDERAS[1]):
            break
        else:
            GPIO.output(PASO_LINK1,GPIO.HIGH)
            sleep(delay)
            GPIO.output(PASO_LINK1,GPIO.LOW)
            sleep(delay)
            x = x+1

def MOVE_HOME_LINK2(pasos):
    GPIO.output(DIR_LINK2,DIR_HOME_LINK2)
    x=0
    while 1:
        if x > pasos:
            break
        if(BANDERAS[2]):
            break
        else:
            GPIO.output(PASO_LINK2,GPIO.HIGH)
            sleep(delay)
            GPIO.output(PASO_LINK2,GPIO.LOW)
            sleep(delay)
            x = x+1

def MOVE_HOME():
    while 1:
        if (BANDERAS == [False,True,True]):
            break
        else:
            MOVE_HOME_LINK2(5)
            MOVE_HOME_LINK1(5)
    MOVE_HOME_BASE()

def MOV_BASE(ang):
    GPIO.output(DIR_BASE,DIR_OUT_BASE)
    x =0
    pasos = ang*((MICRO_STEPPING*ENG_BASE)/(360*ENG_MOTOR))
    while 1:
        if x >pasos:
            break
        else:
            GPIO.output(PASO_BASE,GPIO.HIGH)
            sleep(delay)
            GPIO.output(PASO_BASE,GPIO.LOW)
            sleep(delay)
            x =x+1    

def MOV_LINK1(ang):
    GPIO.output(DIR_LINK1,DIR_OUT_LINK1)
    x =0
    if ang > 145 :
        print("Angulo muy grande,angulo maximo colocado")
        ang =145
    pasos = (ang-20) * ((MICRO_STEPPING*ENG_BASE)/(360*ENG_MOTOR))
    while 1:
        if x >pasos:
            break
        else:
            GPIO.output(PASO_LINK1,GPIO.HIGH)
            sleep(delay)
            GPIO.output(PASO_LINK1,GPIO.LOW)
            sleep(delay)
            x =x+1
def MOV_LINK2(ang):
    GPIO.output(DIR_LINK2,DIR_OUT_LINK2)
    x =0
    ang = 90 - ang +27
    pasos = (ang) * ((MICRO_STEPPING*ENG_BASE)/(360*ENG_MOTOR))
    while 1: 
        if x >pasos:
            break
        else:
            GPIO.output(PASO_LINK2,GPIO.HIGH)
            sleep(delay)
            GPIO.output(PASO_LINK2,GPIO.LOW)
            sleep(delay)
            x =x+1

def MOV_LINKS(ang1,ang2):
    GPIO.output(DIR_LINK1,DIR_OUT_LINK1)
    GPIO.output(DIR_LINK2,DIR_OUT_LINK2)
    #ANG1
    if ang1 >145 :
        ang1 = 145
    pasos1 = (180-ang1) *((MICRO_STEPPING*ENG_LINK1)/(360*ENG_MOTOR))
    #ANG2S
    ang2 = 90 -ang2 + 40
    pasos2 = ang2 * ((MICRO_STEPPING*ENG_LINK2)/(360*ENG_MOTOR))
    x1=0
    x2=0
    while 1:
        if ang1 < 90:
            if x1 > pasos1/2:
                if x2> pasos2:
                    GPIO.output(PASO_LINK1,GPIO.HIGH)
                    sleep(delay)
                    GPIO.output(PASO_LINK1,GPIO.LOW)
                    sleep(delay)
                    x1 = x1 +1  
            else:
                GPIO.output(PASO_LINK1,GPIO.HIGH)
                sleep(delay)
                GPIO.output(PASO_LINK1,GPIO.LOW)
                sleep(delay)
                x1 = x1 +1
        else:
            if x1 > pasos1:
                 pass
            else:
                GPIO.output(PASO_LINK1,GPIO.HIGH)
                sleep(delay)
                GPIO.output(PASO_LINK1,GPIO.LOW)
                sleep(delay)
                x1 = x1 +1
        if x2 > pasos2:
            pass
        else:
            GPIO.output(PASO_LINK2,GPIO.HIGH)
            sleep(delay)
            GPIO.output(PASO_LINK2,GPIO.LOW)
            sleep(delay)
            x2 = x2 +1
        if (x2 > pasos2) and (x1 > pasos1):
            break
        
        
            


