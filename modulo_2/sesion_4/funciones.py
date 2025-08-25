# Programa para demostrar el uso de funciones en Python
# Actividad práctica de sesión 3: Funciones en Python   - DataPro solutions
import zipfile
import math
import random
from statistics import mean

# 1. Función para calcular el área de un rectángulo
def calcular_area_rectangulo(largo, ancho):
    return largo * ancho

# 2. Función para calcular la circunferencia de un círculo
def calcular_circunferencia(radio):
    return 2 * math.pi * radio

# 3. Función para calcular el promedio manualmente
def calcular_promedio(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

# 4. Función para calcular el promedio usando statistics.mean
def calcular_promedio_avanzado(lista):
    return mean(lista)

# 5. Función para generar números aleatorios
def generar_numeros_aleatorios(cantidad, limite):
    return [random.randint(1, limite) for _ in range(cantidad)]

# 6. Programa principal que usa todas las funciones
if __name__ == "__main__":
    # Área del rectángulo
    area = calcular_area_rectangulo(3, 4)
    print("Área del rectángulo (10x5):", area)

    # Circunferencia de un círculo
    circunferencia = calcular_circunferencia(6378)  # Radio de la Tierra en km
    print("Circunferencia del círculo (radio tierra):", circunferencia)

    # Lista de ejemplo para promedios
    lista_numeros = [11, 42, 51, 125,  36, 78, 90, 100, 45, 67]
    print("Lista de números:", lista_numeros)

    # Promedio manual
    promedio = calcular_promedio(lista_numeros)
    print("Promedio con cálculos básicos:", promedio)

    # Promedio avanzado con statistics.mean
    promedio_avanzado = calcular_promedio_avanzado(lista_numeros)
    print("Promedio con statistics.mean:", promedio_avanzado)

    # Generar números aleatorios
    numeros_aleatorios = generar_numeros_aleatorios(5, 50)
    print("Números aleatorios generados (5 entre 1 y 50):", numeros_aleatorios)

with zipfile.ZipFile('sesion4.zip', 'w') as zip_ref:
    zip_ref.write('funciones.py')
    print("Archivo comprimido creado: sesion4.zip")