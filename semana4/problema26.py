import json

# Archivo donde se almacenarán los contactos
ARCHIVO_CONTACTOS = "agenda.json"

# Cargar contactos desde el archivo
def cargar_contactos():
    try:
        with open(ARCHIVO_CONTACTOS, "r") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Guardar contactos en el archivo
def guardar_contactos(contactos):
    with open(ARCHIVO_CONTACTOS, "w") as archivo:
        json.dump(contactos, archivo, indent=4)

# Agregar un nuevo contacto
def agregar_contacto(contactos):
    nombre = input("Nombre: ").strip()
    if nombre in contactos:
        print("El contacto ya existe.")
        return
    
    telefono = input("Teléfono: ").strip()
    correo = input("Correo electrónico: ").strip()
    contactos[nombre] = {"Teléfono": telefono, "Correo": correo}
    guardar_contactos(contactos)
    print(f"Contacto {nombre} agregado.")

# Buscar un contacto por nombre
def buscar_contacto(contactos):
    nombre = input("Ingrese el nombre del contacto a buscar: ").strip()
    if nombre in contactos:
        print(f"📌 {nombre}: Teléfono: {contactos[nombre]['Teléfono']}, Correo: {contactos[nombre]['Correo']}")
    else:
        print("Contacto no encontrado.")

# Mostrar todos los contactos
def mostrar_contactos(contactos):
    if not contactos:
        print("La agenda está vacía.")
    else:
        print("\n📖 Agenda de contactos:")
        for nombre, info in contactos.items():
            print(f"{nombre} - Teléfono: {info['Teléfono']}, Correo: {info['Correo']}")
        print()

# Eliminar un contacto
def eliminar_contacto(contactos):
    nombre = input("Ingrese el nombre del contacto a eliminar: ").strip()
    if nombre in contactos:
        del contactos[nombre]
        guardar_contactos(contactos)
        print(f"Contacto {nombre} eliminado.")
    else:
        print("Contacto no encontrado.")

# Menú principal
def menu():
    contactos = cargar_contactos()

    while True:
        print("\n📒 AGENDA DE CONTACTOS")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Mostrar todos los contactos")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_contacto(contactos)
        elif opcion == "2":
            buscar_contacto(contactos)
        elif opcion == "3":
            mostrar_contactos(contactos)
        elif opcion == "4":
            eliminar_contacto(contactos)
        elif opcion == "5":
            print("Saliendo de la agenda...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
