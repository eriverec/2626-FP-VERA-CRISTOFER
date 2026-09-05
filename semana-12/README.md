# Sistema de Reserva de Asientos de Cine

## Datos del Estudiante
- **Nombre:** CRISTOFER ERI VERA ITURRALDE
- **Materia:** FUNDAMENTOS DE PROGRAMACION PARALELO A
- **Semana:** 12

## Descripción del Proyecto
Este programa en Python simula el control de reservas de una sala de cine con capacidad para 12 asientos distribuidos en una matriz de 3 filas por 4 columnas.

El sistema:
1. Representa la sala mediante una lista de listas (matriz 3x4) inicializada en `0` (asiento libre).
2. Solicita al usuario la fila (`0-2`) y la columna (`0-3`) a reservar.
3. Actualiza el valor a `1` (asiento reservado).
4. Muestra la matriz resultante en formato de tabla usando bucles anidados `for`.

## Cómo ejecutar el programa
1. Clonar el repositorio o descargar el archivo `reserva_cine.py`.
2. Abrir una terminal en el directorio del archivo.
3. Ejecutar el comando:
   ```bash
   python reserva_cine.py