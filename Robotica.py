
from CineamaticaInversa import *
from time import sleep

cordenadas = [0,0,0]
while True:
    cordenadas[0] = float(input('Xc:'))
    cordenadas[1] = float(input('Yc:'))
    cordenadas[2] = float(input('Zc:'))
    print(cordenadas)
    grados =invKinematic(cordenadas[0],cordenadas[1],cordenadas[2])
    print(grados)

