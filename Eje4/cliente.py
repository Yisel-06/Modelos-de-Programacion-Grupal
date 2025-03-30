import socket

cliente_socket = socket.socket()  # Crea el socket
cliente_socket.connect(("localhost", 8000))  # Conecta al servidor

while True:
    numero = input("Ingrese el número o 'Salir' para cerrar las conexiones: ")
    print("-----------------------------------------------") 

    if numero.lower() == "salir":  # Permitir salida manual
        break
    
    # try catch para validar cuando reciba un número lo convierta entero y que 
    # si recibe un valor diferente a un numero o salir muestre el mensaje avisando
    # que no es válido
    try: 
        int(numero)
    
    except ValueError:
        print("Por favor, ingrese un número válido o 'Salir': ")
        print("-----------------------------------------------") 
        continue

    cliente_socket.sendall(str(numero).encode())  # Enviar número al servidor
    respuesta = cliente_socket.recv(4096).decode()  # Recibir respuesta del servidor

    print("Respuesta del servidor:", respuesta)  # Imprimir la respuesta sin afectar el flujo

    if respuesta == "Se han recibido 30 números, la conexión se cerrará.":
        break

cliente_socket.close()
