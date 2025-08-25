# actividad evaluada sesion 1
import zipfile
#1. Importar la librería NumPy
import numpy as np
#2. Crear un vector de 10 elementos con valores del 1 al 10 utilizando arange()
vector = np.arange(1,11)
print(vector)
#Generar una matriz de 3x3 con valores aleatorios entre 0 y 1 usando random.rand() 
matriz = np.random.rand(3, 3) 
print(matriz)
# 4: Crear una matriz identidad de tamaño 4x4 utilizando eye() 
identidad = np.eye(4)
print(identidad)
#5:Redimensionar el vector creado en el punto 2 en una matriz de 2x5 usando .reshape()
vector_reshaped = vector.reshape(2, 5)
print(f"\nVector redimensionado: \n{vector_reshaped}")
print(f"Forma redimensionada: {vector_reshaped.shape}") # # shape  muestra las dimensiones del arreglo 2 x 5
# 6: Seleccionar los elementos mayores a 5 del vector original y mostrarlos
print(f"\nNúmeros mayores a 5 en vector:  \n{vector[vector > 5]}")
# 7: Realizar una operación matemática entre arreglos; Crea dos arreglos de tamaño 5 con arange() y súmalos, muestralos-
arr_1 = np.arange(20, 25)
arr_2 = np.arange(26,31)
print(f"Suma de los arreglos: \n{arr_1 + arr_2}")
#8: Aplicar una función matemática a un arreglo
print(f"Aplicar una función matemática al array 2: \n{np.sqrt(arr_2)}")

zipfile.ZipFile('evaluacion_s1m3.zip', 'w').write('evaluacion_s1m3.py')