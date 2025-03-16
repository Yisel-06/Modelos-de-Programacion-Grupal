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

#Instancia de variables para contabilizar aciertos y desaciertos
victorias = 0
derrotas = 0
derrotas_consecutivas = 0

while True:
    mensaje = cliente_socket.recv(1024).decode()
    
    if mensaje.lower() == "terminar":
        print("El cliente ha terminado el juego.")
        break
    
    else:
        numerocliente = int(mensaje)
        
        numeroservidor = generar_numero_servidor()
        
        print(f"Cliente envió: {numerocliente}")
        print(f"Servidor generó: {numeroservidor}")
    
        if numerocliente == numeroservidor:
            print(f"¡Coincidencia! Ambos eligieron: {numerocliente}")
            victorias += 1
            derrotas_consecutivas = 0    
            
        else:
            print(f"No coinciden. Servidor: {numeroservidor}, Cliente: {numerocliente}")
            derrotas += 1
            derrotas_consecutivas += 1
            
        if derrotas_consecutivas >= 3:
            print('Tienes 3 derrotas consecutivas perdiste xd')
            mi_socket.sendall(derrotas_consecutivas.encode())
            break

cliente_socket.close()
mi_socket.close()
print('Cantidad de aciertos durante la partida: ', victorias)
print('Cantidad de desaciertos durante la partida: ', derrotas)

print("Conexión cerrada.")
     



