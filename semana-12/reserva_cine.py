# =============================================================================
# Tarea Semana 12: Reserva de un asiento en sala de cine
# Unidad 3: Arreglos N-Dimensionales (Listas de listas en Python)
# =============================================================================

def gestionar_reserva():
    # 1. Creación de la matriz 3x4 inicializada en 0 (asientos libres)
    # 3 filas (0 a 2) y 4 columnas (0 a 3)
    asientos = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    print("--- SISTEMA DE RESERVA DE CINE ---")
    print("Dimensiones de la sala: 3 filas (0-2) y 4 columnas (0-3)\n")

    # 2. Solicitud de datos al usuario con validación de rangos
    try:
        fila = int(input("Ingrese la fila que desea reservar (0 a 2): "))
        columna = int(input("Ingrese la columna que desea reservar (0 a 3): "))

        # Validación de límites de la matriz
        if 0 <= fila <= 2 and 0 <= columna <= 3:
            # 3. Modificación del elemento en la posición solicitada
            if asientos[fila][columna] == 0:
                asientos[fila][columna] = 1
                print(f"\n✓ ¡Asiento [{fila}][{columna}] reservado con éxito!\n")
            else:
                print(f"\n⚠ El asiento [{fila}][{columna}] ya está reservado.\n")
        else:
            print("\n❌ Error: Posición fuera de rango. Fila (0-2) o Columna (0-3) inválida.\n")

    except ValueError:
        print("\n❌ Error: Debe ingresar únicamente números enteros.\n")
        return

    # 4. Recorrido y visualización de la matriz con bucles anidados
    print("Estado actual de la sala (0 = Libre, 1 = Reservado):")
    print("-" * 25)

    # Bucle externo: itera sobre las filas (i)
    for i in range(len(asientos)):
        # Bucle interno: itera sobre las columnas (j)
        for j in range(len(asientos[i])):
            # Imprime cada valor separado por un espacio sin saltar de línea
            print(asientos[i][j], end=" ")
        # Salto de línea al terminar de imprimir todas las columnas de la fila actual
        print()

    print("-" * 25)

if __name__ == "__main__":
    gestionar_reserva()