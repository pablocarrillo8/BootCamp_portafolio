# Métodos de Validación:
# - Train/Test Split (Hold-out)
# - K-Fold Cross-Validation (Stratified)
# - Leave-One-Out Cross-Validation (LOO)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification
from sklearn.model_selection import (
    LeaveOneOut, StratifiedKFold, train_test_split, cross_val_score
)
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    make_scorer
)




#crear datos simulados

X, y = make_classification(
    n_samples=300,  # Número de muestras
    n_features=5,  # Número de características
    n_informative=4,  # Número de características informativas, contribuyen a la predicción, son como clases
    n_redundant=0,  # Número de características redundantes, son combinaciones lineales de las informativas
    random_state=42,  # Semilla para reproducibilidad
    flip_y=0.02,  # Proporción de muestras de la clase minoritaria
    class_sep=1.0  # Separación entre las clases
)
# X = array de tamaño (300, 50) con las características
# y = array de tamaño (300,) con las etiquetas de clase

model = RandomForestClassifier(
    n_estimators=100,  # Número de árboles en el bosque
    random_state=42,  # Semilla para reproducibilidad
    max_depth=5,  # Profundidad máxima de los árboles
)    

# 2: Diccionar para almacenar resultado
metricas = {
    'accuracy': [], # precisión global del modelo
    'precision': [], # precisión del modelo, proporción de verdaderos positivos sobre el total de positivos predichos
    'recall': [], # exhaustividad del modelo, proporción de verdaderos positivos sobre el total de positivos reales
    'f1_score': [] # puntuación F1 del modelo, media armónica entre precisión y exhaustividad
}
resultado = {m: [] for m in metricas.keys()} # diccionario para almacenar los resultado
nombres = [] # lista para almacenar los nombres de los modelos

# 3: Método train/Test Split(Hold-out)
# Dividir los datos en conjuntos de entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # test_size=0.2 indica que el 20% de los datos se utilizará para pruebas

#Crear y entrenar el modelo regresion lineal
model.fit(X_train, y_train) 


#Predecir el conjunto de pruebas
y_pred = model.predict(X_test) # predecir las etiquetas de clase para el conjunto de prueba

#Almacenar la métrica de evaluación
resultado['accuracy'].append(accuracy_score(y_test, y_pred)) # precisión global del modelo, es util cuando se tiene un conjunto de datos balanceado, la clase esta balanceada
resultado['precision'].append(precision_score(y_test, y_pred)) #Precission Score, mide cuanto elemento predicho como positivo son realmente positivos, Precision = TP / (TP + FP). TP=Verdaderos Positivos, FP=Falsos Positivos
resultado['recall'].append(recall_score(y_test, y_pred)) # Recall Score, mide cuantos elementos positivos fueron correctamente identificados, Recall = TP / (TP + FN)
resultado['f1_score'].append(f1_score(y_test, y_pred)) # F1 Score, es la media armonica entre precision y recall, F1 = 2 * (Precision * Recall) / (Precision + Recall)

# 4: Validación cruzada, Metodo K-Fold
# Realizar validación cruzada con 10 pliegues (k=10)

skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)  # Dividir los datos en 5 pliegues estratificados. StratifiedKFold asegura que cada pliegue tenga la misma proporción de clases que el conjunto completo

#####################################################################################################################
# Nota: Los siguientes comentarios son un ejemplo de cómo se podría implementar la validación cruzada segun copilot / nos quedamos segun el profesor
# Si se desea implementar la validación cruzada, se puede descomentar el siguiente bloque.
#####################################################################################################################
# for train_index, test_index in skf.split(X, y):
#     X_train_cv, X_test_cv = X[train_index], X[test_index]
#     y_train_cv, y_test_cv = y[train_index], y[test_index]
    
#     # Entrenar el modelo
#     model.fit(X_train_cv, y_train_cv)
    
#     # Predecir el conjunto de prueba
#     y_pred_cv = model.predict(X_test_cv)
    
