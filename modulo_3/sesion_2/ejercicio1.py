import pandas as pd
import numpy as np

dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
temperatura_diaria = [20, 22, 21, 19, 23, 25, 24]

serie_temperatura_diaria = pd.Series(temperatura_diaria, index=dias)
#print(serie_temperatura_diaria)


print(serie_temperatura_diaria["lunes"])  # Acceso por etiqueta
print(serie_temperatura_diaria[0])  # Acceso por posición
print(serie_temperatura_diaria[1:4])  # Acceso por rango de posiciones
print("\nPromedio de temperatura diaria:")
print(serie_temperatura_diaria.mean())  # Cálculo del promedio
#print(serie_temperatura_diaria.groupby(temperatura_diaria).mean())  # Agrupación por condición y cálculo de la media

