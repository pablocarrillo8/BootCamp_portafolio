#actividad evaluada sesión 3 modulo 4

"""
ACTIVIDAD SESIÓN CORRELACIÓN
En esta actividad, generarás y analizarás datos simulados para explorar la relación entre dos
variables utilizando herramientas estadísticas y visualización en Python

"""
# Importar las bibliotecas necesarias
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import zipfile
# 1. Creación de Datos Simulados
# Generar dos listas de datos numéricos simulados que representen variables relacionadas
np.random.seed(42)

horas_ejercicio = np.random.normal(5, 2, 100)  # horas de ejercicio por semana
presion_arterial = 120 - 0.5 * horas_ejercicio + np.random.normal(0, 5, 100)  # presión arterial, con relación negativa

# 2. Construcción de una Tabla de Contingencia
# Datos categóricos simulados: grupo de edad y tipo de dieta
grupo_edad = np.random.choice(['Joven', 'Adulto', 'Mayor'], 100)
tipo_dieta = np.random.choice(['Vegetariana', 'Omnívora', 'Vegana'], 100)

tabla_contingencia = pd.crosstab(grupo_edad, tipo_dieta)

# 3. Visualización con Scatterplot
plt.scatter(horas_ejercicio, presion_arterial)
plt.title('Relación entre horas de ejercicio y presión arterial')
plt.xlabel('Horas de ejercicio por semana')
plt.ylabel('Presión arterial (mm Hg)')
plt.grid(True)
#plt.show()
plt.savefig('graficas/grafico_S3M4.png')
# 4. Cálculo del Coeficiente de Correlación de Pearson
coef_pearson, p_value = pearsonr(horas_ejercicio, presion_arterial)

# Mostrar resultados
coef_pearson, p_value, tabla_contingencia.head()

# Guardar resultados en un archivo zip
with zipfile.ZipFile('actividad_S3M4.zip', 'w') as z:
    z.write('actividad_S3M4.py')
    z.writestr('coeficiente_pearson.txt', f'Coeficiente de Pearson: {coef_pearson}\nValor p: {p_value}')
    z.writestr('tabla_contingencia.csv', tabla_contingencia.to_csv())
    z.write('graficas/grafico_S3M4.png')
