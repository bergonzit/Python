import pyautogui
import time
import random

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

cantidadRepeticiones = 40
tiempoEspera = 10

print("Bergonzi es un tipo muy crack y le sabe a la vida")
print("\nMicrosoft Rewards:")
for i in range(cantidadRepeticiones):
    numeroRandom = random.randint(0,len(busquedas) - 1)
    time.sleep(tiempoEspera)
    pyautogui.click(x = 440, y = 55)
    pyautogui.press('backspace')
    pyautogui.write(busquedas.pop(numeroRandom))
    pyautogui.press('enter')
    print("Busquedas ", (i+1), "/", cantidadRepeticiones)
time.sleep(tiempoEspera/2)
pyautogui.click(x = 240, y = 55)
pyautogui.press('backspace')
pyautogui.write("https://store.steampowered.com/app/312530/Duck_Game/")
pyautogui.press('enter')
exit()