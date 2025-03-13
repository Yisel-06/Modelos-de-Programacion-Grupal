import socket  # Importar librería

host = "127.0.0.1"
port = 8000

# Crear el socket
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect((host, port))  # Conectar al servidor

print("Hola desde el cliente")

while True:
    mensaje = input("Ingrese un valor: ")
    cliente_socket.sendall(mensaje.encode())
