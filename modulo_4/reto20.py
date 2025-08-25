# Reto número 20.

"""
🧩 Reto 6 – “¿Dinero compra votos?”
Archivo: campaign_finance_elections.csv

Tema: Financiamiento de campañas y resultados electorales

Descripción:
Este reto pone a prueba la hipótesis de que mayores recursos de campaña se
traducen en más votos. También considera si los candidatos incumbentes
tienen ventaja adicional.
Objetivos:
• Visualizar la relación entre campaign_spending_musd y votes_received_pct.
• Comparar patrones de gasto y resultados por party.
• Analizar el efecto de la incumbencia (incumbent) en el desempeño
electoral.
Visualizaciones recomendadas:
jointplot, regplot, violinplot por partido, barplot por región, FacetGrid por
condición de incumbente.

"""
import pandas as pd
import seaborn as sns
sns.set_theme(style="whitegrid", context="talk") #
import matplotlib.pyplot as plt
import numpy as np
import os

# cargar datos
df = pd.read_csv("entrada/campaign_finance_elections.csv")
print("Primeras filas del dataset")
print(df.head())
print("Informacion del dataframe")
print(df.info())
print("Valor faltantes por columna")
print(df.isnull().sum())

# 2: Visualizar la relación entre campaign_spending_musd y votes_received_pct.

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
plt.show()