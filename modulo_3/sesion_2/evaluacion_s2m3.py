# Actividad evaluada sesion 2 modulo 3
import zipfile  
"""
Eres un analista de datos en un club de fútbol que busca mejorar el rendimiento de los jugadores. Te
han proporcionado un archivo con datos sobre los futbolistas del equipo, incluyendo su nombre,
posición, edad, goles y asistencias en la última temporada. Tu tarea es analizar estos datos usando
Pandas para responder preguntas clave

"""

# Importar las librerías necesarias
import pandas as pd
import numpy as np

# 1 : crea un DataFrame con los siguientes datos
data = {
    'Nombre': ['Lionel Messi', 'Cristiano Ronaldo', 'Kevin de Bruyne', 'Kylian Mbappé', 'Luka Modric'],
    'Posición': ['Delantero', 'Delantero', 'Mediocampista', 'Delantero', 'Mediocampista'],
    'Edad': [35, 38, 31, 24, 37],
    'Goles': [20, 18, 8, 25, 3],
    'Asistencias': [10, 5, 15, 12, 8]
}

df = pd.DataFrame(data) 

#2: Selecciona una columna y muestra los nombres de todos los jugadores
print("Nombres de los jugadores:\n", df['Nombre'].to_list())

#3: Filtra jugadores con más de 10 goles y muestra solo su nombre y cantidad de goles
for Nombre, Goles in zip(df['Nombre'], df['Goles']):
    if Goles > 10:
        print(f"\n{Nombre} - {Goles} goles")

# 4: grega una nueva columna al DataFrame llamada Puntos, donde cada jugador obtiene Puntos = (Goles * 4) + (Asistencias * 2)
df['Puntos'] = (df['Goles'] * 4) + (df['Asistencias'] * 2)
print("\nDataFrame con la nueva columna Puntos:\n", df)

#5: Calcula el promedio de goles de todos los jugadores 
promedio_goles = df['Goles'].mean()
print("\nPromedio de goles de todos los jugadores:", promedio_goles)

#6 Obtén el máximo y mínimo de asistencias en el equipo
max_asistencias = df['Asistencias'].max()
min_asistencias = df['Asistencias'].min()
print("\nMáximo de asistencias:", max_asistencias)
print("Mínimo de asistencias:", min_asistencias)

#7: Cuenta cuántos jugadores hay por posición (Delantero, Mediocampista)
posicion_counts = df['Posición'].value_counts()
print("\nCantidad de jugadores por posición:\n", posicion_counts)

#8: Ordena el DataFrame en función de los goles en orden descendente
df_sorted = df.sort_values(by='Goles', ascending=False)
print("\nDataFrame ordenado por goles en orden descendente:\n", df_sorted)

# guardamos el codigo en un archivo zip
with zipfile.ZipFile('evaluacion_s2m3.zip', 'w') as zipf:
    zipf.write('evaluacion_s2m3.py')