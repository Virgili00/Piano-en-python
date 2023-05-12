
import numpy as np
import sounddevice as sd
import threading
import sys
def sonido (frequency,duracion,presion):
    framerate = 44100
    tiempo = np.linspace(0,duracion/100,int(framerate*duracion/1000))
    data = np.sin(2*np.pi * frequency*tiempo)
   #si la tecla se esta apretando reproduce sonido, si no se esta apretando 
    if presion==1:
        sd.play(data,framerate)
        
    else: 
       
        sd.stop()
        

def reproducirDO(presion):
    sonido(65,2200,presion)
def reproducirre(presion):
    sonido(73,2200,presion)
def reproducirmi(presion):
    sonido(82,2200,presion)
def reproducirfa(presion):
    sonido(87,2200,presion)
def reproducirsol(presion):
    sonido(97,2200,presion)
def reproducirla(presion):
    sonido(110,2200,presion)
def reproducirsi(presion):
    sonido(123,2200,presion)
def reproducirdo2(presion):
    sonido(130,2200,presion)
#no reproducir sonido

