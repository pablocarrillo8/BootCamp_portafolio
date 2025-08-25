import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# --- 1. Identificar los Parámetros de Entrada ---
# Tamaño de cada muestra (número de días en cada simulación)
sample_size = 30

# Número total de simulaciones
num_simulations = 1000

# Parámetros de la población (temperatura promedio diaria)
population_mean = 25  # °C
population_std_dev = 3  # °C

# Lista para almacenar las medias de cada muestra
sample_means = []

# --- 2. Simular las Medias Muestrales ---
for _ in range(num_simulations):
    # Generar una muestra de temperaturas de 30 días
    # Usamos una distribución normal con la media y desviación estándar de la población
    daily_temperatures = np.random.normal(loc=population_mean, scale=population_std_dev, size=sample_size)

    # Calcular la media de esta muestra
    current_sample_mean = np.mean(daily_temperatures)

    # Almacenar la media de la muestra
    sample_means.append(current_sample_mean)

# Convertir la lista a un array de NumPy para facilitar cálculos posteriores
sample_means = np.array(sample_means)

# --- 3. Calcular Estadísticos Clave ---
# Media de las medias muestrales
mean_of_sample_means = np.mean(sample_means)

# Desviación estándar de las medias muestrales (Error Estándar Empírico)
std_dev_of_sample_means = np.std(sample_means)

# Error Estándar Teórico según el TLC
theoretical_standard_error = population_std_dev / np.sqrt(sample_size)

print(f"--- Resultados de los Estadísticos ---")
print(f"Media de las medias muestrales (Empírica): {mean_of_sample_means:.2f}°C")
print(f"Desviación estándar de las medias muestrales (Empírica): {std_dev_of_sample_means:.2f}°C")
print(f"Error Estándar Teórico (según TLC): {theoretical_standard_error:.2f}°C")

# --- 4. Interpretar en el Contexto del Teorema del Límite Central (TLC) ---
print(f"\n--- Interpretación del Teorema del Límite Central ---")
print(f"Observación de la Media:")
print(f"La media de las medias muestrales ({mean_of_sample_means:.2f}°C) es muy cercana a la media poblacional original ({population_mean}°C).")
print(f"Esto es consistente con el TLC, que establece que la media de la distribución de las medias muestrales tiende a ser igual a la media de la población.")

print(f"\nObservación de la Desviación Estándar (Error Estándar):")
print(f"La desviación estándar de las medias muestrales ({std_dev_of_sample_means:.2f}°C) es cercana al Error Estándar Teórico ({theoretical_standard_error:.2f}°C) predicho por el TLC.")
print(f"El TLC nos dice que la dispersión de las medias muestrales se reduce a medida que el tamaño de la muestra aumenta.")

print(f"\nConclusión sobre el TLC:")
print(f"Dado que la distribución de las medias muestrales se centra alrededor de la media poblacional y su desviación estándar se aproxima al error estándar teórico, podemos concluir que el Teorema del Límite Central se verifica en esta simulación.")
print(f"La forma de la distribución (que veremos en el histograma) también debería ser aproximadamente normal, lo cual es otro pilar del TLC para tamaños de muestra suficientemente grandes.")


# --- 5. Generar una Visualización (Histograma) ---
plt.figure(figsize=(10, 6))
plt.hist(sample_means, bins=30, density=True, alpha=0.7, color='skyblue', edgecolor='black', label='Histograma de Medias Muestrales')

# Superponer una curva de densidad de probabilidad normal
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, mean_of_sample_means, std_dev_of_sample_means)
plt.plot(x, p, 'k', linewidth=2, label=f'Curva Normal (Media={mean_of_sample_means:.2f}, DE={std_dev_of_sample_means:.2f})')

plt.title('Distribución de las Medias Muestrales de Temperaturas Diarias')
plt.xlabel('Media de Temperatura (°C)')
plt.ylabel('Densidad de Frecuencia')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.axvline(population_mean, color='red', linestyle='dashed', linewidth=1.5, label=f'Media Poblacional ({population_mean}°C)')
plt.legend()
plt.show()