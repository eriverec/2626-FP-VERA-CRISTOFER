"""
Programa para calcular el total a pagar en una compra minorista.
Autor: [Tu Nombre y Apellido]
Fecha: Septiembre 2026
"""

def calcular_total_compra(precio_unitario: float, cantidad: int) -> float:
    """
    Calcula el monto total a pagar multiplicando el precio unitario por la cantidad.

    Parámetros:
        precio_unitario (float): Precio de cada producto.
        cantidad (int): Número de unidades adquiridas.

    Retorna:
        float: El total a pagar.
    """
    total = precio_unitario * cantidad
    return total


if __name__ == "__main__":
    # Datos de prueba para la ejecución
    precio = 12.50
    unidades = 4

    # Llamada a la función y captura del resultado retornado
    resultado_pago = calcular_total_compra(precio, unidades)

    # Muestra del resultado en consola con formato monetario
    print("--- Sistema de Facturación ---")
    print(f"Precio por unidad: ${precio:.2f}")
    print(f"Cantidad adquirida: {unidades}")
    print(f"Total a cancelar:  ${resultado_pago:.2f}")