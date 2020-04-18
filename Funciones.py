import math
import numpy as np

def Tx(value):
    TX = np.identity(4)
    TX [0][3] = value
    return Tx

def Ty(value):
    TY = np.identity(4)
    TY [1][3] = value
    return TY

def Tz(value):
    TZ = np.identity(4)
    TZ [2][3] = value
    return TZ

def Rx(thetai):
    thetai = math.radians(thetai)
    RX = np.array([[1,0,0,0],
        [0,math.cos(thetai),-math.sin(thetai),0],
        [0, math.sin(thetai), math.cos(thetai),0],
        [0,0,0,1]])
    return RX

def Ry(thetai):
    thetai = math.radians(thetai)
    RY = np.array([[math.cos(thetai),0,math.sin(thetai),0],
    [0,1,0,0],
    [-math.sin(thetai), 0, math.cos(thetai),0],
    [0,0,0,1]])
    return RY

def Rz(thetai):
    thetai = math.radians(thetai)
    RZ = np.array([[math.cos(thetai),-math.sin(thetai),0,0],
    [math.sin(thetai),math.cos(thetai),0,0],
    [0, 0, 1,0],
    [0,0,0,1]])
    return RZ