import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sns

""""
Clase modulo 4, sesión 2: Práctica de detección y tratamiento de outliers
En esta clase revisamos los tipos de variables, discretas y continuas, ademas de aplicar Estadisticas descriptivas.
"""
# 1. Load the dataset
df = pd.read_csv('entrada/dataset_con_outliers.csv')

# 2 : Frecuencia de variables categoricas
freq_color = df['Color'].value_counts() # value_counts() arroja por defecto el orden de mayor a menor
freq_satifacion = df['Satisfaction'].value_counts(sort=False) # Sort=False mantiene el orden original de aparición.
print("\nFrecuencia de colores: ", freq_color)
print("\nFrecuencia de satisfacción: ", freq_satifacion)

# 3. función para obtener estadisticas descriptivas
def estadisticas_descriptivas(df):
    return pd.DataFrame({
        'Media': df.mean(),
        'Mediana': df.median(),
        'Moda': df.mode().iloc[0],  # .mode() devuelve una serie, tomamos el primer valor
        'Varianza': df.var(),
        'Desviación Estándar': df.std(),
        'Mínimo': df.min(),
        'Máximo': df.max(),
        'Rango': df.max() - df.min(),
        'IQR': df.quantile(0.75) - df.quantile(0.25) # IQR: Interquartile Range, rango intercuartil: 
    })

# 4. Estadísticas descriptivas para DataFrame original
df_origin = estadisticas_descriptivas(df[['Children', 'Temperature']])
print("\nEstadísticas descriptivas del DataFrame original:", df_origin)

"""
El método del rango intercuartílico (IQR) es una técnica estadística para identificar valores atípicos (outliers)
en un conjunto de datos. Se basa en la dispersión de los datos calculada a través de los cuartiles.
Un dato se considera outlier si es menor que Q1 - 1.5 * IQR o mayor que Q3 + 1.5 * IQR, donde Q1 es el primer cuartil,
Q3 es el tercer cuartil, y IQR es el rango intercuartílico (Q3 - Q1)

"""
# 4.1 Calcular el IQR para detectar outliers
def Detectar_outliers(serie):
    Q1 = serie.quantile(0.25)
    Q3 = serie.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = serie[(serie < lower_bound) | (serie > upper_bound)] 
    return outliers, lower_bound, upper_bound

out_children, lower_bound_children, upper_bound_children = Detectar_outliers(df['Children'])
out_temperature, lower_bound_temperature, upper_bound_temperature = Detectar_outliers(df['Temperature'])
print("\nOutliers en Children:", out_children.values)
print("\nOutliers en Temperature:", out_temperature.values)




# 5. Crear PDF con análisis 
# with PdfPages('salida/analisis_outliers.pdf') as pdf:
#     # 5.1 Histograma de Children
#     plt.figure(figsize=(10, 5))
#     sns.histplot(df['Children'], kde=True, bins=30)
#     plt.title("Distribución de Children")
#     plt.xlabel("Children")
#     plt.ylabel("Frecuencia")
#     pdf.savefig()  # Save the current figure into the PDF
#     plt.close()

#     # 5.2 Boxplot de Temperature
#     plt.figure(figsize=(10, 5))
#     sns.boxplot(x=df['Temperature'])
#     plt.title("Boxplot de Temperature")
#     plt.xlabel("Temperature")
#     pdf.savefig()  # Save the current figure into the PDF
#     plt.close()

#Eliminar registro  con outlier
df_clean = df[
    (df['Children'].between(li_c,ls_c)) &
    (df['Temperature'].between(li_t,ls_t)) ]

estadisticas_limpia = calcular_estadisticas(df_clean[['Children', 'Temperature']])
print(estadisticas_limpia)


# Paso 6: Crear Pdf con analisis 
with PdfPages('salida/analisis_reporte.pdf') as pdf:
    #Pagina 1: Portada
    fig = plt.figure(figsize=(11,8.5))
    plt.suptitle("Reporte Analisis de Datos", fontsize=16, y=0.95)
    plt.text(0.1, 0.6, f"Dataset Original:{len(df)} registros", fontsize=12)
    plt.text(0.1, 0.4, f"Dataset limpios:{len(df_clean)} registros", fontsize=12)
    plt.axis('off')
    pdf.savefig(fig)
    plt.close()
    
    
    #Pagina Tabla de frencuencias  
    fig, ax = plt.subplots(figsize=(11,8.5)) 
    ax.axis('off')
    tabla = pd.concat([freq_color,freq_satifacion], axis=1, keys=['Color', 'Satifacion']).fillna('')
    t= ax.table(cellText=tabla.values,
                colLabels=tabla.columns,
                rowLabels=tabla.index,
                loc='center')
    t.scale(1,1.5)
    ax.set_title("Frencuencia de variable categorica", fontsize=14, pad=20)
    pdf.savefig()
    plt.close

#Pagina3 : Estadisticas descriptivas
    fig, ax = plt.subplots(figsize=(11,8.5)) 
    ax.axis('off')
    resumen= pd.concat([estadisticas_originales.round(2),estadisticas_limpia.round(2)], axis=1, keys=['Original', 'limpio'])
    t= ax.table(cellText=resumen.values,
                colLabels=resumen.columns,
                rowLabels=resumen.index,
                loc='center')
    t.scale(1,1.5)
    ax.set_title("Estadisticas descriptiva(con y sin Outliers)", fontsize=14, pad=20)
    pdf.savefig()
    plt.close
    
    #Pagina 4
    fig, axs = plt.subplots(figsize=(11, 4)) 
    axs.hist(df['Children'], bins=range(df['Children'].min(),df['Children'].max() + 1), edgecolor='black')
    axs.set_title("Children Original")
    axs.set_xlabel("Numero de hijos")
    axs.set_ylabel("Frencuencia")
    pdf.savefig()
    plt.close