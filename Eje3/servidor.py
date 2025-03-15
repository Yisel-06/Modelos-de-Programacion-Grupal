import socket
import random

host = "127.0.0.1"
port = 8000

# Crear el socket del servidor
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mi_socket.bind((host, port))
mi_socket.listen()

print(f"Servidor escucha en {host}:{port}")

cliente_socket, addr = mi_socket.accept()
print(f"Conexión establecida desde {addr}")

def generar_numero_servidor():
    return random.randint(1, 10) 

while True:
    mensaje = cliente_socket.recv(1024).decode()
    
    if mensaje.lower() == "fin":
        print("El cliente ha terminado el juego.")
        break
    
    else:
        numerocliente = int(mensaje)
        
        numeroservidor = generar_numero_servidor()
        
        print(f"Cliente envió: {numerocliente}")
        print(f"Servidor generó: {numeroservidor}")
    
        if numerocliente == numeroservidor:
            print(f"¡Coincidencia! Ambos eligieron: {numerocliente}")
        else:
            print(f"No coinciden. Servidor: {numeroservidor}, Cliente: {numerocliente}")


cliente_socket.close()
mi_socket.close()
print("Conexión cerrada.")
     



