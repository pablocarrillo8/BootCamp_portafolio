# reto 19: practica regresion lineal

#1 importar librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import  LinearRegression
from sklearn.metrics import mean_squared_error ,mean_absolute_error,r2_score

# 1: Carga el cojunto de datos usando pandas
df = pd.read_csv("entrada/science_data_1.csv")
print("Primeras filas dataset")
#print(df.head(5))

# 2: Para cada especie, calcular el coeficiente de correlación de Pearson entre niveles_co2y crecimiento_planta

species_groups = df.groupby('especie') # agrupar por especie
print("Grupos de especies:" + str(species_groups.groups.keys()))
correlations = {}
for especies, group in species_groups: # group es un DataFrame con los datos de cada especie
    correlation = group['niveles_co2'].corr(group['crecimiento_planta'])
    correlations[especies] = correlation
    print(f"Correlación de Pearson para {especies}: {correlation:.3f}")

# 3: Para cada especie, implementar una regresión lineal simple con niveles_co2como predictor y crecimiento_plantacomo variable dependiente.

for species, group in species_groups:
    print(f"\nProcesando especie: {species}")
    X = group[['niveles_co2']]  # matriz de características (n,1)
    y = group['crecimiento_planta']  # vector objetivo (n,)
    
    model = LinearRegression()
    model.fit(X, y)

    # 4: Imprimir el intercepto y la pendiente del modelo para cada especie.
    print(f"Especie: {species}")
    print(f"Intercepto (β0): {model.intercept_:.3f}") # instercepto : es el valor de y cuando x=0
    print(f"Pendiente (β1): {model.coef_[0]:.3f}") # pendiente : es el cambio en y por cada unidad de cambio en x

    # 5: Crear tres gráficos de dispersión (uno por especie) mostrando niveles_co2 versus crecimiento_planta con la línea de regresión.
    plt.scatter(group['niveles_co2'], group['crecimiento_planta'], label=f"{species} - Datos", alpha=0.5)
    y_pred = model.predict(X) # predicciones del modelo: esto es lo que el modelo predice para cada valor de x
    plt.plot(group['niveles_co2'], y_pred, color='red', label=f"{species} - Línea de Regresión")
    plt.title(f"Regresión Lineal para {species}")
    plt.xlabel("Niveles de CO2 (ppm)")
    plt.ylabel("Crecimiento de la Planta (cm)")
    plt.legend()
    plt.grid(True)
    #plt.show()

# 6: Evaluar el rendimiento  del modelo, calcular MSE, MAE y R² para cada modelo. 
mse = mean_squared_error(y, y_pred) # Error cuadrático medio: mide la media de los errores al cuadrado, sirve para evaluar la precisión del modelo
mae = mean_absolute_error(y, y_pred) # Error absoluto medio: mide la media de los errores absolutos, sirve para evaluar la precisión del modelo
r2 = r2_score(y, y_pred) # Coeficiente de determinación: mide la proporción de la varianza en la variable dependiente que es predecible a partir de la variable independiente

print("\Evaluacion del Modelo")
print(f"Error Cuadratico Medio (MSE): {mse:.2f}")
print(f"Error Absoluto Medio (MAE){mae:.2f}")
print(f"coeficiente de Determinacion (R2):{r2:.3f} ")

# 7: Interpretar las diferencias en los coeficientes de correlación y R², y discutir si una correlación fuerte implica causalidad.