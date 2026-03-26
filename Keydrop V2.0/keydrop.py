import pyautogui
import time
import cv2
import numpy as np
import mss
import matplotlib.pyplot as plt
import sys
import os

CANTIDAD_REPETICIONES = 40
TIEMPO_CLICK = 10
TIEMPO_SORTEO = 60 * 2.5

def esperar(tiempo):
    time.sleep(tiempo)

def clickear(x,y):
    time.sleep(TIEMPO_CLICK/2)
    pyautogui.click(x,y)
    time.sleep(TIEMPO_CLICK/2)

def busquedaImagen(imagen):
    region = {
        "top": 0,
        "left": 0,
        "width": 1365,
        "height": 767
    }
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
    if filtered == []:
        filtered.append((0,0))
    return filtered

def resource_path(relative_path):
    try:
        # PyInstaller crea una carpeta temporal
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

imgUnirse = cv2.imread(resource_path("unirse.png"), 0)
imgSorteo = cv2.imread(resource_path("sorteo.png"), 0)
while True:
    clickear(280,100) #Click en barra de marcadores
    sorteos = busquedaImagen(imgUnirse)
    sorteo = max(sorteos, key=lambda p: p[0])
    clickear(sorteo[0] + 123, sorteo[1] + 17)
    sorteo = busquedaImagen(imgSorteo)[0]
    clickear(sorteo[0] + 70,sorteo[1] + 20) #Click entrar al sorteo
    print("Ciclo ", (i+1), " de ", CANTIDAD_REPETICIONES)
    esperar(TIEMPO_SORTEO) #Espera el tiempo restante
exit()