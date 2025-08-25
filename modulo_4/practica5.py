"""
Reto: Análisis Visual del Plebiscito Constitucional Chile 2023
Objetivo general:
Explorar la relación entre la participación electoral y
el apoyo a la propuesta constitucional en el plebiscito chileno de 2023,
utilizando visualizaciones estadísticas generadas con Pandas y Seaborn.
"""

# Cada fila represent un resumen de mesa o sección electoral

import pandas as pd
import seaborn as sns
sns.set_theme(style="whitegrid", context="talk")
import matplotlib.pyplot as plt
import numpy as np

# cargar datos
df = pd.read_csv("entrada/plebiscito_chile_2023_400reg.csv")
print("Primeras filas del dataset")
print(df.head(5))

# crear carpeta de salida para graficos
import os # os es una libreria para interactuar con el sistema operativo, esto debido a que no todos los sistemas operativos son iguales
os.makedirs("graficas", exist_ok=True) # exist_ok=True: si la carpeta ya existe, no lanza error, si no existe, la crea

# 1. Visualizar la distribución de la participación electoral
plt.figure(figsize=(9, 5))
sns.histplot(df['percent_favor'], bins=25, kde=True, color='royalblue', edgecolor='black')
plt.title("Distribución dePorcentaje a favor del Plebiscito 2023")
plt.xlabel("Porcentaje de Votantes a Favor (%)")
plt.ylabel("Número de Mesas Electorales, Frecuencia")
plt.tight_layout
plt.savefig("graficas/histograma_porcentaje_favor.png")
#plt.show()

# GRAFICO 2 : Distribución del porcentaje de participación electoral
"""
 El gráfico kdeplot en Seaborn representa una Estimación de Densidad de Núcleo (Kernel Density Estimation, KDE). Es una forma suave de visualizar la distribución de una variable numérica, similar a un histograma pero más continua.

¿Qué significa un KDE plot?
Eje X: Los valores de la variable (en tu caso, percent_turnout, el porcentaje de participación electoral).
Eje Y: La densidad estimada (no es el número de casos, sino una estimación de la probabilidad de encontrar valores en ese rango).
Curva: Muestra dónde se concentran más los datos. Los picos indican valores más frecuentes.
Interpretación de tus datos
Picos altos: Indican rangos de participación electoral donde hubo más mesas electorales.
Valles: Indican rangos menos frecuentes.
Anchura de la curva: Si la curva es ancha, los datos están más dispersos; si es angosta y alta, los datos están más concentrados en ciertos valores.
Ejemplo:
Si ves un pico alrededor del 80% en tu KDE, significa que muchas mesas tuvieron una participación cercana al 80%.

Ventaja sobre el histograma:
El KDE es más suave y permite ver tendencias generales sin depender tanto del tamaño de los bins.
"""

plt.figure(figsize=(9, 5))
sns.kdeplot(df['turnout'], fill=True, color='seagreen', alpha=0.7) 
plt.title("Distribución del Porcentaje de Participación Electoral 2023")
plt.xlabel("Porcentaje de Participación Electoral (%)")
plt.ylabel("Densidad")
plt.tight_layout()
plt.savefig("graficas/kde_porcentaje_participacion.png")
#plt.show()


# 3. Visualizar la relación entre participación electoral y apoyo a la propuesta constitucional
plt.figure(figsize=(9, 5))
sns.regplot(x='turnout',
            y='percent_favor',
            data=df,
            scatter_kws={'alpha':0.5, 'color':'darkorange'}, #Configuración de puntos transparencia y color
            line_kws={'color':'red', 'linewidth':2}, #Configuración de la línea de regresión
        )
plt.title("Relación entre Participación Electoral y Porcentaje a Favor", fontsize=16,pad=15)
plt.xlabel("Participación Electoral (%)", fontsize=14)
plt.ylabel("Porcentaje a Favor (%)", fontsize=14)
plt.tight_layout()
plt.savefig("graficas/regplot_turnout_percent_favor.png")
#plt.show()
"""
La línea roja ascendente en el gráfico sugiere una compensación positiva entre la participación 
electoral y el porcentaje a favor. Esto implica que, a medida que aumenta la participación electoral, tiende a
aumentar también el porcentaje a favor. en cuanto a la disperción diría que si bien exite una 
tendencia gneral hay variabilidad en la relación, (no siempre un aumento en la participación
electoral se traduce en incremento proporcional del % a favor).

"""


# GRAFICO 4: Barplot. Promedio de apoyo por region/rango de participación electoral
#Calculamos el promedio de porcentaje a favor por región
region_avg = (df.groupby('region',as_index=False)).mean(numeric_only=True).sort_values(by='percent_favor', ascending=False)
plt.figure(figsize=(12, 6))
sns.barplot(x='percent_favor', 
            y='region', 
            data=region_avg, 
            edgecolor='black', #Color del borde de las barras
            )
plt.title("Promedio de Porcentaje a Favor por Región", fontsize=16,pad=15)
plt.xlabel("Porcentaje a Favor (%)", fontsize=14)
plt.ylabel("Región", fontsize=14)
plt.tight_layout()
plt.savefig("graficas/barplot_region_percent_favor.png")
#plt.show()

# Gráfico 5: Violinplot - Distribución del porcentaje a favor por región
plt.figure(figsize=(12, 6))
sns.violinplot( x='region',
    y='percent_favor',
    data=df,
    cut=0,
    hue='region',
    palette='pastel',
    inner='quartile',
    legend=False
)


