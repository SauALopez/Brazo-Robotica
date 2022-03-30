import pygame                   #Importamos las libreria pygame para la interfaz grafica
from HomDeg import *            #Importamos las funciones para el control de motores
from CineamaticaInversa import *#Importamos la funcion de cinemativa inversa
from time import sleep          #Importamos la libreia para el manejo de delays
import RPi.GPIO as GPIO         #Importamos la libreria para controlar los GPIO
import cv2                      #Importamos la libreria cv2
import numpy as np              #Importamos la libreria numpy y le colocamos un alias


captura = cv2.VideoCapture(0)                    #Definimos una variable para nuestra captura
captura.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))   #CAMBIO DE FORMATO
AzulBajo1 = np.array([0,0,0],np.uint8)           #Definimos el color a detectar por medio de intervalos 
AzulAlto1 = np.array([0,0,255],np.uint8)         #Definidos para el HSV, un numero bajo y otro alto

ORIGEN_X = 342          #Definimos el origen de nuestros ejes de coordenadas
ORIGEN_Y = 2            #Definimos el origen de nuestro ejes de cordenadas
CONT_DADO = 0           #Conteo de dados del sistema
GPIO_SETUP()            #Inicializa los GPIO
Interrupt_Setup()       #Configura las interrupciones para los homming
a=[]                    #Lista para los objetos
angulos_actuales=[0,0,0]#Lista de angulos actuales


pygame.init()                               #Inicializacion de pygame
screen = pygame.display.set_mode((640,480)) #Tamanio de ventana
screen.fill((245,230,170))                  #COLOR
pygame.display.set_caption('CONTROL BRAZO') #Titulo de ventana
fuente = pygame.font.SysFont('comicsans',35)#Feunte botones
fuenteD= pygame.font.SysFont('comicsans',25)#FUente botones

print ("INICIO DE CONTROL")                 #cmd, inicio de control


