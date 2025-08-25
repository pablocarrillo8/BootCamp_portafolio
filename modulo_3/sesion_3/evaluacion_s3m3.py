# Actividad evaluada sesión 3 modulo 3.
import pandas as pd
import numpy as np
import zipfile
"""
OBTENCIÓN DE DATOS DESDE ARCHIVOS
Una tienda de tecnología ha registrado sus ventas en un archivo llamado ventas.csv. Cada fila del
archivo representa una venta con las siguientes columnas:

"""
# En BASH:
# echo "ID_venta, Producto, Cantidad, Precio, Total" > ventas.csv
# nano ventas.csv para completar

#1:Cargar el archivo CSV en un DataFrame 

df = pd.read_csv("ventas.csv")

#2:Mostrar las primeras 5 filas del archivo 
print(df.head(5))

#3:Extraer solo las columnas "Producto" y "Precio"
productos_precios = df[["Producto", "Precio"]]
print(productos_precios)

#4: Filtrar los productos cuyo precio sea mayor a 50
productos_mayores_50 = df[df["Precio"] > 50]
print(f"Productos cuyo precio sea mayor a 50:\n", productos_mayores_50)
"""
Aquí, df["Precio"] > 50 crea una serie booleana (True/False) indicando qué filas cumplen la condición.
Luego, df[...] usa esa serie para seleccionar solo las filas donde la condición es True.

"""
#5: Guardar el DataFrame filtrado en un nuevo archivo CSV
dataframe_filtrado = productos_mayores_50.to_csv("ventas_filtrado.csv", index=False)

# guardamos el codigo en un archivo zip
with zipfile.ZipFile('evaluacion_s3m3.zip', 'w') as zipf:
    zipf.write('evaluacion_s3m3.py')
