# Inicializar la matriz de 5x5 con ceros
matriz = [[0 for _ in range(5)] for _ in range(5)]

print("=== INGRESO DE DATOS A LA MATRIZ 5x5 ===")

# Solicitar los 25 valores al usuario
for i in range(5):
    for j in range(5):
        matriz[i][j] = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))

# Mostrar la matriz en formato tabular
print("\nMatriz ingresada:")
for i in range(5):
    for j in range(5):
        print(matriz[i][j], end="\t")
    print()