"""
Un violinplot es una gráfica que combina las características de un boxplot y un gráfico
de densidad (como el KDE). Permite visualizar la distribución de una variable numérica
 para diferentes categorías.

¿Cómo se interpreta un violinplot?
Forma de la “viola”: La anchura de la figura en cada punto del eje Y indica la densidad
de los datos en ese valor. Zonas más anchas significan que hay más datos en ese rango.
Línea central y caja interna: Suele mostrar la mediana (línea blanca o negra en el 
centro) y los cuartiles (caja interna), igual que un boxplot. Extremos: Muestran los
valores mínimos y máximos (sin contar outliers si se corta con cut=0).
Comparación entre categorías: Puedes comparar la forma, dispersión y concentración 
de los datos entre diferentes grupos (por ejemplo, regiones).

"""
plt.title("Distribución del Porcentaje a Favor por Región", fontsize=16,pad=15)
plt.xlabel("Región", fontsize=14)
plt.ylabel("Porcentaje a Favor (%)", fontsize=14)
plt.xticks(rotation=45) #Rota las etiquetas del eje x
plt.tight_layout()
plt.savefig("graficas/violinplot_region_percent_favor.png")
#plt.show()


# GRAFICO 6: Triada clave ( % a favor , contra, participacion)
plt.figure(figsize=(10, 6))
sns.pairplot(df,
             vars=['percent_favor', 'percent_against', 'turnout'],
             hue='region', #Colorea por región,
             diag_kind='kde', #Curva KDE en la diagonal,
             height=2.4, 
             corner=True, #Muestra solo la mitad inferior
)

"""
El método pairplot de Seaborn (sns.pairplot) es una herramienta para visualizar
relaciones entre varias variables numéricas de un DataFrame, mostrando todas las
combinaciones posibles de pares de variables.

¿Qué hace un pairplot?
Crea una matriz de gráficos: Cada celda muestra la relación entre dos variables numéricas diferentes (por ejemplo, un scatterplot).
Diagonal: En la diagonal se muestra la distribución de cada variable (por defecto un histograma o un KDE si usas diag_kind='kde').
Colores por categoría: Si usas el parámetro hue, puedes diferenciar los puntos según una variable categórica (por ejemplo, región).
corner=True: Muestra solo la mitad inferior de la matriz, evitando duplicados.
¿Para qué sirve?
Para explorar visualmente correlaciones y patrones entre varias variables numéricas al mismo tiempo.
Para detectar agrupaciones, tendencias, relaciones lineales/no lineales y posibles outliers.

"""

plt.suptitle("Relaciones bivariada clave por Region", fontsize=16, y=1.02)
plt.tight_layout()
plt.savefig("graficas/pairplot_triada_clave.png")
plt.show()


# GRAFICA 7 : FaceGrid

"""
Un FacetGrid en Seaborn es una herramienta para crear múltiples gráficos (subplots)
organizados en una cuadrícula, donde cada gráfico muestra una “faceta” diferente de
los datos según una o más variables categóricas.

¿Para qué sirve?
Permite comparar visualmente la distribución o relación de variables en diferentes
subgrupos de tus datos. Por ejemplo, puedes ver cómo cambia la relación entre dos 
variables según la región, el género, el año, etc.

¿Cómo funciona?
Filas y columnas: Puedes asignar una variable categórica a las filas 
y otra a las columnas, creando así una matriz de gráficos.
Hue: Puedes usar otra variable para diferenciar los datos dentro de cada 
gráfico usando colores. Función de mapeo: Usas .map() o .map_dataframe() 
para dibujar el tipo de gráfico que quieras (histograma, scatterplot, etc.) 
en cada faceta.

import seaborn as sns
g = sns.FacetGrid(df, col="region")
g.map(sns.histplot, "percent_favor")
Un **FacetGrid** en Seaborn es una herramienta para crear múltiples gráficos (subplots) organizados en una cuadrícula, donde cada gráfico muestra una “faceta” diferente de los datos según una o más variables categóricas.

### ¿Para qué sirve?
Permite comparar visualmente la distribución o relación de variables en diferentes subgrupos de tus datos. Por ejemplo, puedes ver cómo cambia la relación entre dos variables según la región, el género, el año, etc.

### ¿Cómo funciona?
- **Filas y columnas:** Puedes asignar una variable categórica a las filas y otra a las columnas, creando así una matriz de gráficos.
- **Hue:** Puedes usar otra variable para diferenciar los datos dentro de cada gráfico usando colores.
- **Función de mapeo:** Usas `.map()` o `.map_dataframe()` para dibujar el tipo de gráfico que quieras (histograma, scatterplot, etc.) en cada faceta.

### Ejemplo básico
___
import seaborn as sns
g = sns.FacetGrid(df, col="region")
g.map(sns.histplot, "percent_favor")
__
Esto crea un histograma de `percent_favor`
para cada región en una columna diferente.

**En resumen:**  
FacetGrid te ayuda a explorar y comparar visualmente patrones en 
subgrupos de tus datos de forma eficiente y ordenada.
"""

#Creamos 4 densidades de participación (bins)
df['turnout_bins'] = pd.cut(df['turnout'],
                            bins=[60, 70, 80, 90, 100],#   Rangos de participación
                            labels=['60-70%', '70-80%', '80-90%', '90-100%'], #Etiquetas de los rangos
)
g = sns.FacetGrid(df, col='turnout_bins', col_wrap=2, height=3.2, sharex=True)# Fuera que  todo lo subgrafico tenga el mismo eje x

g.map_dataframe(
    sns.kdeplot,
    x='percent_favor',
    fill=True,
    clip=(30,70)
    ) #Curva KDE

g.set_titles(col_template="{col_name} participacion") #Título de cada subgráfico
g.fig.subplots_adjust(top=0.9) #Ajusta el espacio superior
g.fig.suptitle("Distribución del Porcentaje a Favor por Rango de Participación", fontsize=16)
g.savefig("graficas/facetgrid_turnout_bins_percent_favor.png")
plt.show()