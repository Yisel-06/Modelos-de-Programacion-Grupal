import socket
import random

host = "127.0.0.1"
port = 8000

ejecutando = True

# Crear el socket
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect((host, port))  # Conectar al servidor

print('____________________\n')

print('         Bienvenido al juego adivina adivinador           ')
print('____________________')

while True:
    
    mensaje = input("Presiona 'enter' si deseas iniciar el juego o 'terminar' si deseas terminar: ")
    
    if mensaje.lower() != 'terminar':
        numero = random.randint(1, 10)
        print(f"Cliente generó: {numero}")
        
        cliente_socket.sendall(str(numero).encode())
    
    
    else:
        cliente_socket.sendall(mensaje.encode())
        ejecutando = False
        break

cliente_socket.close()