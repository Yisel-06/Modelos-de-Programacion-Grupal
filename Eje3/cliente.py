import socket
import random

host = "127.0.0.1"
port = 8000

ejecutando = True
numeros_cliente = []

# Crear el socket
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect((host, port))  # Conectar al servidor

print('__________________________________\n')
print('         Bienvenido al juego adivina adivinador :D          ')
print('__________________________________')


while True:
    
    if len(numeros_cliente) == 10:
        numeros_cliente = []

    mensaje = input("Presiona 'enter' si deseas iniciar el juego o 'terminar' si deseas terminar: ")
    
    if mensaje.lower() != 'terminar':
        numero = random.randint(1, 10)

        # Verifica que el número generado no se repita con números anteriormente generados
        if len(numeros_cliente) > 0:
            while numero in numeros_cliente:
                numero = random.randint(1, 10)

        print(f"- El cliente eligió el número: {numero}")
        print('__________________________________')
        numeros_cliente.append(numero)
        
        cliente_socket.sendall(str(numero).encode())
    
    else:
        cliente_socket.sendall(mensaje.encode())
        ejecutando = False
        break

cliente_socket.close()