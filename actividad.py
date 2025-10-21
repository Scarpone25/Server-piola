import time
import sys
#Usar el siguiente código en la terminal del codespace para ejecutarlo:
#python3 keep_alive.py

def actividad(intervalo=600):
    while True:
        print("Manteniendo actividad en el server xd")  # Imprime algo en la terminal
        sys.stdout.flush()  # Asegura que el mensaje se imprima de inmediato en la terminal
        time.sleep(interval)  # Espera el intervalo especificado (en segundos)

if __name__ == "__main__":
    actividad(intervalo=600)
