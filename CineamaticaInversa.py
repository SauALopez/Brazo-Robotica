import numpy as np
import math
import Funciones as Func
import ConstantesRRR as C


#DEFINE POSITION
Xc = 6
Yc = 4
Zc = 10
#########(########
D = ((Xc**2)+(Yc**2)+((Zc-C.d1)**2)-(C.a3)-(C.a2))/(2*C.a2*C.a3)
print(D)
Theta1 = math.degrees(np.arctan2(Yc,Xc))
Theta3a = math.degrees(np.arctan2(math.sqrt(1-D**2),D))
Theta3b = math.degrees(np.arctan2(-math.sqrt(1-D**2),D))
Theta2a = math.degrees(np.arctan2((Zc-C.d1),(math.sqrt(Xc**2+Yc**2)))-np.arctan2(C.a3*math.sin(Theta3a),C.a2+C.a3*math.cos(Theta3a)))
Theta2b = math.degrees(np.arctan2((Zc-C.d1),(math.sqrt(Xc**2+Yc**2)))-np.arctan2(C.a3*math.sin(Theta3b),C.a2+C.a3*math.cos(Theta3b)))
A= [[Theta1,Theta2a,Theta3a],[Theta1,Theta2b,Theta3b]]
print(A)