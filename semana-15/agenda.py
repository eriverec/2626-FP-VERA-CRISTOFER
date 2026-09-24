# Programa: Agenda Telefónica de Contactos
# Este programa utiliza un diccionario para guardar nombres (claves) y números de teléfono (valores).

def mostrar_menu():
    """Muestra las opciones disponibles en la pantalla."""
    print("\n--- MI AGENDA DE CONTACTOS ---")
    print("1. Agregar un contacto nuevo")
    print("2. Mostrar todos los contactos")
    print("3. Buscar un contacto")
    print("4. Eliminar un contacto")
    print("5. Salir")

# 1. Creación de la colección de datos (Diccionario)
agenda = {}

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-5): ")

    if opcion == '1':
        # 2. Funcionalidad para insertar/agregar datos a la colección
        nombre = input("Ingresa el nombre del contacto: ")
        telefono = input("Ingresa el número de teléfono: ")
        agenda[nombre] = telefono
        print(f"✅ Contacto '{nombre}' agregado exitosamente.")

    elif opcion == '2':
        # 3. Muestra de forma clara la información almacenada en pantalla
        print("\n--- Lista de Contactos ---")
        if len(agenda) == 0:
            print("La agenda está vacía.")
        else:
            # Operación adicional: Recorrer elementos del diccionario
            for nombre, telefono in agenda.items():
                print(f"👤 {nombre}: 📞 {telefono}")
        print("--------------------------")

    elif opcion == '3':
        # 4. Operación básica adicional: Buscar un elemento
        nombre = input("Ingresa el nombre del contacto a buscar: ")
        if nombre in agenda:
            print(f"🔍 El teléfono de {nombre} es {agenda[nombre]}")
        else:
            print(f"❌ El contacto '{nombre}' no existe en la agenda.")

    elif opcion == '4':
        # 5. Operación básica adicional: Eliminar un elemento
        nombre = input("Ingresa el nombre del contacto a eliminar: ")
        if nombre in agenda:
            del agenda[nombre]
            print(f"🗑️ Contacto '{nombre}' eliminado de la agenda.")
        else:
            print(f"❌ El contacto '{nombre}' no se encontró.")

    elif opcion == '5':
        print("Saliendo del programa... ¡Hasta luego!")
        break
        
    else:
        print("⚠️ Opción no válida. Por favor, intenta de nuevo.")