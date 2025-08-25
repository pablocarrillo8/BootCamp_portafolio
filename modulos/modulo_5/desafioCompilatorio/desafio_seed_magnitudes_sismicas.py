import os
import sys  

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

"""
RETO INTEGRADOR : 🌍 Proyecto 3: Geofísica - Magnitud de sismos 
Contexto: Comparar la magnitud media reciente con el histórico (3.5), sabiendo
que σ = 0.3
🧭 Pasos a seguir:
1. Cargar los datos de magnitudes en un DataFrame.
2. Calcular:
    o Media muestral
    o Error estándar usando σ = 0.3
3. Formular hipótesis:
    o H₀: μ ≤ 3.5
    o H₁: μ > 3.5
4. Calcular estadístico Z (como σ es conocida).
5. Calcular:
    o Intervalo de confianza al 95%
    o Valor p
    o Tamaño muestral para detectar diferencia de 0.2
6. Visualizar:
    o Histograma de magnitudes
    o Curva normal con la zona crítica marcada
7.  ¿Se rechaza H₀ con el valor p obtenido?
    ¿Qué significa ese resultado en el contexto del problema?
    ¿La diferencia es significativa o atribuible al azar?
"""

# --- 1. Cargar los datos de magnitudes en un DataFrame ---
# Vamos a simular algunos datos de magnitudes.
# En un caso real, cargarías un archivo CSV, Excel, etc.
np.random.seed(42) # Para reproducibilidad
# Simulamos una muestra de 50 sismos con una media ligeramente superior a 3.5
# para ver si nuestra prueba detecta la diferencia.
magnitudes = np.random.normal(loc=3.7, scale=0.3, size=50)
df = pd.DataFrame({'magnitud': magnitudes})

print("--- Datos Cargados ---")
print(df.head())
print(f"Número de sismos en la muestra: {len(df)}")
print("-------------------------------")

# --- 2. Calcular la Media muestral y el Error estándar ---
media_muestral = df['magnitud'].mean()
sigma_poblacional = 0.3 # Desviación estándar poblacional conocida
n = len(df)
error_estandar = sigma_poblacional / np.sqrt(n)

print(f"Media muestral de magnitudes: {media_muestral:.4f}")
print(f"Error estándar (usando σ = {sigma_poblacional}): {error_estandar:.4f}")
print("-------------------------------")

# --- 3. Formular hipótesis ---
# H₀: μ ≤ 3.5 (La magnitud media reciente es menor o igual a 3.5)
# H₁: μ > 3.5 (La magnitud media reciente es mayor que 3.5)
mu_historica = 3.5
print(f"Hipótesis Nula (H₀): μ <= {mu_historica}")
print(f"Hipótesis Alternativa (H₁): μ > {mu_historica}")
print("-------------------------------")

# --- 4. Calcular estadístico Z (como σ es conocida) ---
z_estadistico = (media_muestral - mu_historica) / error_estandar # z-score es utilizado para comparar la media muestral con la media poblacional bajo H₀
print(f"Estadístico Z: {z_estadistico:.4f}")
print("-------------------------------")
# --- 5. Calcular: Intervalo de confianza al 95%, Valor p, Tamaño muestral ---

# Nivel de confianza
confianza = 0.95
alfa = 1 - confianza # Nivel de significancia

# Para un IC del 95%, el valor crítico Z es z_alpha/2
# Sin embargo, para una prueba de una cola (H1: mu > 3.5), el IC se interpreta un poco diferente.
# Pero el ejercicio pide el IC del 95% general.
# Para un IC bilateral del 95%, z_critico es 1.96
z_critico_ic = stats.norm.ppf(1 - (alfa / 2)) # Z-score para el 95% IC bilateral (aprox 1.96)

# Intervalo de confianza al 95%
limite_inferior_ic = media_muestral - z_critico_ic * error_estandar
limite_superior_ic = media_muestral + z_critico_ic * error_estandar

print(f"Intervalo de Confianza al {confianza*100}%:")
print(f"  [{limite_inferior_ic:.4f}, {limite_superior_ic:.4f}]")

# Valor p (para una prueba de cola superior)
# p-value = P(Z > z_estadistico | H0 es verdadera)
valor_p = 1 - stats.norm.cdf(z_estadistico)

print(f"Valor p (prueba de cola superior): {valor_p:.4f}")

# Tamaño muestral para detectar diferencia de 0.2
# Fórmula para el tamaño muestral (para una cola, con potencia del 80% y alfa del 5%)
# n = ((Z_alpha + Z_beta) * sigma / delta)^2
# Z_alpha para alfa = 0.05 (una cola)
z_alpha_una_cola = stats.norm.ppf(1 - alfa) # Para 0.05 es aprox 1.645
# Z_beta para beta = 0.2 (potencia del 80%)
z_beta = stats.norm.ppf(0.80) # Para 0.80 es aprox 0.84
delta = 0.2 # Diferencia a detectar

