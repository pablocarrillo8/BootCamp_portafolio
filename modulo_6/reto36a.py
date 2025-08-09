#   Importar librerías
 
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
 
 
#   Simular dataset de muestras de agua
 
np.random.seed(42)
df = pd.DataFrame({
    'muestra_id': range(1, 11),
    'fuente': np.random.choice(['río', 'pozo', 'lluvia', 'canal'], size=10),
    'tipo_contaminante': np.random.choice(['orgánico', 'metálico', 'biológico'], size=10),
    'nivel_contaminación': np.random.uniform(0.1, 1.0, size=10),
    'zona': np.random.choice(['urbana', 'rural'], size=10)
})
 
print("Dataset original:")
print(df)
 
 
#  1. Aplicar Label Encoding a tipo_contaminante
# ===============================
#  Para modelos que aceptan codificación ordinal (aunque esta variable es nominal)
le_contaminante = LabelEncoder()
df['contaminante_encoded'] = le_contaminante.fit_transform(df['tipo_contaminante'])
 
print("\n Dataset con Label Encoding:")
print(df[['muestra_id', 'tipo_contaminante', 'contaminante_encoded']])
 
 
#  2. Aplicar One-Hot Encoding a fuente y zona
# ===============================
#  Evita orden artificial, útil para clasificación con modelos lineales
columnas = ['fuente', 'zona']
encoder = OneHotEncoder(sparse_output=False, drop=None)
 
transformador = ColumnTransformer(
    transformers=[('onehot', encoder, columnas)],
    remainder='passthrough'
)
 
datos_transformados = transformador.fit_transform(df)
columnas_onehot = transformador.get_feature_names_out()
df_onehot = pd.DataFrame(datos_transformados, columns=columnas_onehot)
 
print("\n Dataset con One-Hot Encoding:")
print(df_onehot)
 
 
#  3. Crear variables dummy con pandas.get_dummies()
# ===============================
df_dummies = pd.get_dummies(df, columns=['fuente', 'zona'], drop_first=False)
 
print("\n Dataset con Variables Dummies:")
print(df_dummies)
 
 
#  4. Comparación y recomendaciones para modelos lineales
# ===============================
print("\n Comparación de formas codificadas:")
print(f" Original: {df.shape}")
print(f" Label Encoding: {df[['contaminante_encoded']].shape}")
print(f" One Hot Encoding: {df_onehot.shape}")
print(f" Variables Dummies: {df_dummies.shape}")
 
"""
 Recomendación:
 Para modelos lineales (regresión logística, regresión lineal, SVM):
   - Usar One-Hot Encoding o Dummies para evitar interpretación de orden numérico artificial.
 Label Encoding solo si la variable representa un orden real (no aplicable en este caso).
"""