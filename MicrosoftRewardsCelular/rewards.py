import subprocess
import shlex
import time
import sys
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

cantRepeticiones = 40
tiempoEspera = 6
viewport = get_screen_size()
#Accede al rewards
time.sleep(tiempoEspera)
tap(viewport[0] * 0.2,viewport[1] * 0.7)
time.sleep(tiempoEspera*2)
scroll()
#Inicia ciclo de rewards
for i in range(cantRepeticiones):
    print("Inicia ciclo " , i)
    time.sleep(tiempoEspera)
    #Reinicia la pagina
    if (i+1) % 10 == 0:
        print("Resetea")
        tap(viewport[0] * 0.8,viewport[1] * 0.08)
        time.sleep(tiempoEspera)
        scroll()
        time.sleep(1)
    tap(viewport[0] * 0.5,viewport[1] * 0.5)
    time.sleep(tiempoEspera)
    tap(viewport[0] * 0.2,viewport[1] * 0.95)
    
    