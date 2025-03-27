import socket

cliente_socket = socket.socket()  # Crea el socket
cliente_socket.connect(("localhost", 8000))  # Conecta al servidor

while True:
    numero = int(input("Ingresa un número (o -1 para salir): "))

    if numero == -1:  # Permitir salida manual
        break

    cliente_socket.sendall(str(numero).encode())  # Enviar número al servidor
    respuesta = cliente_socket.recv(4096).decode()  # Recibir respuesta del servidor

    print("Respuesta del servidor:", respuesta)  # Imprimir la respuesta sin afectar el flujo

    if respuesta == "Se han recibido 30 números, la conexión se cerrará.":
        break

cliente_socket.close()
