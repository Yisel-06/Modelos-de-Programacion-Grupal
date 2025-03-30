import socket
import time
from binarytree import Node

# Definición de las clases Nodo y Árbol
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None  
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def insert(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self.insert_recursive(self.raiz, valor)

    def insert_recursive(self, nodo, valor):
        if valor < nodo.valor:               
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self.insert_recursive(nodo.izquierda, valor)
        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self.insert_recursive(nodo.derecha, valor)

    def tree(self, nodo):
        if nodo is None:
            return None
        bt_nodo = Node(nodo.valor)
        bt_nodo.left = self.tree(nodo.izquierda)
        bt_nodo.right = self.tree(nodo.derecha)
        return bt_nodo

servidor_socket = socket.socket()
servidor_socket.bind(("localhost", 8000))
servidor_socket.listen()

conexion, direccion = servidor_socket.accept()
print("Conexión establecida con:", direccion)

arbol = Arbol()
lista = []

while True:
    data = conexion.recv(4096)

    if not data:
        break  # Si no hay datos, salir del bucle

    numero_cliente = int(data.decode())
        
    if 10 <= numero_cliente < 100:
        if numero_cliente in lista:
            respuesta = "Número repetido"
            
        else:
            lista.append(numero_cliente)
            arbol.insert(numero_cliente)
            respuesta = "Numero ingresado"
        
            bt_raiz = arbol.tree(arbol.raiz)
            print("Árbol binario:")
            print(bt_raiz)
        
            if len(lista) == 30:
                mensaje_cierre = "Se han recibido 30 números, la conexión se cerrará."
                conexion.sendall(mensaje_cierre.encode())  # Avisar antes de cerrar
                print("La conexión se ha cerrado")

                time.sleep(2)  # intervalo de tiempo para cerrar la conexión
                break 

    else:
        respuesta = "El número no tiene dos dígitos"
        print(f"Número incorrecto: {numero_cliente}")
    
    # Enviar respuesta al cliente
    conexion.sendall(respuesta.encode())
        
print("Desconectado del cliente", direccion)
servidor_socket.close()
conexion.close()