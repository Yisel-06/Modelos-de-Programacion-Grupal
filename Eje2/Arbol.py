##Arbol binario de búsqueda

class Nodo:
    def __init__(self, valor): ## Inicialización de los nodos
        self.valor = valor
        self.izquierda = None  
        self.derecha = None

class Arbol:
    def __init__(self, raiz): ## Inicialización de la raiz del arbol
        self.raiz = Nodo(raiz)

    def insert(self, valor):
        self.insert_recursive(self.raiz, valor) ## Envía la raiz y el valor que capturamos desde el teclado
    
    def insert_recursive(self, nodo, valor): ## Inserta los valores a la izquierda o a la derecha de los nodos según su valor 
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

        else:
            print("El valor no existe")

    def search(self, valor):
        return self.search_recursive(self.raiz, valor) ## Envía la raiz y el valor que capturamos desde el teclado

    def search_recursive(self, nodo, valor): ## La raiz la recibe en nodo
        if nodo is None:
            return False
        
        if nodo == nodo.valor:
            return True
        
        if valor < nodo.valor:
            return self.search_recursive(nodo.izquierda, valor)
        
##Captura de datos desde el teclado
raiz = int(input("Ingresa el valor de la raiz: "))
arbol = Arbol(raiz)

while True:
    num = int(input("Ingresa un número si deseas continuar, de lo contrario ingresa '0' para finalizar el ciclo: "))

    if num == 0:
        break
    arbol.insert(num)

busqueda = int(input("Ingresa el valor a buscar: "))

if arbol.search(busqueda):
    print(f"El valor {busqueda} se encuentra en el arbol")
    
else:
    print(f"El valor {busqueda} no se encuentra en el arbol")



                        