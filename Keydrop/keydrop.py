import pyautogui
import time

cantidadRepeticiones = 40
tiempoEsperaClick = 10
tiempoEsperaSorteo = 60 * 2.5

def esperar(tiempo):
    time.sleep(tiempo)

def clickear(posX,posY):
    esperar(tiempoEsperaClick/2)
    pyautogui.click(x = posX, y = posY)
    esperar(tiempoEsperaClick/2)


cantidadRepeticiones = input("Cantidad de repeticiones: ")
desvioX = input("Desvio Sorteo X: ")
desvioY = input("Desvio Sorteo Y: ")
entrarX = input("Desvio Entrar Sorteo X: ")
entrarY = input("Desvio Entrar Sorteo Y: ")
for i in range(cantidadRepeticiones):
    clickear(280,100) #Click en barra de marcadores
    clickear(1100 + desvioX,512 + desvioY) #Click en sorteo
    clickear(1150 + entrarX,500 + entrarY) #Click entrar al sorteo
    print("Ciclo ", (i+1), " de ", cantidadRepeticiones)
    esperar(tiempoEsperaSorteo) #Espera el tiempo restante
exit()