import os
import pandas as pd

data = {
    "Nombre": ["Juan", "Ana", "Pablo", "María"],
    "Edad": [28, 22, 35, 30],
    "Ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla"]
}

df = pd.DataFrame(data)
print(df)

productos = ["camisa", "pantalón", "zapatos", "chaqueta"]
precios = [20.5, 35.0, 50.0, 80.0]
df2 = pd.DataFrame({
    "Producto": productos,
    "Precio": precios
})
print("\n DataFrame desde listas:")
print(df2)

# Acceso a una columna por nombre o multiples columnas

data2 = {"Nombre": ["Juan", "Ana", "Pablo", "María"],
         "Salario": [3000, 2500, 4000, 3500],
         "departamento": ["Ventas", "Marketing", "IT", "Recursos Humanos"]}
df3 = pd.DataFrame(data2)
print("\n DataFrame desde diccionario:")
print(df3[['Nombre', 'Salario']])  # Acceso a múltiples columnas
print(df3.iloc[3]) # Acceso a una fila por posición
print(df3.iloc[1:3]) # Acceso a un rango de filas (filas 1 y 2, todas las columnas)
# Select a single element
# element = df.iloc[1, 2] # Returns 110 (row 1, column 2)

# # Select a row
# row = df.iloc[0] # Returns the first row

# # Select multiple rows
# rows = df.iloc[0:2] # Returns the first two rows

# # Select a column
# column = df.iloc[:, 0] # Returns the first column

# # Select multiple columns
# columns = df.iloc[:, 0:2] # Returns the first two columns

# # Select specific rows and columns
# subset = df.iloc[[0, 2], [1, 2]] # Returns rows 0 and 2, columns 1 and 2

# # Select rows based on a boolean array
# rows_bool = df.iloc[[True, False, True, False]] # Returns rows 0 and 2

print(df3[(df3['Salario'] > 4000) & (df3['departamento'] == 'IT')]) # Filtrado por condiciones
print(df3[df3['Nombre'].str.startswith('M')]) # Filtrado por nombre que empieza con 'M'
print(df3[df3['Salario'].between(3000, 5000)]) # Filtrado por rango de salario
print(df3[df3['departamento'].isin(['Ventas', "Marketing"])]) 
print(df3.head(2))  # Muestra las primeras 2 filas
print(df3.tail(2))  # Muestra las últimas 2 filas
print(df3.info())  # Información del DataFrame
print(df3.describe())  # Estadísticas descriptivas del DataFrame
print(df3['Salario'].mean())  # Media de la columna 'Salario'
print(df3['Salario'].max())  # Máximo de la columna 'Salario'
print(df3['Salario'].min())  # Mínimo de la columna 'Salario'
print(df3['Salario'].sum())  # Suma de la columna 'Salario'
print(df3['Salario'].count())  # Conteo de la columna 'Salario'
# Accediendo a una columna específica
print(df3['Nombre'].unique())  # Valores únicos en la columna 'Nombre'
print(df3['Nombre'].value_counts())  # Conteo de valores en la columna 'Nombre'
print(df3['Nombre'].nunique)  # Convertir a minúsculas
