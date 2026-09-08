# Tarea Práctica: Cálculo de Total de Compra en Python

**Estudiante:** CRISTOFER ERI VERA ITURRALDE  
**Curso:** Fundamentos de Programación / Definición y uso de funciones

---

## 📌 Descripción del Problema
En un comercio o tienda minorista es necesario calcular de manera automática y precisa el valor total a cancelar por un cliente según el precio individual del artículo y el número de unidades adquiridas.

---

## 📝 Algoritmo en Pseudocódigo

```text
ALGORITMO CalcularTotalCompra
    FUNCION calcular_total_compra(precio_unitario, cantidad)
        total <- precio_unitario * cantidad
        RETORNAR total
    FIN FUNCION

    INICIO
        precio <- 12.50
        unidades <- 4
        resultado <- calcular_total_compra(precio, unidades)
        IMPRIMIR "Total a pagar: ", resultado
    FIN
FIN ALGORITMO