import numpy as np
import math
import Funciones as Func
from ConstantesRRR import *


#DEFINE POSITION
Xc = 20.5/100
Yc = 10.5/100
Zc = 11/100
#########(########
r = Xc**2+Yc**2+(Zc-d1)**2
theta1 = math.degrees(np.arctan2(Yc,Xc))
beta = np.arctan2((Zc-d1),(math.sqrt(Xc**2+Yc**2)))
alfa = np.arccos((a2**2+r**2-a3**2)/(2*a2*r))
THETA= np.arccos((a2**2+a3**2-r**2)/(2*a2*a3))
theta2= beta+alfa
theta3 = math.pi - THETA - theta2
#Theta3a = math.degrees(np.arctan2(math.sqrt(1-D**2),D))
#Theta3b = math.degrees(np.arctan2(-math.sqrt(1-D**2),D))
#Theta2a = math.degrees(np.arctan2((Zc-C.d1),(math.sqrt(Xc**2+Yc**2)))-np.arctan2(C.a3*math.sin(Theta3a),C.a2+C.a3*math.cos(Theta3a)))
#Theta2b = math.degrees(np.arctan2((Zc-C.d1),(math.sqrt(Xc**2+Yc**2)))-np.arctan2(C.a3*math.sin(Theta3b),C.a2+C.a3*math.cos(Theta3b)))
#Theta2= (np.arcsin(a3*))+
#A= [[Theta1,Theta2a,Theta3a],[Theta1,Theta2b,Theta3b]]
print(r)
print(theta1)
print(beta)
print(alfa)
print(THETA)
print(math.degrees(theta2))
print(math.degrees(theta3))