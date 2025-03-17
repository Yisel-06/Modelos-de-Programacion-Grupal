import socket
import random

host = "127.0.0.1"
port = 8000

# Crear el socket del servidor
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_socket.bind((host, port))
servidor_socket.listen()

print(f"Servidor escucha en {host}:{port}")

cliente_socket, addr = servidor_socket.accept()
print(f"Conexión establecida desde {addr}")
print('__________________________________')

def generar_numero_servidor():
    return random.randint(1, 10) 

# Instancia de variables para contabilizar aciertos y desaciertos y la lista de los numeros que se han ido generando
victorias = 0
derrotas = 0
derrotas_consecutivas = 0
numeros_servidor = []

while True:
    mensaje = cliente_socket.recv(1024).decode()
    
    if len(numeros_servidor) == 10:
        numeros_servidor = []
        print("->    ¡El juego se reinició, buena suerte! :D    <-")
        print('__________________________________')

    if mensaje.lower() == "terminar":
        print("El cliente ha terminado el juego :v")
        break
    
    else:
        numerocliente = int(mensaje)
        
        numeroservidor = generar_numero_servidor()

        # Verifica que el número generado no se repita con números anteriormente generados
        if len(numeros_servidor) > 0:
            while numeroservidor in numeros_servidor:
                numeroservidor = generar_numero_servidor()
        
        print(f"- El servidor eligió el número: {numeroservidor}")
        numeros_servidor.append(numeroservidor)
    
        if numerocliente == numeroservidor:
            print(f"¡Coincidencia :D! Ambos eligieron el número '{numerocliente}'")
            print('__________________________________')

            victorias += 1
            derrotas_consecutivas = 0    
            
        else:
            print(f"Los números no coinciden :c")
            print(f"El cliente eligió el número '{numerocliente}' y el servidor eligió el número '{numeroservidor}'")
            print('__________________________________')
            derrotas += 1
            derrotas_consecutivas += 1
        
        # Si el servidor detecta que hay 3 derrotas consecutivas, termina el juego
        if derrotas_consecutivas == 3:
            print('->    Tienes 3 derrotas consecutivas. Perdiste :c    <-')
            print('__________________________________')
            derrotas_consecutivas = 0

cliente_socket.close()
servidor_socket.close()

print('Resultados:')
print('- Cantidad de aciertos durante la partida:', victorias)
print('- Cantidad de desaciertos durante la partida:', derrotas)

print("Conexión cerrada.")
     