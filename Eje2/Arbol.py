from binarytree import Node

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None  
        self.derecha = None

class Arbol:
    def __init__(self, raiz):
        self.raiz = Nodo(raiz)
        self.nodos_joined = []

    def insert(self, valor):
        self.insert_recursive(self.raiz, valor)
        self.nodos_joined.append(valor)
        
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

    # Función busqueda de nodos
    def search(self, valor):
        recorrido = []
        if self.search_recursive(self.raiz, valor, recorrido):
            print(" -> ".join(map(str, recorrido)))
            return True
        return False
    
    def search_recursive(self, nodo, valor,recorrido):
        if nodo is None:
            return False
        recorrido.append(nodo.valor)
        if valor == nodo.valor:
            return True
        if valor < nodo.valor:
            return self.search_recursive(nodo.izquierda, valor, recorrido)
        else:
            return self.search_recursive(nodo.derecha, valor, recorrido)

    def count_nodos(self):
        return self.count_nodos_recursive(self,raiz)
    
    def count_nodos_recursive(self, nodo):
        if nodo is None:
           return 0
        contador= 0
        if nodo.izquierda is not None and nodo.derecha is not None:
         contador = 1
        contador += self.count_nodos_recursive(nodo.izquierda)
        contador += self.count_nodos_recursive(nodo.derecha)
        return contador
    
    def show_nodos(self):
            nodos_children = []
            for valor in self.nodos_joined:
                nodo = self.obtain(self.raiz, valor)
                if nodo and nodo.izquierda and nodo.derecha:
                    nodos_children.append(valor)
            return nodos_children

    def obtain(self, nodo, valor):
            if nodo is None:
             return None
            if nodo.valor == valor:
                return nodo
            elif valor < nodo.valor:
                return self.obtain(nodo.izquierda, valor)
            else:
                return self.obtain(nodo.derecha, valor)
            
    # Recorrido en preorden
    def preorden(self):
        resultado = []
        self.preorden_recursivo(self.raiz, resultado)
        return resultado

    def preorden_recursivo(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.valor)  
            self.preorden_recursivo(nodo.izquierda, resultado)
            self.preorden_recursivo(nodo.derecha, resultado)
            
    def nodos_con_hijos_pares_preorden(self, nodo, resultado):
        if nodo:
       
            if (nodo.izquierda and nodo.izquierda.valor % 2 == 0) or \
            (nodo.derecha and nodo.derecha.valor % 2 == 0):
                resultado.append(nodo.valor)  
        
            self.nodos_con_hijos_pares_preorden(nodo.izquierda, resultado)
            self.nodos_con_hijos_pares_preorden(nodo.derecha, resultado)
    
    def sumas_hijos_preorden(self, nodo, resultado):
        if nodo:  
            suma = 0
            if nodo.izquierda:
                suma += nodo.izquierda.valor
            if nodo.derecha:
                suma += nodo.derecha.valor
        
            resultado.append(suma)

            self.sumas_hijos_preorden(nodo.izquierda, resultado)
            self.sumas_hijos_preorden(nodo.derecha, resultado)
                
    # Función árbol binario
    def tree(self, nodo):
        if nodo is None:
            return None
        bt_nodo = Node(nodo.valor)
        bt_nodo.left = self.tree(nodo.izquierda)
        bt_nodo.right = self.tree(nodo.derecha)
        return bt_nodo
            
    # Ingresar datos desde la consola
raiz = int(input("Ingresa el valor de la raiz: "))
arbol = Arbol(raiz)
resultado = []
nodos_pares_preorden = []

while True:
    num = int(input("Ingresa un número si deseas continuar, de lo contrario ingresa '0' para finalizar el ciclo: "))
    if num == 0:
        break
    arbol.insert(num)

    # Mostrar el árbol en consola
bt_raiz = arbol.tree(arbol.raiz)
print("\nÁrbol binario:")
print(bt_raiz)
print("--------------------------------------------------------------------------")

print("Recorrido inorden: ")
def inorden(nodo):
        if nodo is not None:
            inorden(nodo.izquierda)
            print(nodo.valor, end=" ")
            inorden(nodo.derecha)
inorden(arbol.raiz)
print("\n--------------------------------------------------------------------------")

    # Mostrar nodos con dos hijos
nodos_content =raiz,arbol.show_nodos()
print(f"Nodos ingresados con exactamente dos hijos: {nodos_content}")
print("--------------------------------------------------------------------------")

    # Mostrar nodos con hijos pares en preorden - suma de los hijos de los nodos
print("Recorrido Preorden:", arbol.preorden())
arbol.nodos_con_hijos_pares_preorden(arbol.raiz, nodos_pares_preorden)
print("--------------------------------------------------------------------------")

print("Nodos con al menos un hijo par (recorrido preorden):", nodos_pares_preorden)
arbol.sumas_hijos_preorden(arbol.raiz, resultado)
print("--------------------------------------------------------------------------")

print("Suma de sus hijos:", ", ".join(map(str, resultado)))
print("--------------------------------------------------------------------------")

    # Buscar nodos
busqueda = int(input("Ingresa el valor a buscar: "))
print("--------------------------------------------------------------------------")
if arbol.search(busqueda):
    print(f"\nEl valor {busqueda} sí se encuentra en el árbol")
else:
    print(f"El valor {busqueda} no se encuentra en el árbol")
print("--------------------------------------------------------------------------")
