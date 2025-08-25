# Reto número 1: temperaturas CDMX - Guadalajara - Monterrey
import pandas as pd
import numpy as np

# Cargar el archivo CSV
df = pd.read_csv('reto1_temperatura_ampliado.csv')
print(df.head())
print(df.info())

# encontrar valores vacios y rellenar con la media
nans_positions = df[df["Temperatura_Maxima"].isnull()].index.tolist()
#print(f"Posiciones de valores nulos en 'Temperatura_Maxima': {nans_positions}")
#print(df.isnull().sum())
media = df['Temperatura_Maxima'].mean()
df['Temperatura_Maxima'] = df['Temperatura_Maxima'].fillna(media)
#df["Temperatura_Maxima"] = df["Temperatura_Maxima"].fillna(df["Temperatura_Maxima"].mean())
#df.to_csv("salidas/reto1_temperatura_ampliado.csv", index=False)

# 2.Discretizar con pd.cut() en categorías
## valores = [10, 20, 30, 40, 50]
#bins = [-np.inf, 20, 40, np.inf]
#categorias = pd.cut(valores, bins=bins)
# print(categorias)
# Esto agrupa los valores en tres intervalos:
# - Menos de 20
# - Entre 20 y 40
# - Más de 40
# Usar -np.inf y np.inf asegura que todos los valores extremos sean incluidos en los intervalos.

df["Temperatura_Maxima_Categoria"] = pd.cut(
    df["Temperatura_Maxima"],
    bins=[-np.inf, 15, 25, np.inf],
    labels=["Frio", "Templado", "Caluroso"], 
)

# Mostrar el conteo de cada categoría   
#print(df["Temperatura_Maxima_Categoria"].value_counts())
#df.to_csv("salidas/reto1_temperatura_ampliado_categorias.csv", index=False)

# 3.Analizar diferencias de temperatura por ciudad.
# primero necesito saber cuantas ciudades hay
ciudades = df["Ciudad"].unique() # unique devuelve un array con los valores únicos de la columna Ciudad
print(ciudades)
# convertir el array a una lista
ciudades = ciudades.tolist()  # Convertir el array a una lista
# ahora puedo imprimir las ciudades únicas
# y contar cuántas hay
num_ciudades = len(ciudades)  # Contar el número de ciudades únicas
print(f"Número de ciudades únicas: {num_ciudades}") 
print(f"Ciudades únicas en el DataFrame: {ciudades}")

# Agrupar por ciudad y calcular la temperatura máxima promedio
temperatura_promedio_por_ciudad = df.groupby("Ciudad")["Temperatura_Maxima"].mean().reset_index() # groupby agrupa el DataFrame por la columna Ciudad y calcula la media de la columna Temperatura_Maxima
print("Temperatura promedio por ciudad:")
for ciudad in ciudades:
    promedio = temperatura_promedio_por_ciudad[temperatura_promedio_por_ciudad['Ciudad'] == ciudad]['Temperatura_Maxima'].values[0]
    print(f"{ciudad}: {promedio}")
    