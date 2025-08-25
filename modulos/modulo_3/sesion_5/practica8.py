# indexación de listas
import pandas as pd
import numpy as np

df_ventas = pd.read_csv('entradas/ventas_diarias.csv')
df_empleados = pd.read_csv('entradas/empleados_sucursal.csv')
df_productos = pd.read_csv('entradas/productos_categoria.csv')

# 1: examinar los DataFrames
#print("\n == DataFrame original =============")
#print(df_ventas.head(10))

# 2: Indexación Jerarquica (multi-index) del DataFrames
# convetimos tres columnas claves en indice jerarquico : Sucursal, Fecha y Categoria
df_multindex = df_ventas.set_index(['Sucursal', 'Fecha', 'Categoria'], inplace=False) # inplace=False crea una copia del DataFrame original
print("\n == DataFrame con multi-index =============")
print(df_multindex.tail(10))
print(df_multindex.loc['Sur'])  # muestra todas las filas de la sucursal 'Centro'
#print(df_multindex.loc[('Sur', '2024-01-07')])  # muestra todas las filas de la sucursal 'Sur' en la fecha 
print(df_multindex.loc[('Sur', '2024-01-10', 'Electrónica')])  # muestra todas las filas de la sucursal 'Centro' en la fecha '2024-06-01' y categoria 'Bebidas'

# 3 agrupar y agregar
#df_gruped = df_multindex.groupby(['Sucursal', 'Categoria'])['Ventas', 'Unidades'].agg(['sum','mean']).reset_index()


# 4: Transformacion de estructuras con pivot 
# primero agrupamos por fecha y categoria  y asi evitar duplicados
df_grupo =  df_ventas.groupby(['Fecha', 'Categoria'])['Ventas'].sum().reset_index() # # Agrupar por Fecha y Categoria y sumar las Ventas
print("\n == DataFrame agrupado por Fecha y Categoria =============")
print(df_grupo.head(10))
# ahora hacemos un pivot para transformar el DataFrame de categorias (filas) como columnas
df_pivot = df_grupo.pivot(index='Fecha', columns='Categoria', values='Ventas')       # pivotar el DataFrame
print("\n == DataFrame pivotado =============")
print(df_pivot.head(10))

# 5: Caso contrario, desPivot 
df_melted = df_pivot.reset_index().melt(id_vars='Fecha', var_name='Categoria', value_name='Ventas')  # comando melt :
print("\n == DataFrame desPivotado =============")
print(df_melted.head(10))

# 6: concatenacion del DataFrame
df_extra = df_ventas.copy()  # Hacemos una copia del DataFrame original para evitar modificarlo
df_extra['Fecha'] = pd.to_datetime(df_extra['Fecha']) + pd.Timedelta(days=10) # Convertimos la columna Fecha a tipo datetime y le sumamos 10 días
df_extra['Fecha'] = df_extra['Fecha'].dt.strftime('%Y-%m-%d') # Convertimos la columna Fecha de nuevo a string para que coincida con el formato original
# Ahora concatenamos los DataFrames df_ventas y df_extra
df_concat = pd.concat([df_ventas, df_extra], axis=0 )
print("\n 6 : Concatenacion ---")
print(df_concat.head(10))
#df_concat.to_csv("salidas/paso6_concatenado.csv")


# muestra la ayuda de la funcion merge
# 7  :Combinaciones usando merge(joins)
print("-------Merge-------------")
#Inner Join
df_merge_inner = pd.merge(df_ventas, df_productos, on='Categoria', how = 'inner')
print(df_merge_inner.head(10))
df_merge_inner.to_csv("salidas/paso7_merge_inner.csv", index=False)
#Left Join
df_merge_left= pd.merge(df_ventas,df_empleados, on="Sucursal", how='left')
print(df_merge_left.head(10))
df_merge_left.to_csv("salidas/paso7_merge_left.csv")
 #Rigth Join
df_merge_right = pd.merge(df_productos, df_ventas, on="Categoria", how="right")
print(df_merge_right.head(10))
df_merge_right.to_csv("salidas/paso7_merge.csv")
