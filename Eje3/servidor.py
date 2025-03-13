import socket  # Librería
host = "127.0.0.1" #Deben correr en el mismo host y puerto
port =8000 #Este puerto corresponde al servidor el del cliente se asigna dinamico


# Crear el socket
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mi_socket.bind((host, port))
mi_socket.listen(5)

print("Servidor escucha en {}:{}".format(host, port))

cliente_socket, addr = mi_socket.accept()
print("Conexionestablecida desde",addr)


