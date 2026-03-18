import pyautogui
import time

cantidadRepeticiones = 40
tiempoEsperaClick = 10
tiempoEsperaSorteo = 60 * 2.5

def esperar(tiempo):
    time.sleep(tiempo)

def clickear(posX,posY):
    pyautogui.click(x = posX, y = posY)
    esperar(tiempoEsperaClick)

for i in range(cantidadRepeticiones):
    clickear(280,100) #Click en barra de marcadores
    clickear(1100,645) #Click en sorteo
    clickear(1150,500) #Click entrar al sorteo
    print("Ciclo ", (i+1), " de ", cantidadRepeticiones)
    esperar(tiempoEsperaSorteo) #Espera el tiempo restante
exit()