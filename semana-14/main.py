def calcular_total_compra(precio_unitario, cantidad, impuesto_porcentaje, descuento_porcentaje):
    """
    Calcula el subtotal, aplica el impuesto, resta el descuento
    y retorna el valor neto a pagar.
    """
    # Cálculo del subtotal base
    subtotal = precio_unitario * cantidad
    
    # Cálculo del monto adicional por impuesto
    monto_impuesto = subtotal * (impuesto_porcentaje / 100)
    
    # Cálculo del monto a descontar
    monto_descuento = subtotal * (descuento_porcentaje / 100)
    
    # Cálculo del total final
    total_a_pagar = subtotal + monto_impuesto - monto_descuento
    
    # Retorno del resultado calculado al punto donde se llamó la función
    return total_a_pagar


print("--- SISTEMA DE FACTURACIÓN BÁSICO ---")


# Datos de entrada para la prueba
precio = 25.0       # Precio por unidad en dólares
unidades = 4        # Cantidad de productos comprados
iva = 15.0          # 15% de impuesto
descuento = 10.0    # 10% de descuento promocional


resultado_final = calcular_total_compra(precio, unidades, iva, descuento)

print(f"Precio unitario: ${precio:.2f}")
print(f"Cantidad: {unidades} unidades")
print(f"Subtotal: ${precio * unidades:.2f}")
print(f"Impuesto aplicado: {iva}%")
print(f"Descuento aplicado: {descuento}%")
print("-------------------------------------")
print(f"Total a pagar: ${resultado_final:.2f}")