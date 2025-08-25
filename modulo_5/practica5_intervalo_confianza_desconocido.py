# Calcular el intervalo de confianza del 95% para 30 rocas
# con media 10 Kg. y σ = 1.5 Kg.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

# Datos
n = 30 # Tamaño de la muestra
mean_sample = 10 # Media de la muestra
std_pop = 1.5 # Desviación estándar poblacional
#z_critical = stats.norm.ppf(0.975) # Valor crítico para un IC del 95%
gl = n - 1 # Grados de libertad
confianza = 0.95 # Nivel de confianza
z_critical = stats.t.ppf((1 + confianza) / 2, gl)  # Valor crítico para un IC del 95% usando la distribución t
# stats.t.ppf es usado para muestras pequeñas o cuando la desviación estándar poblacional es desconocida
# Cálculo del margen de error
margin_error = z_critical * (std_pop / np.sqrt(n))
# Cálculo del intervalo de confianza
ci = (mean_sample - margin_error, mean_sample + margin_error)
print(f"Intervalo de confianza del 95%: {ci}")

#visualización
data = pd.DataFrame({'peso': np.random.normal(mean_sample, std_pop, n)})  # peso de las rocas
sns.histplot(data['peso'], kde=True) # sns.histplot(data=data, x='peso', kde=True para mostrar la densidad)
plt.axvline(ci[0], color='red', linestyle='--', label=f'Limite inferior IC: {ci[0]:.2f}') # Línea del límite inferior del IC
plt.axvline(ci[1], color='green', linestyle='--', label=f'Limite superior IC: {ci[1]:.2f}') # Línea del límite superior del IC
plt.axvline(mean_sample, color='blue', linestyle='-', label=f'Media muestral: {mean_sample:.2f}') # Línea de la media muestral
# Añadir etiquetas y título
plt.legend()
plt.title('Distribución de pesos de las rocas con intervalo de confianza')
plt.xlabel('Peso (kg)')
plt.ylabel('Frecuencia')
plt.savefig('graficas/desconocido.png')
plt.show()