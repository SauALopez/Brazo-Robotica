from time import sleep
import RPi.GPIO as GPIO
from CONSTANTES import *
from CineamaticaInversa import *


#BANDERA DE HOMMING
BANDERAS = []
BANDERAS = [ False, False, False]
###################

##############################################################
#                                                            #
#               DEFINICION DE CONFIGURACIONES                #            
#                                                            #
############################################################## 
def GPIO_SETUP():
    global garra
    ######################
    ##GPIO CONFIGURATION##
    GPIO.setmode(GPIO.BCM)          
    GPIO.setwarnings(False)
    GPIO.setup(DIR_BASE, GPIO.OUT)
    GPIO.setup(DIR_LINK1,GPIO.OUT)
    GPIO.setup(DIR_LINK2,GPIO.OUT)
    GPIO.setup(PASO_BASE, GPIO.OUT)
    GPIO.setup(PASO_LINK1,GPIO.OUT)
    GPIO.setup(PASO_LINK2,GPIO.OUT)
    GPIO.setup(HOM_BASE,  GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(HOM_LINK1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(HOM_LINK2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    ###GARRA CONFIGURATION
    GPIO.setup(SERVO, GPIO.OUT)
    garra = GPIO.PWM(SERVO, 100)
    garra.start(7.55)
    ######################


##############################################################
#                                                            #
#               DEFINICION DE INTERRUPCIONES                 #            
#                                                            #
############################################################## 
def Homming_Base(channel):
    global BANDERAS
    print("BASE SE ENCUENTRA EN CASA")
    BANDERAS[0] = True
    pass

def Homming_LINK1(channel):
    global BANDERAS
    print("LINK1 SE ENCUENTRA EN CASA")
    BANDERAS[1] = True
    pass

def Homming_LINK2(channel):
    global BANDERAS
    print("LINK2 SE ENCUENTRA EN CASA")  
    BANDERAS[2] = True
    pass
##############################################################
#                                                            #
#               DEFINICION DE CONFIGURACIONES, INT           #            
#                                                            #
############################################################## 
def Interrupt_Setup():
    GPIO.add_event_detect(HOM_BASE, GPIO.FALLING, callback=Homming_Base, bouncetime=1000)
    GPIO.add_event_detect(HOM_LINK1, GPIO.FALLING, callback=Homming_LINK1, bouncetime=1000)
    GPIO.add_event_detect(HOM_LINK2, GPIO.FALLING, callback=Homming_LINK2, bouncetime=1000)

##############################################################
#                                                            #
#               DEFINICION DE REGRESO A HOME->BASE           #            
#                                                            #
############################################################## 
def MOVE_HOME_BASE():
    global BANDERAS
    GPIO.output(DIR_BASE,DIR_HOME_BASE)
    while 1:
        if(BANDERAS[0]):
            break
        else:
            GPIO.output(PASO_BASE,GPIO.HIGH)
            sleep(delay)
            GPIO.output(PASO_BASE,GPIO.LOW)
            sleep(delay)
##############################################################
#                                                            #
#               DEFINICION DE REGRESO A HOME->LINK1          #            
#                                                            #
############################################################## 
def MOVE_HOME_LINK1(pasos):
    global BANDERAS
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
##############################################################
#                                                            #
#               DEFINICION DE REGRESO A HOME->LINK2          #            
#                                                            #
############################################################## 
def MOVE_HOME_LINK2(pasos):
    global BANDERAS
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
##############################################################
#                                                            #
#               DEFINICION DE REGRESO A HOME                 #            
#                                                            #
############################################################## 
def MOVE_HOME(actual):
    
    global BANDERAS
    BANDERAS = [False,False,False]
    while 1:
        if (BANDERAS[1] and BANDERAS[2]):
            break
        else:
            MOVE_HOME_LINK2(6)
            MOVE_HOME_LINK1(1)
    MOVE_HOME_BASE()
    actual= [0,0,0]
    return actual
##############################################################
#                                                            #
#               DEFINICION DE MOVIMIENTO BASE                #            
#                                                            #
############################################################## 
def MOV_BASE(ang,actual):
    ang =  ang - actual[0]      #DIFERENCIA PARA MOVER RESPECTO A LA POSICION ACTUAL
    if  ang <0:                 #CONDICION PARA LA DIRECCION DEL MOTOR
        GPIO.output(DIR_BASE,DIR_HOME_BASE)
    else:
        GPIO.output(DIR_BASE,DIR_OUT_BASE) 
    x =0
    pasos = (abs(ang))*((MICRO_STEPPING*ENG_BASE)/(360*ENG_MOTOR))  #RELACION ANGULOS DE PASOS
    while 1:
        if x >=pasos:
            break
        else:
            GPIO.output(PASO_BASE,GPIO.HIGH)
            sleep(delay)
            GPIO.output(PASO_BASE,GPIO.LOW)
            sleep(delay)
            x =x+1
    actual[0] = ang + actual[0] -0.1
    return actual
##############################################################
#                                                            #
#               DEFINICION DE MOVIMIENTOS DE LINKS           #            
#                                                            #
##############################################################     
def MOV_LINKS(ang1,ang2,actual):
    ang1 = ang1 - actual[1]         #DIFERENCIA PARA MOVER RESPECTO
    ang2 = ang2 - actual[2]         #A LA POSICION ACTUAL            
    #ANG1
    pasos1 = (abs(ang1)) *((MICRO_STEPPING*ENG_LINK1)/(360*ENG_MOTOR))  #RELACION DE ANGULO A PASOS
    if  ang1 <0:                                #CONDICIONAL PARA LA DIRECCION
        GPIO.output(DIR_LINK1,DIR_HOME_LINK1)   #DEL MOTOR
    else:
        GPIO.output(DIR_LINK1,DIR_OUT_LINK1)    
    #ANG2
    pasos2 = (abs(ang2)) * ((MICRO_STEPPING*ENG_LINK2)/(360*ENG_MOTOR)) #RELACION DE ANGULO A PASOS
    if  ang2 <0:                                #CONDICION PARA LA DIRECCION
        GPIO.output(DIR_LINK2,DIR_HOME_LINK2)   #DEL MOTOR
    else:
        GPIO.output(DIR_LINK2,DIR_OUT_LINK2)

    x1=0
    x2=0
    for i in range(int(pasos1/3)):
        GPIO.output(PASO_LINK1,GPIO.HIGH)
        sleep(delay)
        GPIO.output(PASO_LINK1,GPIO.LOW)
        sleep(delay)
        x1 =x1+1
    for i in range(int(pasos2/3)):
        GPIO.output(PASO_LINK2,GPIO.HIGH)
        sleep(delay)
        GPIO.output(PASO_LINK2,GPIO.LOW)
        sleep(delay)
        x2 =x2+1
    for i in range(int(pasos1 * 2/3)):
        GPIO.output(PASO_LINK1,GPIO.HIGH)
        sleep(delay)
        GPIO.output(PASO_LINK1,GPIO.LOW)
        sleep(delay)
        x1 =x1+1    
    for i in range(int(pasos2*2/3)):
        GPIO.output(PASO_LINK2,GPIO.HIGH)
        sleep(delay)
        GPIO.output(PASO_LINK2,GPIO.LOW)
        sleep(delay)
        x2 =x2+1
    actual[1] = ang1 + actual[1]
    actual[2] = ang2 + actual[2]
    sleep(0.05)
    return actual
##############################################################
#                                                            #
#               DEFINICION DE APERTURA DE GARRA              #            
#                                                            #
##############################################################     
def Garra_Open(ang):
    global garra
    for i in range(ang,180,10):
        garra.ChangeDutyCycle(2+i/18)
        sleep(0.1)
        garra.ChangeDutyCycle(0)
##############################################################
#                                                            #
#               DEFINICION DE CIERRE DE GARRA                #            
#                                                            #
############################################################## 
def Garra_Close(ang):
    global garra
    for i in range(ang,90,-5):
        garra.ChangeDutyCycle(2+i/18)
        sleep(0.1)
        garra.ChangeDutyCycle(0)
##############################################################
#                                                            #
#               DEFINICION DE TRAYECTORIA                    #            
#                                                            #
############################################################## 
def trayectoria(ang1,ang2,actuales):
    while True:
        if actuales[1] < (ang1-4):
            actuales = MOV_LINKS(actuales[1]+4,actuales[2],actuales)
        else:
            actuales = MOV_LINKS(ang1,actuales[2],actuales)
        if actuales[2] < (ang2-2):
            actuales = MOV_LINKS(actuales[1],actuales[2]+2,actuales)
        else:
            actuales = MOV_LINKS(actuales[1],ang2, actuales)
        if (ang1)== actuales[1] and ang2 == actuales[2]:
            break
    return actuales
##############################################################
#                                                            #
#               DEFINICION DE TRAYECTORIA INVERSA            #            
#                                                            #
############################################################## 
def trayectoria_inv(ang1,ang2,actuales):
    while True:
        if actuales[1] > (ang1+4):
            actuales = MOV_LINKS(actuales[1]-4,actuales[2],actuales)
        else:
            actuales = MOV_LINKS(ang1,actuales[2],actuales)
        if actuales[2] > (ang2+2):
            actuales = MOV_LINKS(actuales[1],actuales[2]-2,actuales)
        else:
            actuales = MOV_LINKS(actuales[1],ang2, actuales)
        if (ang1)== actuales[1] and ang2 == actuales[2]:
            break
    return actuales


