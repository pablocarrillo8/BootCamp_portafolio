# 1. Importar la librería NumPy
import numpy as np

# 2. Crear un vector de 10 elementos con valores del 1 al 10
vector = np.arange(1, 11)
print("Vector del 1 al 10:")
print(vector)

# 3. Generar una matriz de 3x3 con valores aleatorios entre 0 y 1
matriz_aleatoria = np.random.rand(3, 3)
print("\nMatriz 3x3 con valores aleatorios entre 0 y 1:")
print(matriz_aleatoria)

# 4. Crear una matriz identidad de tamaño 4x4
matriz_identidad = np.eye(4)
print("\nMatriz identidad 4x4:")
print(matriz_identidad)

# 5. Redimensionar el vector en una matriz de 2x5
matriz_2x5 = vector.reshape(2, 5)
print("\nVector redimensionado a matriz 2x5:")
print(matriz_2x5)

# 6. Seleccionar los elementos mayores a 5 del vector original
mayores_a_5 = vector[vector > 5]
print("\nElementos del vector mayores a 5:")
print(mayores_a_5)

# 7. Operación matemática entre arreglos (suma)
arreglo1 = np.arange(5)
arreglo2 = np.arange(5)
suma_arreglos = arreglo1 + arreglo2
print("\nSuma de dos arreglos:")
print("Arreglo 1:", arreglo1)
print("Arreglo 2:", arreglo2)
print("Suma:", suma_arreglos)

# 8. Aplicar una función matemática: raíz cuadrada
raices_cuadradas = np.sqrt(vector)
print("\nRaíz cuadrada de los elementos del vector:")
print(raices_cuadradas)