tamaño_muestral_necesario = ((z_alpha_una_cola + z_beta) * sigma_poblacional / delta)**2
tamaño_muestral_necesario = np.ceil(tamaño_muestral_necesario).astype(int) # Redondear hacia arriba, esto para asegurar que tenemos un número entero de sismos

print(f"Tamaño muestral necesario para detectar una diferencia de {delta} con 80% de potencia (α=0.05): {tamaño_muestral_necesario} sismos")
print("-------------------------------")

# --- 6. Visualizar: Histograma de magnitudes y Curva normal con zona crítica ---

plt.figure(figsize=(12, 6))

# Histograma de magnitudes
plt.subplot(1, 2, 1)
sns.histplot(df['magnitud'], kde=True, bins=7)
plt.axvline(media_muestral, color='red', linestyle='dashed', linewidth=2, label=f'Media Muestral: {media_muestral:.2f}')
plt.title('Distribución de Magnitudes Recientes')
plt.xlabel('Magnitud')
plt.ylabel('Frecuencia')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# Curva normal con la zona crítica marcada
plt.subplot(1, 2, 2)
x = np.linspace(mu_historica - 3 * sigma_poblacional / np.sqrt(n), mu_historica + 3 * sigma_poblacional / np.sqrt(n), 100)
y = stats.norm.pdf(x, loc=mu_historica, scale=sigma_poblacional / np.sqrt(n))
plt.plot(x, y, color='blue', label='Distribución bajo H₀')

# Marcar la media muestral
plt.axvline(media_muestral, color='red', linestyle='dashed', linewidth=2, label=f'Media Muestral: {media_muestral:.2f}')

# Marcar la zona crítica (z-crítico para alfa = 0.05 en una cola)
z_critico_una_cola = stats.norm.ppf(1 - alfa) # approx 1.645
valor_critico_magnitud = mu_historica + z_critico_una_cola * error_estandar
plt.axvline(valor_critico_magnitud, color='green', linestyle='dotted', linewidth=2, label=f'Valor Crítico (Z={z_critico_una_cola:.2f})')

# Rellenar la zona crítica
x_critical = np.linspace(valor_critico_magnitud, mu_historica + 3 * sigma_poblacional / np.sqrt(n), 100)
y_critical = stats.norm.pdf(x_critical, loc=mu_historica, scale=sigma_poblacional / np.sqrt(n))
plt.fill_between(x_critical, 0, y_critical, color='green', alpha=0.3, label='Zona de Rechazo de H₀')

plt.title('Distribución Muestral de la Media bajo H₀')
plt.xlabel('Magnitud Media')
plt.ylabel('Densidad de Probabilidad')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# --- 7. ¿Se rechaza H₀ con el valor p obtenido? ¿Qué significa ese resultado en el contexto del problema? ¿La diferencia es significativa o atribuible al azar? ---

print("-------------------------------")
print("--- Conclusiones ---")
nivel_significancia = 0.05 # Usamos un alfa común del 5%

if valor_p < nivel_significancia:
    print(f"Dado que el valor p ({valor_p:.4f}) es menor que el nivel de significancia ({nivel_significancia}),")
    print("se RECHAZA la Hipótesis Nula (H₀).")
    print("\n¿Qué significa este resultado en el contexto del problema?")
    print(f"Esto significa que hay evidencia estadística suficiente para concluir que la magnitud media reciente de los sismos")
    print(f"es SIGNIFICATIVAMENTE MAYOR que la magnitud histórica de {mu_historica}.")
    print("\n¿La diferencia es significativa o atribuible al azar?")
    print("La diferencia observada es estadísticamente SIGNIFICATIVA y no parece ser atribuible al azar.")
    print("Esto sugiere un cambio real en la actividad sísmica de la región, donde los sismos recientes son, en promedio, más fuertes.")
else:
    print(f"Dado que el valor p ({valor_p:.4f}) es mayor o igual que el nivel de significancia ({nivel_significancia}),")
    print("NO se RECHAZA la Hipótesis Nula (H₀).")
    print("\n¿Qué significa este resultado en el contexto del problema?")
    print(f"Esto significa que no hay evidencia estadística suficiente para concluir que la magnitud media reciente de los sismos")
    print(f"es significativamente mayor que la magnitud histórica de {mu_historica}.")
    print("\n¿La diferencia es significativa o atribuible al azar?")
    print("La diferencia observada podría ser atribuible al azar. No podemos concluir que haya un aumento real en la magnitud media.")

print("-------------------------------")