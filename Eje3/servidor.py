import socket  # Librería
host = "127.0.0.1" #Deben correr en el mismo host y puerto
port =8000 #Este puerto corresponde al servidor el del cliente se asigna dinamico


#AF_INET Tipo de direcciones a los que se conecta el servidor
#SOCK_STREAM Tipo de socket- stream: intercambio y flujo de datos

# Crear el socket
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mi_socket.bind((host, port))
mi_socket.listen()

print("Servidor escucha en {}:{}".format(host, port))

cliente_socket, addr = mi_socket.accept()
print("Conexionestablecida desde",addr)

while True:
     mensaje = cliente_socket.recv(1024).decode()
     print(f"recibe: {mensaje}")
     if mensaje.lower() == "fin":
         break
     
cliente_socket.close()
mi_socket.close()
     
     



