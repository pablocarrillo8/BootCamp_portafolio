"""
ACTIVIDAD SESIÓN CONCEPTOS BÁSICOS DE ESTADÍSTICA DESCRIPTIVA
Deberás trabajar con un conjunto de datos ficticio para calcular estadísticas descriptivas clave y
visualizar la distribución de los datos. Se utilizarán herramientas como Pandas, NumPy y Matplotlib
para realizar el análisis.

"""
import matplotlib
#matplotlib.use('Qt5Agg') # O 'TkAgg', 'Agg' es non-interactive
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import zipfile
import pandas as pd
import numpy as np

# CARGA DE DATOS
df = pd.read_csv('entrada/datos_S2M4.csv', sep=',',  header=0)
# Visualización de las primeras filas del DataFrame
print(df.head())
print(df.columns)
print(type(df))
df.columns = df.columns.str.strip()


# 1. Definir Variables:  Identificar el tipo de variable (categórica, cuantitativa discreta o continua) de cada columna en el conjunto de datos.
variables = {
    'ID': 'categórica',
    'Nombre': 'categórica',
    'Edad': 'cuantitativa discreta',
    'Ingresos': 'cuantitativa continua',
    'Género': 'categórica',
    'Ciudad': 'categórica',
}
print("Tipos de variables:")
for var, tipo in variables.items():
    print(f"{var}: {tipo}")

#guardamos el DataFrame para su uso posterior
#df.to_csv('entrada/datos_df_S2M4.csv', index=False)

# 2. Construcción de una Tabla de Frecuencia: Generar una tabla de frecuencia para una variable categórica y otra para una variable cuantitativa discreta.

# Tabla de frecuencia para la variable categórica 'Género'
tabla_frecuencia_genero = df['Género'].value_counts()
print("\nTabla de Frecuencia para Género:")
print(tabla_frecuencia_genero)

# Tabla de frecuencia para la variable cuantitativa discreta 'Edad'
tabla_frecuencia_edad = df['Edad'].value_counts().sort_index() #sort_index() para ordenar por edad
print("\nTabla de Frecuencia para Edad:")
print(tabla_frecuencia_edad)
# 3. Cálculo de Medidas de Tendencia Central: Calcular la media, mediana y moda para una variable cuantitativa continua.
media_ingresos = df['Ingresos'].mean()
mediana_ingresos = df['Ingresos'].median()
moda_ingresos = df['Ingresos'].mode()[0]  # La moda puede devolver múltiples valores, tomamos el primero
print("\nMedidas de Tendencia Central para Ingresos:")
print(f"Media: {media_ingresos}")
print(f"Mediana: {mediana_ingresos}")
print(f"Moda: {moda_ingresos}")

# 4. Cálculo de Medidas de Dispersión: Calcular la desviación estándar, Varianza y el rango intercuartílico (IQR) para la variable cuantitativa continua.
desviacion_estandar_ingresos = df['Ingresos'].std()
varianza_ingresos = df['Ingresos'].var()
q1_ingresos = df['Ingresos'].quantile(0.25)
q3_ingresos = df['Ingresos'].quantile(0.75)
iqr_ingresos = q3_ingresos - q1_ingresos
print("\nMedidas de Dispersión para Ingresos:")
print(f"Desviación Estándar: {desviacion_estandar_ingresos}")
print(f"Varianza: {varianza_ingresos}")
print(f"Rango Intercuartílico (IQR): {iqr_ingresos}")

# 5. Visualización de Datos: Crear un histograma y un boxplot para la otra variable

# Histograma para la variable cuantitativa continua 'Edad'  
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(df['Edad'], bins=10, color='skyblue', edgecolor='black')
plt.title('Histograma de Edad')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
# Boxplot para la variable cuantitativa continua 'Edad'
plt.subplot(1, 2, 2)
plt.boxplot(df['Edad'], vert=False, patch_artist=True, boxprops=dict(facecolor='lightgreen', color='black'))
plt.title('Boxplot de Edad')
plt.xlabel('Edad')
plt.tight_layout() # Ajusta el layout para evitar superposiciones
plt.savefig("salida/grafico_edades.png", dpi=300, bbox_inches="tight")
#plt.show()

# Guardar el script en un archivo zip
# with zipfile.ZipFile('salida/actividad_S2M4.zip', 'w') as zipf:
#     zipf.write('entrada/datos_S2M4.csv', arcname='datos_S2M4.csv')
#     zipf.write('salida/grafico_edades.png', arcname='grafico_edades.png')
#     zipf.write('actividad_S2M4.py', arcname='actividad_S2M4.py')    
    