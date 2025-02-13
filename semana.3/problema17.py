class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Agrega un elemento a la pila."""
        self.items.append(item)

    def pop(self):
        """Elimina y devuelve el elemento superior de la pila."""
        if not self.esta_vacia():
            return self.items.pop()
        return "La pila está vacía."

    def peek(self):
        """Devuelve el elemento superior de la pila sin eliminarlo."""
        if not self.esta_vacia():
            return self.items[-1]
        return "La pila está vacía."

    def esta_vacia(self):
        """Verifica si la pila está vacía."""
        return len(self.items) == 0

# Ejemplo de uso
pila = Pila()
pila.push(10)
pila.push(20)
print("Elemento superior:", pila.peek())
pila.pop()
print("Elemento superior tras pop:", pila.peek())

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, item):
        """Agrega un elemento al final de la cola."""
        self.items.append(item)

    def desencolar(self):
        """Elimina y devuelve el elemento al frente de la cola."""
        if not self.esta_vacia():
            return self.items.pop(0)
        return "La cola está vacía."

    def frente(self):
        """Devuelve el elemento al frente de la cola sin eliminarlo."""
        if not self.esta_vacia():
            return self.items[0]
        return "La cola está vacía."

    def esta_vacia(self):
        """Verifica si la cola está vacía."""
        return len(self.items) == 0

# Ejemplo de uso
cola = Cola()
cola.encolar(1)
cola.encolar(2)
print("Elemento al frente:", cola.frente())
cola.desencolar()
print("Elemento al frente tras desencolar:", cola.frente())


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_al_final(self, dato):
        """Agrega un nuevo nodo al final de la lista."""
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def mostrar_lista(self):
        """Muestra todos los elementos de la lista enlazada."""
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

# Ejemplo de uso
lista = ListaEnlazada()
lista.agregar_al_final(5)
lista.agregar_al_final(10)
lista.agregar_al_final(15)
print("Elementos de la lista enlazada:")
lista.mostrar_lista()

