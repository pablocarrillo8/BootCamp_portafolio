#Ejercicio Integrador 2: Revisión de Desempeño de Empleados

import pandas as pd 

data = { 'Nombre': ['Alicia', 'Bruno', 'Carlos', 'David'],
		 'Departamento': ['Ventas', 'Marketing', 'TI', 'Ventas'],
		 'Puntaje': [85, 90, 75, 88],
		 'Calificación': ['A', 'A', 'B', 'A'] }


df = pd.DataFrame(data, index=['E001', 'E002', 'E003', 'E004'])
print("DataFrame de Empleados:")
print(df)
print("\nAltos Desempeños en Ventas/Marketing:")
print(df[df['Puntaje'].between(80, 90)]) # Filtrado por rango de salario
print(df[(df['Puntaje'] > 80)])
#Calcular el puntaje promedio por departamento e identificar calificaciones únicas de desempeño
print("\nPuntaje promedio por departamento:")
print(df.groupby('Departamento')['Puntaje'].mean()) #groupby para calcular el promedio
print("\nCalificaciones únicas de desempeño:")  
print(df['Calificación'].unique())  # Calificaciones únicas