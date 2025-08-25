#reto 38b
"""
RETO 2: Análisis, Escalamiento y Modelado de Rendimiento
(kg/mš)
Dataset: Cosechas_Cosechas_2023b.csv
Variable objetivo: Rendimiento (kg/mš)
"""

# 1: Importar librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split        
from sklearn.linear_model import LinearRegression, Ridge, Lasso 
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score         
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import Pipeline, make_pipeline

# 2: Cargar el dataset
df = pd.read_csv('Cosechas_Cosechas_2023b.csv')

#Antes le borre en la última linea del csv una información y borre las primeras FILAS vacias para que me queden los nombres de las columnas al inicio 
 
df = pd.read_csv('Cosechas_Cosechas_2023.csv', sep=',' ,header=None,usecols=range(1, 8),skiprows=1) # usecols=range(1, 8) para seleccionar las columnas de la 2 a la 8 (0 es la primera columna)
 
# Paso 2: Asignar nombres de columna (opcional)
nombres_columnas = ['Código Centro','Empresa','Especie','Toneladas Cosechadas','Mes Inicio Ciclo','Mes Fin Ciclo','Periodo Información']
df.columns = nombres_columnas