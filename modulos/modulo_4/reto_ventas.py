import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
df = pd.read_csv('entrada/ventas.csv')

print(df.head(10)) # Display the first few rows of the dataset
print("--------- DataFrame Information ---------")
print(df.info())   # Display information about the DataFrame
#print("--------- Summary Statistics ---------")
#print(df.describe())  # Display summary statistics


# 1.1 Cuenta cuántos valores nulos hay en cada columna.
print("Valores faltantes por columna") 
print(df.isnull().sum())
# Otra forma de mostrar los nulos por columna, mostrando True/False
# print("\nVisualización de nulos (True/False):")
# print(df.isnull())
print("Filas duplicadas",df.duplicated().sum())
print("Tipo de datos por columna")
print(df.dtypes)



#  2. Limpieza de datos
# 2.1 rellenar con valores nulos en precio con la mediana        
df = df.drop_duplicates() #eliminar duplicados
df.fillna(df['precio'].median(), inplace=True, )
df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')  # Convertir la columna 'fecha' a tipo datetime, erros ='coerce' convierte errores a NaT: not a Time
print("--------- DataFrame Information After Cleaning ---------")
print(df.info())   # Display information about the DataFrame after cleaning 

# 3.Análisis univariado 
# 3.1 Estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(df.describe())
# 3.2 Medidas de tendencia central
print("\nMedidas de tendencia central:")
print("Media del precio:", df['precio'].mean())
print("Mediana del precio:", df['precio'].median())
print("Moda del precio:", df['precio'].mode()[0])  # mode() devuelve una Serie, tomamos el primer valor
# 3.3 Medidas de dispersión
print("\nMedidas de dispersión:")
print("Rango del precio:", df['precio'].max() - df['precio'].min())
print("Desviación estándar del precio:", df['precio'].std())
# 3.4 Visualización de la distribución del precio y cantidad vendida
sns.histplot(df['precio'], kde=True, bins=30) # kde=True añade una curva de densidad, bins=30 define el número de barras en el histograma
sns.histplot(df['cantidad_vendida'], kde=True, bins=30) # Histograma para la cantidad vendida
plt.title("Distribución del Precio")
plt.subplot(2, 1, 1)  # Subplot para el histograma del precio
plt.subplot(2, 2, 2)  # Subplot para el histograma de cantidad vendida
plt.xlabel("Precio")

plt.show()
# 3.5 Boxplot para detectar valores atípicos (outliers)
sns.boxplot(x=df['precio'])
plt.title("3.5 Boxplot del Precio") 
plt.xlabel("Precio")
plt.show()
sns.boxplot(x=df['cantidad_vendida'])
plt.title("3.5 Boxplot de Cantidad Vendida")    
plt.xlabel("Cantidad Vendida")
plt.show()

# 4. Deteccion de outliers
# 4.1 Usa el rango intercuartílico (IQR) para calcular los outliers en precioy cantidad_vendida.
# Calcular el IQR
Q1_precio = df['precio'].quantile(0.25)
Q3_precio = df['precio'].quantile(0.75)
IQR_precio = Q3_precio - Q1_precio
Q1_cantidad = df['cantidad_vendida'].quantile(0.25)
Q3_cantidad = df['cantidad_vendida'].quantile(0.75)
IQR_cantidad = Q3_cantidad - Q1_cantidad
# Definir los límites para detectar outliers
lower_bound_precio = Q1_precio - 1.5 * IQR_precio
upper_bound_precio = Q3_precio + 1.5 * IQR_precio
lower_bound_cantidad = Q1_cantidad - 1.5 * IQR_cantidad
upper_bound_cantidad = Q3_cantidad + 1.5 * IQR_cantidad
# Filtrar los outliers
outliers_precio = df[(df['precio'] < lower_bound_precio) | (df['precio'] > upper_bound_precio)]
outliers_cantidad = df[(df['cantidad_vendida'] < lower_bound_cantidad)
    | (df['cantidad_vendida'] > upper_bound_cantidad)]
print("\nOutliers en Precio:")
print(outliers_precio)
print("\nOutliers en Cantidad Vendida:")
print(outliers_cantidad)
# 4.2 Visualización de los outliers
plt.figure(figsize=(10, 5))
sns.boxplot(x=df['precio'])
plt.title("4.2 Boxplot del Precio con Outliers")
plt.xlabel("Precio")
plt.show()
plt.figure(figsize=(10, 5))
sns.boxplot(x=df['cantidad_vendida'])
plt.title("4.2 Boxplot de Cantidad Vendida con Outliers")
plt.xlabel("Cantidad Vendida")
plt.show()
# 4.3 Eliminar los outliers del DataFrame
df = df[(df['precio'] >= lower_bound_precio) & (df['precio'] <= upper_bound_precio)]
df = df[(df['cantidad_vendida'] >= lower_bound_cantidad) & (df['cantidad_vendida'] <= upper_bound_cantidad)]
# 4.4 Verificar si se han eliminado los outliers
print("\nValores faltantes por columna después de eliminar outliers:")
print(df.isnull().sum())
print("Filas duplicadas después de eliminar outliers:", df.duplicated().sum())
# 4.5 Visualización de la distribución del precio y cantidad vendida después de eliminar outliers
sns.histplot(df['precio'], kde=True, bins=30)
plt.title("4.5 Distribución del Precio Después de Eliminar Outliers")
plt.xlabel("Precio")
plt.show()
sns.histplot(df['cantidad_vendida'], kde=True, bins=30)
plt.title("4.5 Distribución de Cantidad Vendida Después de Eliminar Outliers")
plt.xlabel("Cantidad Vendida")
plt.show()

# Identifica cuántos valores extremos existen y decide si conservarlos o no
# 4.6 Identificación de valores extremos
num_outliers_precio = len(outliers_precio)
num_outliers_cantidad = len(outliers_cantidad)
print(f"\nNúmero de outliers en Precio: {num_outliers_precio}")
print(f"Número de outliers en Cantidad Vendida: {num_outliers_cantidad}")
# 4.7 Decisión sobre los outliers
# En este caso, hemos decidido eliminar los outliers del DataFrame, pero se podría optar por conservarlos dependiendo del contexto del análisis.    
# 4.8 Visualización de la distribución del precio y cantidad vendida después de eliminar outliers
sns.histplot(df['precio'], kde=True, bins=30)
plt.title("4.8 Distribución del Precio Después de Eliminar Outliers")




# 5. Analisis bivariado
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='precio', y='cantidad_vendida', hue='categoria', style='categoria', s=100) # hue='categoria' añade color por categoría, style='categoria' añade estilo por categoría, s=100 define el tamaño de los puntos
plt.title("Precio vs Cantidad Vendida")
plt.xlabel("Precio")
plt.ylabel("Cantidad Vendida")
plt.show()