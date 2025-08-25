import numpy as numpy
import pandas as pd
import zipfile

"""
ACTIVIDAD SESIÓN LIMPIEZA Y TRANSFORMACIÓN DE DATOS CON PANDAS
Imagina que eres parte del equipo de análisis de datos de una tienda en línea. El gerente te ha enviado
un archivo CSV llamado ventas.csv, el cual contiene información sobre las ventas realizadas en la
tienda. Sin embargo, debido a errores en el proceso de recolección de datos, el archivo tiene algunas
inconsistencias y problemas que deben corregirse antes de que se pueda utilizar para el análisis.

"""

#1: cargar datos e inspección de dataframe

df = pd.read_csv('ventas.csv')
print(df.head())
print(df.info())

# 2: Identificar y manejar valores perdidos
print(df.isnull())
print(df.isnull().sum())
df["Categoría"] = df["Categoría"].fillna(df["Categoría"].mode()[0])  # Reemplazar valores perdidos en 'Categoria' con la moda
#df["Precio"].fillna(df["Precio"].mean(), inplace=True)  # Reemplazar valores perdidos en 'Precio' con la media
df["Precio"] = df["Precio"].fillna(df["Precio"].mean())

# 3: Detectar y eliminar registros duplicados 
df.drop_duplicates(inplace=True)
#print(df.head())
#print(df.info())


# 4: Detectar y manejar outliers en la columna "Cantidad"

q1 = df["Cantidad"].quantile(0.25)
q3 = df["Cantidad"].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
df = df[(df["Cantidad"] >= lower_bound) & (df["Cantidad"] <= upper_bound)]
print("Cantidad de registros después de eliminar outliers:", len(df))   

# 5: Transformar la columna "Fecha" a tipo datetime
df["Fecha"] = pd.to_datetime(df["Fecha"], format="%Y-%m-%d", errors='coerce')
print(df.info())
print(df["Fecha"].dtype)
df.to_csv('ventas_limpias.csv', index=False)


# guardamos el codigo en un archivo zip
with zipfile.ZipFile('evaluacion_s4m3.zip', 'w') as zipf:
    zipf.write('evaluacion_s4m3.py')