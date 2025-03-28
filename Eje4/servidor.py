import socket
import time

servidor_socket = socket.socket()
servidor_socket.bind(("localhost", 8000))
servidor_socket.listen()

conexion, direccion = servidor_socket.accept()
print("Conexión establecida con:", direccion)

lista = []

while True:
    data = conexion.recv(4096)

    if not data:
        break  # Si no hay datos, salir del bucle

    numero_cliente = int(data.decode())

    if 10 <= numero_cliente < 100:
        lista.append(numero_cliente)
        respuesta = "Número recibido y válido"
        print(f"El cliente envió: {numero_cliente}")
    else:
        respuesta = "El número no tiene dos dígitos"
        print(f"Número incorrecto: {numero_cliente}")

    # Enviar respuesta al cliente
    conexion.sendall(respuesta.encode())

    if len(lista) == 30:
        mensaje_cierre = "Se han recibido 30 números, la conexión se cerrará."
        conexion.sendall(mensaje_cierre.encode())  # Avisar antes de cerrar
        print("La conexión se ha cerrado")

        time.sleep(2)  # intervalo de tiempo para cerrar la conexión
        break 
        
print("Desconectado del cliente", direccion)
servidor_socket.close()
conexion.close()
