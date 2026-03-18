import time
import math
import numpy as np
import random as r
import matplotlib.pyplot as plt


N, M = 31, 31
mapa = np.zeros((N,M))
exploradores = []

def iniciarLaberinto():
    #x,y = r.randint(round(N/4),round(3*N/4)),r.randint(round(M/4),round(3*M/4))
    x,y = valorInicial(N),valorInicial(M)
    print(x, "A", y)
    mapa[x][y] = 1
    agregarExploradores(x,y)

def valorInicial(max):
    valor = r.randint(1,max-2)
    valor += 1 if valor%2 == 0 else 0
    return valor

def agregarExploradores(x,y):
    colocarExplorador(x+2,y)
    colocarExplorador(x-2,y)
    colocarExplorador(x,y+2)
    colocarExplorador(x,y-2)

def colocarExplorador(x,y):
    if coordenadaValida(x,y) and mapa[x][y] == 0:
        mapa[x][y] = 0.5
        exploradores.append((x,y))

def coordenadaValida(x,y):
    return x >= 0 and x < N and y >= 0 and y < M

def mostrarMapa():
    mngr = plt.get_current_fig_manager()
    # Geometry string: "width x height + x_offset + y_offset"
    mngr.window.wm_geometry("+100+200") 
    plt.imshow(mapa, cmap='gray')   
    plt.show()

def construirLaberinto():
    while len(exploradores) != 0:
        filtrarExploradores()
        abrirCamino(exploradores.pop())
        #mostrarMapa()

def filtrarExploradores():
    r.shuffle(exploradores)

def abrirCamino(pos):
    posiblesCaminos = []
    if caminoPosible(pos[0]+2,pos[1]):
        posiblesCaminos.append((1,0))
    if caminoPosible(pos[0]-2,pos[1]):
        posiblesCaminos.append((-1,0))
    if caminoPosible(pos[0],pos[1]+2):
        posiblesCaminos.append((0,1))
    if caminoPosible(pos[0],pos[1]-2):
        posiblesCaminos.append((0,-1))
    r.shuffle(posiblesCaminos)
    camino = posiblesCaminos.pop()
    romperPared(pos,camino[0],camino[1])

def caminoPosible(x,y):
    return coordenadaValida(x,y) and mapa[x][y] == 1

def romperPared(pos,x,y):
    mapa[pos[0]][pos[1]] = 1
    agregarExploradores(pos[0],pos[1])
    mapa[pos[0]+x][pos[1]+y] = 1

iniciarLaberinto()
construirLaberinto()
mostrarMapa()
