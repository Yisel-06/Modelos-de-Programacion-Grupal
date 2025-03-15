import socket  # Importar librería
import random
import threading
import time
host = "127.0.0.1"
port = 8000

ejecutando = True

# Crear el socket
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect((host, port))  # Conectar al servidor

print("Hola desde el cliente")


def generar_numAl():
    global ejecutando 
    while ejecutando:
        numero = random.randrange(1, 10)  
        print(f"Cliente generó: {numero}")
        cliente_socket.sendall(str(numero).encode())
        time.sleep(90) #genera cada x seg

hilo = threading.Thread(target=generar_numAl)
hilo.start()

while True:
    mensaje = input("Escibe fin si desea terminar el juego ")
    if mensaje.lower() == 'fin':
        ejecutando= False
        cliente_socket.sendall(mensaje.encode())

        break

cliente_socket.close()