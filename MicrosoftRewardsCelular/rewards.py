import subprocess
import shlex
import time
import sys
import cv2
import numpy as np

#Requiere adb start-server
def run_adb(cmd):
    """Ejecuta un comando adb (string) y devuelve (exitcode, stdout, stderr)."""
    full_cmd = f"adb {cmd}"
    proc = subprocess.run(shlex.split(full_cmd), capture_output=True, text=True)
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()

def get_screen_size():
    code, out, err = run_adb("shell wm size")
    if code != 0:
        raise RuntimeError(f"Error getting screen size: {err}")
    # out: "Physical size: 1080x2340"
    parts = out.split()[-1].split('x')
    width = int(parts[0]); height = int(parts[1])
    return width, height

def tap(x, y):
    return run_adb(f"shell input tap {x} {y}")

def swipe(x1, y1, x2, y2, duration_ms):
    return run_adb(f"shell input swipe {x1} {y1} {x2} {y2} {duration_ms}")

def scroll():
    swipe(viewport[0] * 0.5,viewport[1] * 0.75,viewport[0] * 0.5,viewport[1] * 0.25,300)

def adb_screencap(filename="screen.png"):
    result = subprocess.run(["adb", "exec-out", "screencap", "-p"], stdout=subprocess.PIPE)
    with open(filename, "wb") as f:
        f.write(result.stdout)

def find_image_on_screen(screen_path, template_path, threshold=0.85):
    screen = cv2.imread(screen_path)
    template = cv2.imread(template_path)

    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        x, y = max_loc
        h, w = template.shape[:2]
        return x + w // 2, y + h // 2
    else:
        return None

def save_heatmap(screen_path, template_path, output_path="heatmap.png"):
    screen = cv2.imread(screen_path)
    template = cv2.imread(template_path)

    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)

    # Normalizar valores entre 0 y 255
    heatmap = cv2.normalize(result, None, 0, 255, cv2.NORM_MINMAX)
    heatmap = heatmap.astype(np.uint8)

    # Aplicar mapa de color tipo Heatmap
    heatmap_color = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)

    # Guardar imagen
    cv2.imwrite(output_path, heatmap_color)
    print("Heatmap guardado como:", output_path)

cantRepeticiones = 20
tiempoEspera = 8
viewport = get_screen_size()
#Accede al rewards
time.sleep(tiempoEspera)
tap(viewport[0] * 0.2,viewport[1] * 0.7)
time.sleep(tiempoEspera*2)
scroll()
#Inicia ciclo de rewards
i = 1
while i < cantRepeticiones:
    print("Inicia ciclo " , i)
    time.sleep(tiempoEspera)
    adb_screencap("screen.png")
    pos = find_image_on_screen("screen.png", "moneda.png")
    #Reinicia la pagina
    if not pos:
        print("Resetea")
        tap(viewport[0] * 0.8,viewport[1] * 0.08)
        time.sleep(tiempoEspera)
        scroll()
        time.sleep(1)
    else :
        i += 1
        tap(pos[0], pos[1])
        time.sleep(tiempoEspera)
        tap(viewport[0] * 0.2,viewport[1] * 0.95)