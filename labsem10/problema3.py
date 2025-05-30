class AgendaContactos:
    def __init__(self):
        self.contactos = []
    
    def agregar_contacto(self, nombre, numero, correo):
        contacto = (nombre, numero, correo)
        self.contactos.append(contacto)
        print(f"Contacto '{nombre}' agregado correctamente.")
    
    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto[0].lower() == nombre.lower():
                print(f"Detalles del contacto: Nombre: {contacto[0]}, Número: {contacto[1]}, Correo: {contacto[2]}")
                return
        print(f"Contacto '{nombre}' no encontrado.")
    
    def listar_contactos(self):
        if not self.contactos:
            print("No hay contactos en la agenda.")
            return
        contactos_ordenados = sorted(self.contactos, key=lambda x: x[0].lower())
        print("Lista de contactos ordenados alfabéticamente:")
        for contacto in contactos_ordenados:
            print(f"Nombre: {contacto[0]}, Número: {contacto[1]}, Correo: {contacto[2]}")

# Ejemplo de uso de la agenda de contactos
agenda = AgendaContactos()

while True:
    print("\nOpciones:")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Listar contactos ordenados alfabéticamente")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        nombre = input("Nombre del contacto: ")
        numero = input("Número de teléfono: ")
        correo = input("Correo electrónico: ")
        agenda.agregar_contacto(nombre, numero, correo)
    elif opcion == "2":
        nombre = input("Nombre del contacto a buscar: ")
        agenda.buscar_contacto(nombre)
    elif opcion == "3":
        agenda.listar_contactos()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