##############################################################
#                                                            #
#                   BLOQUE DE CLASES PYGAME                  #            
#                                                            #
##############################################################
class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,screen,outline=None):

        if outline:
            pygame.draw.rect(screen, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height),0)

        if self.text!='':
            font = pygame.font.SysFont('comicsans',25)
            text = font.render(self.text,1,(0,0,0))
            screen.blit(text,(self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
            
    def isOver (self,pos):

        if pos[0] > self.x and  pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

class buttonS():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,screen,outline=None):

        if outline:
            pygame.draw.rect(screen, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height),0)

        if self.text!='':
            font = pygame.font.SysFont('comicsans',15)
            text = font.render(self.text,1,(255,255,255))
            screen.blit(text,(self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
            
    def isOver (self,pos):

        if pos[0] > self.x and  pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return 
##############################################################
#                                                            #
#              FIN  BLOQUE DE CLASES PYGAME                  #            
#                                                            #
##############################################################
###############################################################
#                                                            #
#               DEFINICION DE VENTANA                        #            
#                                                            #
##############################################################        
def Window0():
    #screen.fill((245,230,170))
    ButtonHome.draw(screen)
    caja1Button.draw(screen)
    caja2Button.draw(screen)
    caja3Button.draw(screen)
    textEstado = fuente.render("ROBOTICA",0,(0,0,0))
    screen.blit(textEstado,(255,350))
    txt = fuenteD.render("SELECCIONE DADO:",0,(0,0,0))
    screen.blit(txt, (235,380))

caja1Button = button((255,255,255), 190, 400, 80, 50, 'DADO 1')
caja2Button = button((255,255,255), 280, 400, 80, 50, 'DADO 2')
caja3Button = button((255,255,255), 370, 400, 80, 50, 'DADO 3')

ButtonHome = buttonS((255,255,255), 5, 5, 28, 10, 'HOME')

####CICLO WHILE####

while 1:

    ret,frame = captura.read()      #Leemos los datos de la captura y obtenemos los argumentos
    ########################
    #DIBUJAMOS LAS LINEAS DE ORIGEN
    cv2.line(frame,(ORIGEN_X,ORIGEN_Y-50),(ORIGEN_X,ORIGEN_Y+50),(0,255,0),1)
    cv2.line(frame,(ORIGEN_X-50,ORIGEN_Y),(ORIGEN_X+50,ORIGEN_Y),(0,255,0),1)
    ##################
    a=[]                            #Inicializacion de lista de objetos
    i=0                             #Inicializacion de numero objetos

    if ret == True:                                                 #Sentencia if cuando el argumento ret sea verdadora (cuando tenemos imagen)
        frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)            #Convertimos la imagen de BGR a HSV
        maskAzul = cv2.inRange(frameHSV,AzulBajo1,AzulAlto1)        #Indicamos que maskRoja1 y maskRoja2 contienen los valores de la imagen 
        contornos,_ = cv2.findContours( maskAzul, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contornos:
            area = cv2.contourArea(c)
            font = cv2.FONT_HERSHEY_SIMPLEX
            x_0,y_0,w,h = cv2.boundingRect(c)
            x=int(x_0+w/2)#coordenada en x del centro del dado
            y=int(y_0+h/2)#coordenada en y del centro del dado
            
            if area > 200:
             ################################
             # RELACION DE PIXELES A ANGULOS   
                Re=0.056947
                Re2=0.054744
            ############Y1 & X1 son la posicion en centimetros vertical y horizontal respectivamente###############
                if y>=ORIGEN_Y:
                    Y1=round(Re2*(y-ORIGEN_Y)+8.8,2)
                else :
                    Y1=-round(Re2*(ORIGEN_Y-y)+8.8,2)
                    
                if x>=ORIGEN_X:
                    X1=-round(Re*(x-ORIGEN_X),2)
                else :
                    X1=round(Re*(ORIGEN_X-x),2)
                
                ##NEGACION DE AREA DE POSICIONAMINETO DE DADOS
                if (X1 <-10 and Y1 <13.8):
                    pass
                else:    
                    a.append([X1,Y1+8.8])
                    i=i+1
                    cv2.putText(frame,'X={}(cm), Y={}(cm)'.format(X1,Y1),(20,10+(i*20)), font, 0.5, (0,255,0), 2) #muestra la posicion x & y en centimetros
                ###############################
                    cv2.putText(frame,'{}'.format(i),(x_0+w,y_0+h), font, 0.75, (0,255,0), 2) #muestra la posicion x & y en centimetros
                    cv2.rectangle(frame, (x_0,y_0),(x_0+w,y_0+h), (255,0,0), 3)
                    cv2.circle(frame,(x,y),2,(0,0,255),3)#muestra el centro de el dado
                #Mostramos en una ventana la imagne de frame
        if cv2.waitKey(1) & 0xFF == ord('e'):                       #Utilizamos una condicional para indicar que el proceso se acabe con la letra 'e'
            break                                                   #Indicamos que se salga de la estructura while

    ##############################
    #CONVERSION DE IMAGEN A PYGAME        
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #CAMBIO DE ESTANDARES DE COLORES
    frame = frame.swapaxes(0,1)                    #ROTACION DE IMAGEN
    frame = pygame.surfarray.make_surface(frame)   #CREACION DE LA IMAGEN EN PYGAME
    screen.blit(frame, (0,0))                      #COLOCO LA IMAGEN PYGAME
    Window0()                                      #DIBUJO LOS BOTONES Y TEXTOS
    pygame.display.update()                        #ACTUALIZO LA VENTANA

    ###############################################
    #                                             #
    #       EVENTOS DE LOS BOTONES DE PYGAME      #
    #                                             #
    ###############################################                                                               
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:   #BOTON SALIR           
            captura.release()           #Indicamos la finalizacion de la captura
            cv2.destroyAllWindows()     #Cerramos ventanas de opencv
            GPIO.cleanup()              #LIMPIAMOS GPIO
            pygame.quit()               #SALIMOS DE PYGAME
            quit()                      #CERRAMOS INSTANCIA DE PYTHON
            ####################################
            #                                  #
            #      PRESIONO UN BOTON           #
            #                                  #
            ####################################
        if event.type == pygame.MOUSEBUTTONDOWN:
            ###############################################
            #                                             #
            #           SELECCION DE HOMMIG               #
            #                                             #
            ###############################################
            if ButtonHome.isOver(pos):
                angulos_actuales = MOVE_HOME(angulos_actuales)
                print('REGRESAR A HOME EL BRAZO')
            ###############################################
            #                                             #
            #           SELECCION DE DADO 1               #
            #                                             #
            ###############################################    
            if caja1Button.isOver(pos):
                objetos=a                                               #Objetos en el plano
                grados = invKinematic(objetos[0][0],objetos[0][1],6.5)  #Cinematica Inversa
                angulos_actuales = MOV_BASE(grados[0],angulos_actuales) #MOVIMIENTO DE BASE
                Garra_Open(60)               #APERTURA DE GARRA
                envio = grados[1]-60         #AJUSTE DE TRAYECTORIA
                angulos_actuales = trayectoria(60,grados[2],angulos_actuales) #Trayectoria de movimiento
                angulos_actuales = MOV_LINKS(angulos_actuales[1]+envio+6,angulos_actuales[2],angulos_actuales)
                Garra_Close(180)             #CIERRE DE GARRA
                print('DADO 1')              #cmd, DADO 1
                angulos_actuales = trayectoria_inv(50,35,angulos_actuales)  #TRAYECTORIA LEVANTAR DADO
                descarga = invKinematic(-12.5,11.3,6.5 + (1.5*CONT_DADO))   #Cinematica para descarga
                angulos_actuales = MOV_BASE(descarga[0],angulos_actuales)   #MOVIMIENTO DE BASE
                #angulos_actuales = trayectoria(descarga[1],descarga[2],angulos_actuales)
                angulos_actuales = trayectoria(55,70,angulos_actuales)      #TRAYECORIA DESCARGA
                Garra_Open(120)             #APERTURA GARRA
                ##################
                #Retorna al centro
                angulos_actuales = trayectoria_inv(50,35,angulos_actuales)
                angulos_actuales = MOV_BASE(90,angulos_actuales)
                CONT_DADO = CONT_DADO + 1
            ###############################################
            #                                             #
            #           SELECCION DE DADO 2               #
            #                                             #
            ###############################################
            if caja2Button.isOver(pos):
                objetos=a                                               #Objetos en el plano
                grados = invKinematic(objetos[1][0],objetos[1][1],6.5)  #Cinematica Inversa
                angulos_actuales = MOV_BASE(grados[0],angulos_actuales) #MOVIMIENTO DE BASE
                Garra_Open(60)               #APERTURA DE GARRA
                envio = grados[1]-60         #AJUSTE DE TRAYECTORIA
                angulos_actuales = trayectoria(60,grados[2],angulos_actuales) #Trayectoria de movimiento
                angulos_actuales = MOV_LINKS(angulos_actuales[1]+envio+6,angulos_actuales[2],angulos_actuales)
                Garra_Close(180)             #CIERRE DE GARRA
                print('DADO 2')              #cmd, DADO 1
                angulos_actuales = trayectoria_inv(50,35,angulos_actuales)  #TRAYECTORIA LEVANTAR DADO
                descarga = invKinematic(-12.5,11.3,6.5 + (1.5*CONT_DADO))   #Cinematica para descarga
                angulos_actuales = MOV_BASE(descarga[0],angulos_actuales)   #MOVIMIENTO DE BASE
                #angulos_actuales = trayectoria(descarga[1],descarga[2],angulos_actuales)
                angulos_actuales = trayectoria(55,70,angulos_actuales)      #TRAYECORIA DESCARGA
                Garra_Open(120)             #APERTURA GARRA
                ##################
                #Retorna al centro
                angulos_actuales = trayectoria_inv(50,35,angulos_actuales)
                angulos_actuales = MOV_BASE(90,angulos_actuales)
                CONT_DADO = CONT_DADO + 1
            ###############################################
            #                                             #
            #           SELECCION DE DADO 3               #
            #                                             #
            ###############################################
            if caja3Button.isOver(pos):
                objetos=a                                               #Objetos en el plano
                grados = invKinematic(objetos[2][0],objetos[2][1],6.5)  #Cinematica Inversa
                angulos_actuales = MOV_BASE(grados[0],angulos_actuales) #MOVIMIENTO DE BASE
                Garra_Open(60)               #APERTURA DE GARRA
                envio = grados[1]-60         #AJUSTE DE TRAYECTORIA
                angulos_actuales = trayectoria(60,grados[2],angulos_actuales) #Trayectoria de movimiento
                angulos_actuales = MOV_LINKS(angulos_actuales[1]+envio+6,angulos_actuales[2],angulos_actuales)
                Garra_Close(180)             #CIERRE DE GARRA
                print('DADO 3')              #cmd, DADO 1
                angulos_actuales = trayectoria_inv(50,35,angulos_actuales)  #TRAYECTORIA LEVANTAR DADO
                descarga = invKinematic(-12.5,11.3,6.5 + (1.5*CONT_DADO))   #Cinematica para descarga
                angulos_actuales = MOV_BASE(descarga[0],angulos_actuales)   #MOVIMIENTO DE BASE
                #angulos_actuales = trayectoria(descarga[1],descarga[2],angulos_actuales)
                angulos_actuales = trayectoria(55,70,angulos_actuales)      #TRAYECORIA DESCARGA
                Garra_Open(120)             #APERTURA GARRA
                ##################
                #Retorna al centro
                angulos_actuales = trayectoria_inv(50,35,angulos_actuales)
                angulos_actuales = MOV_BASE(90,angulos_actuales)
                CONT_DADO = CONT_DADO + 1

        #####################################
        #                                   #
        #   EVENTOS CAMBIO COLOR,BOTONES    #
        #                                   #
        #####################################
        if event.type == pygame.MOUSEMOTION:
            if ButtonHome.isOver(pos):
                ButtonHome.color = (0,180,250)
            else:
                ButtonHome.color = (0,0,0)   
            if caja1Button.isOver(pos):
                caja1Button.color = (0,180,250)
            else:
                caja1Button.color = (255,255,255)

            if caja2Button.isOver(pos):
                caja2Button.color = (0,180,250)
            else:
                caja2Button.color = (255,255,255)

            if caja3Button.isOver(pos):
                caja3Button.color = (0,180,250)
            else:
                caja3Button.color = (255,255,255)


