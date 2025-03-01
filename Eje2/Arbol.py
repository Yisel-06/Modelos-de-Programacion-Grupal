class Nodo:
    def __init__(self, valor): ## Inicialización de los nodos
        self.valor = valor
        self.izquierda = None  
        self.derecha = None

class Arbol:
    def __init__(self, raiz): ## Inicialización de la raíz del árbol
        self.raiz = Nodo(raiz)
        self.nodos_joined = [] #lista de almacenamiento de nodos

    def insert(self, valor):
        self.insert_recursive(self.raiz, valor) ## Envía la raíz y el valor que capturamos desde el teclado
        self.nodos_joined.append(valor) # Almacena el valor ingresado
        
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
        else: self.search_recursive(nodo.derecha, valor)
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
    # recorrido en preorden
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

                
##Captura de datos desde el teclado
raiz = int(input("Ingresa el valor de la raiz: "))
arbol = Arbol(raiz)
resultado = []
nodos_pares_preorden = []


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
print("Recorrido inorden")
def inorden(nodo):
        if nodo is not None:
            inorden(nodo.izquierda)
            print(nodo.valor, end=" ")
            inorden(nodo.derecha)

inorden(arbol.raiz)

    # Mostrar nodos con dos hijos
nodos_content = arbol.show_nodos()
print(f"\nNodos ingresados con exactamente dos hijos: {nodos_content}")

    #mostrar nodos con hijos pares en preorden- suma de los hijos de los nodos
print("Recorrido Preorden:", arbol.preorden())
arbol.nodos_con_hijos_pares_preorden(arbol.raiz, nodos_pares_preorden)
print("Nodos con al menos un hijo par (recorrido preorden):", nodos_pares_preorden)
arbol.sumas_hijos_preorden(arbol.raiz, resultado)
print("Suma hijos:", ", ".join(map(str, resultado)))
