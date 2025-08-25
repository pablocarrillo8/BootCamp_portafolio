# funcion que analiza las amplitudes de una traza sismica

import statistics as stats

def analizar_sismico(amplitudes):
    # Validar que la lista no esté vacía
    if len(amplitudes) == 0:
        raise ValueError("La lista de amplitudes no puede estar vacía.")

    # Calcular la media y desviación estándar
    media = stats.mean(amplitudes)
    desviacion = stats.stdev(amplitudes)

    # Identificar amplitudes anómalas (fuera de media ± 2 * desviación estándar)
    limite_inferior = media - 2 * desviacion
    limite_superior = media + 2 * desviacion
    anomalías = [a for a in amplitudes if a < limite_inferior or a > limite_superior]

    # Retornar el diccionario con los resultados
    return {
        "media": round(media, 2),
        "desviacion": round(desviacion, 2),
        "anomalías": len(anomalías)
    }

amplitudes_1 = [2.2, 1.1, 0.2, 0.98, 3.0, 1.8, 1.5, 2.3]
salida_1 = analizar_sismico(amplitudes_1)
print(f"el cálculo de la función de amplitudes_1 da los siguientes resultados: ", "\n", salida_1)

amplitudes_2 = []
salida_2 = analizar_sismico(amplitudes_2)
print(salida_2)