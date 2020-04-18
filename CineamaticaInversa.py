import numpy as np
import math
import DH as DH_VALUE
import Funciones as Func
DH = np.empty((4,4))
############ LLENADO DE TABLA DH##########
DH[0][0]=DH_VALUE.A1;DH[0][1]=DH_VALUE.alpha1;DH[0][2]=DH_VALUE.d1;DH[0][3]=DH_VALUE.theta1;
DH[1][0]=DH_VALUE.A2;DH[1][1]=DH_VALUE.alpha2;DH[1][2]=DH_VALUE.d2;DH[1][3]=DH_VALUE.theta2;
DH[2][0]=DH_VALUE.A3;DH[2][1]=DH_VALUE.alpha3;DH[2][2]=DH_VALUE.d3;DH[2][3]=DH_VALUE.theta3;
DH[3][0]=DH_VALUE.A4;DH[3][1]=DH_VALUE.alpha4;DH[3][2]=DH_VALUE.d4;DH[3][3]=DH_VALUE.theta4;
##########################################

print(DH)