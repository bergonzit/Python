import pyautogui
import time
import random
import cv2
import numpy as np
import mss
import matplotlib.pyplot as plt

LINK_BASE = "https://rewards.bing.com/"
LINK_ESTADO = 0
TIEMPO_CICLO = 10
TIEMPO_CLICK = 2
VX,VY = (1919,1029)
BARRA = 0.0625
VENTANAS = 4
PANTALLAS = 2
REPETICIONES = 40

busquedas = [
    "python arrays",
    "python listas",
    "python variables",
    "python constantes",
    "python documentacion",
    "python",
    "python input",
    "python print",
    "python pilas",
    "python colas",
    "python mouse",
    "python herencia",
    "wollok arrays",
    "wollok listas",
    "wollok variables",
    "wollok constantes",
    "wollok documentacion",
    "wollok",
    "wollok input",
    "wollok print",
    "wollok pilas",
    "wollok colas",
    "wollok mouse",
    "wollok herencia",
    "prolog arrays",
    "prolog listas",
    "prolog variables",
    "prolog constantes",
    "prolog documentacion",
    "prolog",
    "prolog input",
    "prolog print",
    "prolog pilas",
    "prolog colas",
    "prolog mouse",
    "prolog herencia",
    "haskell arrays",
    "haskell listas",
    "haskell variables",
    "haskell constantes",
    "haskell documentacion",
    "haskell",
    "haskell input",
    "haskell print",
    "haskell pilas",
    "haskell colas",
    "haskell mouse",
    "haskell herencia",
    "bergonzi es un tipo crack",
    "bergonzi es un tipo muy crack",
    "como conquistar a la wacha de mi amigo",
    "top skins zilean",
    "estatura enano promedio",
    "es ser negro y ser boliviano lo mismo?",
    "tutorial de como ser admin de discord",
    "como usar joystick con los pies",
    "policia marítima",
    "silla de ruedas a pedales",
    "roblox",
    "steam",
    "fallout",
    "luau",
    "stardew valley",
    "wikipedia",
    "tabla de derivacion",
    "salame y queso",
    "receta tortilla",
    "pantuflas",
    "fideos con tuco",
    "barrilete",
    "mercado libre"
]

def click(x,y):
    time.sleep(TIEMPO_CLICK/2)
    pyautogui.click(x,y)
    time.sleep(TIEMPO_CLICK/2)

def scroll(dist):
    pyautogui.scroll(-dist)

def buscar(x,y,busqueda):
    click(x,y)
    pyautogui.press('backspace')
    pyautogui.write(busqueda)
    pyautogui.press('enter')


def busquedasPantallas():
    for h in range(REPETICIONES):
        busqueda = busquedas.pop(random.randint(0,len(busquedas) - 1))
        for j in range(PANTALLAS):
            for i in range(VENTANAS):
                multx = i % 2
                multy = 1 if i >= 2 else 0
                buscar(VX * BARRA + multx * VX/2 + (j-1) * VX,VY * BARRA + multy * VY/2,busqueda)
        time.sleep(TIEMPO_CICLO)

def test():
    cerrarx = VX * 0.263
    cerrary = VY * 0.02
    multx = 0 % 2
    multy = 1 if 0 >= 2 else 0
    j = 0
    region = {
        "top": 0,
        "left": -VX,
        "width": round(VX/2),
        "height": round(VY/2)
    }
    #click(cerrarx + multx * VX/2 + (j-1) * VX,cerrary + multy * VY/2)
    #click(cerrarx + multx * VX/2 + (j-1) * VX,6 * cerrary + multy * VY/2)
    #scroll(500)
    #Buscar sobre cv2.imread
    # screenshot

    img = np.array(mss.mss().grab(region))

    # convertir a escala de grises
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # cargar imagen plantilla
    template = cv2.imread("mas.png", 0)

    # template matching
    result = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

    # encontrar mejor coincidencia
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    print(max_val)
    pyautogui.moveTo(-VX+max_loc[0],max_loc[1])

def realizarBusqueda(pos,multx,multy,pantalla):
    cerrarx = VX * 0.265
    cerrary = VY * 0.025
    pyautogui.click(pos[0] + multx * VX/2 + (pantalla-1) * VX, pos[1] + multy * VY/2 + 20)
    click(cerrarx + multx * VX/2 + (pantalla-1) * VX,cerrary + multy * VY/2)
    click(VX * 0.01 + multx * VX/2 + (pantalla-1) * VX,VY * 0.35 + multy * VY/2)

def busquedaImagen1(imagen,region):
    img = np.array(mss.mss().grab(region))
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resultado = cv2.matchTemplate(img_gray, imagen, cv2.TM_CCOEFF_NORMED)
    return cv2.minMaxLoc(resultado)

def busquedaImagen(imagen,region):
    img = np.array(mss.mss().grab(region))
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resultado = cv2.matchTemplate(img_gray, imagen, cv2.TM_CCOEFF_NORMED)
    heatmap = cv2.normalize(resultado, None, 0, 255, cv2.NORM_MINMAX)
    heatmap = np.uint8(heatmap)
    threshold = 0.98
    locations = np.where(resultado >= threshold)
    matches = []
    for y, x in zip(locations[0], locations[1]):
        similarity = resultado[y, x]
        matches.append((x, y, similarity))
    filtered = []
    min_dist = 20
    for x, y, sim in matches:
        keep = True
        for fx, fy, _ in filtered:
            dist = np.sqrt((x - fx)**2 + (y - fy)**2)

            if dist < min_dist:
                keep = False
                break
        if keep:
            filtered.append((x, y, sim))

    return filtered

def ciclarBusqueda(mas,fin,region,multx,multy,pantalla):
    scroll(500)
    time.sleep(2)
    ##_, valorMas, _, posMas = busquedaImagen(mas,region)
    #while valorMas >= 0.998:
    #    realizarBusqueda(posMas,multx,multy,pantalla)
    #    _, valorMas, _, posMas = busquedaImagen(mas,region)
    #    print(valorMas)
    #_, valorFin, _, _ = busquedaImagen(fin,region)
    #if valorFin <= 0.998:
    #    ciclarBusqueda(mas,fin,region,multx,multy,pantalla)
    posiciones = busquedaImagen(mas,region)
    for x, y, sim in posiciones:
        realizarBusqueda((x,y+20),multx,multy,pantalla)
    _, valorFin, _, _ = busquedaImagen1(fin,region)
    if valorFin <= 0.98:
        ciclarBusqueda(mas,fin,region,multx,multy,pantalla)

def busquedasDiarias():
    mas = cv2.imread("mas.png", 0)
    fin = cv2.imread("ayuda.png", 0)
    for j in range(PANTALLAS):
            for i in range(VENTANAS):
                #Valores de la pantalla
                multx = i % 2
                multy = 1 if i >= 2 else 0
                region = {
                    "top": round(VY/2 * multy),
                    "left": round(VX * (j-1) + VX/2 * multx),
                    "width": round(VX/2),
                    "height": round(VY/2)
                }
                #Primera posicion: Conjunto diario
                buscar(VX * BARRA + multx * VX/2 + (j-1) * VX,VY * BARRA + multy * VY/2,LINK_BASE)
                click(VX * 0.01 + multx * VX/2 + (j-1) * VX,VY * 0.35 + multy * VY/2)
                ciclarBusqueda(mas,fin,region,multx,multy,j)


time.sleep(5)
busquedasDiarias()
busquedasPantallas()

#test()