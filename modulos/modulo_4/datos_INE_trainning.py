# datos INE: Temperatura maxima absoluta mensual
import pandas as pd
import seaborn as sns
sns.set_theme(style="whitegrid", context="talk") #
import matplotlib.pyplot as plt
import numpy as np
import os

#load
df = pd.read_csv("temperatura_años.csv")
print("Dataframe extension", len(df))
print("\n Informacion")
print(df.describe())
print("\n Primeros 10 datos")
print(df.head(10))
print("ultimos 10 datos")
print(df.tail())
print("n\ Datos faltantes o nulos")
print(df.notnull().sum()) # 