#     # Almacenar las métricas de evaluación
#     resultado['accuracy'].append(accuracy_score(y_test_cv, y_pred_cv))
#     resultado['precision'].append(precision_score(y_test_cv, y_pred_cv))
#     resultado['recall'].append(recall_score(y_test_cv, y_pred_cv))
#     resultado['f1_score'].append(f1_score(y_test_cv, y_pred_cv))
#####################################################################################################################

f1s = cross_val_score(model, X, y, cv=skf, scoring="f1")
accs = cross_val_score(model, X, y, cv=skf, scoring="accuracy")
precs = cross_val_score(model, X, y, cv=skf, scoring="precision")
recs = cross_val_score(model, X, y, cv=skf, scoring="recall")

resultado['accuracy'].append(accs.mean())
resultado['precision'].append(precs.mean())
resultado['recall'].append(recs.mean())
resultado['f1_score'].append(f1s.mean())
nombres.append("Stratified K-Fold")

# 5. Método: Leave-One-Out (LOO)
loo = LeaveOneOut()

f1s = cross_val_score(model, X, y, cv=loo, scoring=make_scorer(f1_score, zero_division=0))
accs = cross_val_score(model, X, y, cv=loo, scoring="accuracy")
precs = cross_val_score(model, X, y, cv=loo, scoring=make_scorer(precision_score, zero_division=0))
recs = cross_val_score(model, X, y, cv=loo, scoring=make_scorer(recall_score, zero_division=0))

resultado['accuracy'].append(accs.mean())
resultado['precision'].append(precs.mean())  # Corrección: "Precission" → "Precision"
resultado['recall'].append(recs.mean())
resultado['f1_score'].append(f1s.mean())
nombres.append("Leave-One-Out")

# 6. Crear DataFrame de resultado
df_resultado = pd.DataFrame(resultado, index=nombres).round(2)
tabla_html = df_resultado.to_html(classes="table table-bordered", border=0) #HTML significa HyperText Markup Language.


# 7. Gráfica comparativa
plt.figure(figsize=(10, 6))
df_melt = df_resultado.reset_index().melt(id_vars="index", var_name="Métrica", value_name="Valor")
sns.barplot(data=df_melt, x="index", y="Valor", hue="Métrica")
plt.xlabel("Método de Validación")
plt.ylabel("Valor promedio de la métrica")
plt.title("Comparación de Métodos de Validación Cruzada")
plt.legend(title="Métricas")
plt.tight_layout()
plt.savefig("grafica_validacion.png")
plt.close()

# # 8. Interpretación dinámica
# interpretaciones = ""
# for i, row in df_resultado.iterrows():
#     interp = f"""
#     <div class="alert alert-info">
#     <h5>{i}</h5>
#     <ul>
#         <li>Accuracy Promedio: {row['Accuracy']:.3f}</li>
#         <li>Precision Promedio: {row['Precision']:.3f}</li>
#         <li>Recall Promedio: {row['Recall']:.3f}</li>
#         <li>F1-score Promedio: {row['F1-score']:.3f}</li>
#     </ul>
#     </div>
#     """
#     interpretaciones += interp
    

# # 9. Dashboard en HTML
# with open("dashboard_validacion_cruzada.html", "w") as f:
#     f.write(f"""
#     <html>
#     <head>
#         <title>Dashboard: Métodos de Validación Cruzada</title>
#         <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css" rel="stylesheet">
#     </head>
#     <body>
#         <div class="container mt-5">
#             <h1>Dashboard de Validación Cruzada</h1>
#             <p>Comparación de 4 métricas para distintos métodos</p>
#             <h2>Tabla de resultado</h2>
#             {tabla_html}
#             <hr>
#             <h2>Gráfica Comparativa</h2>
#             <img src="grafica_validacion.png" class="img-fluid">
#             <hr>
#             <h2>Interpretación Dinámica</h2>
#             {interpretaciones}
#         </div>
#     </body>
#     </html>
#     """)
