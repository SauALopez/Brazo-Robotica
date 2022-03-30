
###############################################################
#                                                            #
#               CONSTANTES RASPI Y ENGRANAJES                #            
#                                                            #
############################################################## 
#################
#NUMEROS DE PINES
DIR_BASE  = 24
DIR_LINK1 = 12
DIR_LINK2 = 18

PASO_BASE  = 25
PASO_LINK1 = 16
PASO_LINK2 = 23

HOM_BASE  = 13
HOM_LINK1 = 27
HOM_LINK2 = 22

SERVO = 17
###################
#CONSTANTES STEPPER
PASOSXREV = 360/1.8
delay = 1/(PASOSXREV*4)
###################
#CONSTATNES ENGRANAJES 
ENG_MOTOR = 19
ENG_BASE = 108
ENG_LINK1 = 47
ENG_LINK2 = 47

MICRO_STEPPING = PASOSXREV*8
#################################
#DIRECCION LOGICA PARA EL STEPPER
#################################
DIR_HOME_BASE  = 1
DIR_HOME_LINK1 = 1
DIR_HOME_LINK2 = 1

DIR_OUT_BASE  = 0
DIR_OUT_LINK1 = 0
DIR_OUT_LINK2 = 0

