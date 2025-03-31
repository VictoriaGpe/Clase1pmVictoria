class Inventario:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, nombre, categoria, precio, cantidad):
        self.productos.append({
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio,
            "cantidad": cantidad
        })
        print(f"Producto '{nombre}' agregado correctamente.")
    
    def eliminar_producto(self, nombre):
        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():
                self.productos.remove(producto)
                print(f"Producto '{nombre}' eliminado correctamente.")
                return
        print(f"Producto '{nombre}' no encontrado.")
    
    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():
                print(f"Información del producto: {producto}")
                return
        print(f"Producto '{nombre}' no encontrado.")
    
    def mostrar_productos_ordenados(self):
        if not self.productos:
            print("No hay productos en el inventario.")
            return
        productos_ordenados = sorted(self.productos, key=lambda x: x["precio"])
        print("Productos ordenados por precio:")
        for producto in productos_ordenados:
            print(producto)

# Ejemplo de uso del sistema de inventario
inventario = Inventario()

while True:
    print("\nOpciones:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Buscar producto")
    print("4. Mostrar productos ordenados por precio")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        nombre = input("Nombre del producto: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        inventario.agregar_producto(nombre, categoria, precio, cantidad)
    elif opcion == "2":
        nombre = input("Nombre del producto a eliminar: ")
        inventario.eliminar_producto(nombre)
    elif opcion == "3":
        nombre = input("Nombre del producto a buscar: ")
        inventario.buscar_producto(nombre)
    elif opcion == "4":
        inventario.mostrar_productos_ordenados()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
