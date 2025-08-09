import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px 
import plotly.graph_objects as go 
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score 
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm 

"""
Desafíos de Ciencia de Datos – Regresión y Clasificación con Datos Reales 
Contexto: Mortalidad en centros de cultivo y rendimiento de cosechas. 


RETO 1 (Regresión): Predecir cantidad de mortalidades semanales 
Archivo: Mortalidades_Centro de cultivos.csv 
Objetivo: Construir un modelo de regresión para predecir la cantidad de mortalidades semanales 
usando edad, especie, centro, densidad, alimentación, etc. 

 🌽
 Pasos a seguir: 
1. Importar bibliotecas 
2. Cargar el archivo CSV 
3. Mostrar primeras filas y .info() 
4. Mostrar estadísticas descriptivas 
5. Detectar y tratar valores faltantes con la mediana 
6. Convertir tipos de datos apropiadamente 
7. Verificar que no queden valores nulos 
8. Generar gráfico interactivo: Edad vs Mortalidades 
9. Generar gráfico: Centro vs Mortalidades 
10. Detectar outliers (rango intercuartílico - IQR) 
11. Codificar Centro, Especie, Alimentación con OneHotEncoder 
12. Separar X (variables predictoras) e y (mortalidades) 
13. Dividir en datos de entrenamiento y prueba (80/20) 
14. Agregar constante para modelo 
15. Entrenar modelo de regresión con statsmodels.OLS 
16. Mostrar resumen del modelo 
17. Mostrar coeficientes de variables 
18. Predecir mortalidades en el conjunto de prueba 
19. Evaluar con MSE y R² 
20. Graficar reales vs predichos + guardar imagen 

"""

# Cargar el archivo xlsx

df = pd.read_excel('entradas/Mortalidades_2023_202410.xlsx')
print(df.head(5))
print(df.info())
print(df.describe())