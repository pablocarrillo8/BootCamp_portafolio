import zipfile
import pandas as pd
import numpy as np
#import zip file as zipfile
"""
ACTIVIDAD SESIÓN AGRUPAMIENTO, PIVOTEO Y COMBINACIÓN DE DATOS
En esta actividad, deberás resolver los siguientes requerimientos, los cuales te permitirán practicar y
consolidar tus conocimientos sobre la manipulación de datos con Pandas. A través de estos
ejercicios, explorarás diferentes técnicas avanzadas para trabajar con indexación jerárquica,
agrupamiento, pivoteo, despivoteo, y combinación de DataFrames.
"""

# 1. Crear un DataFrame con Indexación Jerárquica

datos = {
    'Estudiantes': ['Juan', 'Juan', 'María', 'María'],
    'Materia': ['Matemáticas', 'Historia', 'Matemáticas', 'Historia'],
    'Calificación': [6.5, 5.8, 4.2, 6.0]
}
df = pd.DataFrame(datos)
print("DataFrame Original:")
print(df)
df.set_index(['Estudiantes', 'Materia'], inplace=True)
print("DataFrame con Indexación Jerárquica:")
print(df)

# 2. Acceder a datos con Indexación Jerárquica. Consulta la calificación de María en Historia.
calificacion_maria_historia = df.loc[('María', 'Historia'), 'Calificación']
print("\nCalificación de María en Historia:")
print(calificacion_maria_historia)

# 3. Agrupar y Agregar Datos con groupby. Agrupa el DataFrame por "Materia" y calcula:
# El promedio de calificaciones por materia.
# La calificación más alta por materia.
agrupado = df.groupby('Materia').agg( # agg permite aplicar múltiples funciones de agregación
    Promedio_Calificaciones=('Calificación', 'mean'),
    Calificacion_Maxima=('Calificación', 'max')
).reset_index() # reset_index() para convertir el índice en una columna normal, es decir, para que no se quede como índice jerárquico
print("\nDatos Agrupados por Materia:")
print(agrupado)

# 4. Pivoteo de DataFrame, Convierte el DataFrame para que:
# Las filas representen a los estudiantes
# Las columnas representen las materias
# Los valores sean las calificaciones
df_pivot = df.pivot_table(
    values='Calificación', # Los valores que se van a pivotear, calificaciones.
    index='Estudiantes',   # Las filas representarán a los estudiantes.
    columns='Materia'      # Las columnas representarán las materias.
).reset_index()            # reset_index() para convertir el índice en una columna normal
# Esto permite que las materias se conviertan en columnas y las calificaciones sean los valores

print("\nDataFrame Pivoteado:")
print(df_pivot)


# 5.Despivoteo de DataFrame con melt. Aplica la función melt para transformar el DataFrame pivoteado a su formato largo.
"""(id_vars) Identifica una o más columnas como variables identificadoras  que permanecerán como columnas.
Toma el resto de las columnas (o un subconjunto especificado por value_vars) y las "derrite" en dos nuevas columnas:
 Una columna (variable o var_name) que contendrá los nombres de las columnas originales que se "derretieron".
 Una columna (value o value_name) que contendrá los valores correspondientes de esas columnas originales."""

df_melted = df_pivot.melt(id_vars='Estudiantes', var_name='Materia', value_name='Calificación')
print("\nDataFrame Despivoteado:")
print(df_melted)

# 6. Concatenación y Merge de DataFrames. Crea dos DataFrames:
# df1 con las columnas "ID_Estudiante", "Estudiante", "Carrera"
# df2 con las columnas "ID_Estudiante", "Materia", "Calificación"
# Concatena ambos DataFrames a lo largo del eje de filas.
# Luego, realiza un merge de ambos DataFrames basado en la columna "ID_Estudiante".
df1 = pd.DataFrame({
    'ID_Estudiante': [1, 2],
    'Estudiante': ['Juan', 'María'],
    'Carrera': ['Ingeniería', 'Medicina']
})
df2 = pd.DataFrame({
    'ID_Estudiante': [1, 2],
    'Materia': ['Matemáticas', 'Historia'],
    'Calificación': [6.5, 5.8]
})
df_concat = pd.concat([df1, df2], axis=0, ignore_index=True) # AXIS=0 para concatenar filas, ignore_index=True para reindexar el DataFrame resultante, si false, se mantendrán los índices originales
print("\nDataFrame Concatenado:")
print(df_concat)
df_merged = pd.merge(df1, df2, on='ID_Estudiante', how='inner') # how='inner' para hacer un merge interno
print("\nDataFrame Mergeado:")
print(df_merged)

# guardamos el codigo en un archivo zip
with zipfile.ZipFile('evaluacion_s5m3.zip', 'w') as zipf:
    zipf.write('evaluacion_s5m3.py')