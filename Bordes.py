import cv2                                                          #Importamos la libreria cv2
import numpy as np                                                  #Importamos la libreria numpy y le colocamos un alias


captura = cv2.VideoCapture(0)                                       #Definimos una variable para nuestra captura y la incializamos
captura.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
captura.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
captura.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
AzulBajo1 = np.array([0,0,0],np.uint8)                         #Definimos el color a detectar por medio de intervalos 
AzulAlto1 = np.array([0,0,255],np.uint8)                        #definidos para el HSV, un numero bajo y otro alto, estos
ORIGEN_X = 593
ORIGEN_Y = 18
while True:                                                        #Creamos un ciclo para la captura de imagen constante
    ret,frame = captura.read()                                      #Leemos los datos de la captura y obtenemos los argumentos
    ########################
    cv2.line(frame,(ORIGEN_X,ORIGEN_Y-50),(ORIGEN_X,ORIGEN_Y+50),(0,255,0),1)
    cv2.line(frame,(ORIGEN_X-50,ORIGEN_Y),(ORIGEN_X+50,ORIGEN_Y),(0,255,0),1)
    ##################
    a=[]
    i=0
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
                Re=0.056947
                Re2=0.054744
            ############Y1 & X1 son la posicion en centimetros vertical y horizontal respectivamente###############
                if y>=ORIGEN_Y:
                    Y1=round(Re2*(y-ORIGEN_Y),2)
                else :
                    Y1=-round(Re2*(ORIGEN_Y-y),2)
                    
                if x<=ORIGEN_X:
                    X1=-round(Re*(ORIGEN_X-x),2)
                else :
                    X1=round(Re*(x-ORIGEN_X),2)
                a.append([X1,Y1])
                i=i+1    
                cv2.putText(frame,'X={}(cm), Y={}(cm)'.format(X1,Y1),(100,100+(i*50)), font, 0.75, (0,255,0), 2) #muestra la posicion x & y en centimetros
            ################################
                cv2.putText(frame,'{}'.format(i),(x_0+w,y_0+h), font, 0.75, (0,255,0), 2) #muestra la posicion x & y en centimetros
                cv2.rectangle(frame, (x_0,y_0),(x_0+w,y_0+h), (255,0,0), 3)
                cv2.circle(frame,(x,y),2,(0,0,255),3)#muestra el centro de el dado
                #cv2.putText(frame, 'X={},Y={},x={},y={}'.format(x_0 , y_0-w , x_0+w ,y_0),(x_0-10,y_0-10), font, 0.75, (0,255,0), 2, cv2.LINE_AA)  
        cv2.imshow('Imagen',frame)    
        #sleep(0.06)                              #Mostramos en una ventana la imagne de frame
        if cv2.waitKey(1) & 0xFF == ord('e'):                       #Utilizamos una condicional para indicar que el proceso se acabe con la letra 'e'
            break                                                   #Indicamos que se salga de la estructura while
captura.release()                                                   #Indicamos la finalizacion de la captura
cv2.destroyAllWindows()  

