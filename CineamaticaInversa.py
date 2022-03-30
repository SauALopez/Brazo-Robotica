import numpy as np
import math
from ConstantesRRR import *

def invKinematic(Xc,Yc,Zc):
    #DEFINE POSICION
    Xc = (Xc-1)/100
    Yc = (Yc-2)/100
    Zc = Zc/100
    #################
    r = Xc**2+Yc**2+(Zc-d1)**2
    theta1 = math.degrees(np.arctan2(Yc,Xc))
    beta = np.arctan2((Zc-d1),(math.sqrt(Xc**2+Yc**2)))
    alfa = np.arccos((a2**2+r**2-a3**2)/(2*a2*r))
    THETA= np.arccos((a2**2+a3**2-r**2)/(2*a2*a3))
    theta2= -beta+alfa
    theta3 = math.pi - THETA - theta2
    #Arreglo espejo, rotacion de pi.
    A = [theta1,180-math.degrees(theta2),math.degrees(theta3)]
    return A