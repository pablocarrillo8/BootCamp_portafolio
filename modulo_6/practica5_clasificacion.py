import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
######################
# Conexion a la base de dades SQLite y carga de datos
######################

"""
# Load the Iris dataset
iris = load_iris()

# The 'iris' object now contains the dataset and its attributes
# For example, to access the data (features) and target labels:
X = iris.data
y = iris.target

# You can also access other attributes like feature names, target names, and a description:
feature_names = iris.feature_names
target_names = iris.target_names
description = iris.DESCR


The iris object provides various attributes:

    data: The feature matrix (X), where each row is a sample and each column is a feature.
    target: The target vector (y), representing the class labels for each sample.
    feature_names: A list of strings describing the names of the features.
    target_names: A list of strings describing the names of the target classes.
    DESCR: A string containing a detailed description of the dataset

"""

def cargar_datos():
    iris = load_iris()
    # Convertir a DataFrame
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    # conectar a la base de datos SQLite
    conn = sqlite3.connect('iris.db') # crea la base de datos si no existe
    # guardar el DataFrame en la base de datos
    df.to_sql('iris_data', conn, if_exists='replace', index=False) # if_exists='replace' reemplaza la tabla si ya existe, index=False evita que se guarde el índice del DataFrame
    #conn.close()
    # Consultar los datos /cargar los datos desde la base de datos
    #df = pd.read_sql_query("SELECT * FROM iris_data", conn)
    query = "SELECT * FROM iris_data"
    data = pd.read_sql_query(query, conn)
    conn.close()
    return data # retorna el DataFrame con los datos del iris

    #Preparar los datos
def preparar_datos(data):
    # separar las características y la variable objetivo
    X = data.drop('target', axis=1)  # Eliminar la columna 'target' para obtener las características, separamos características
    y = data['target']  # La columna 'target' es la variable objetivo, la separamos
    return X, y

# Dividir los datos en conjuntos de entrenamiento y prueba
def dividir_datos(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def graficar_matriz_confusion(y_test, y_predicciones):
    cm = confusion_matrix(y_test, y_predicciones)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=iris.target_names, yticklabels=iris.target_names)
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix -' + nombre_modelo)
    plt.show()

# Modelo de regresión logística    
def modelo_regresion_logistica(X_train, y_train, X_test, y_test):
    modelo = LogisticRegression(max_iter=200)
    # Entrenar el modelo con los datos de entrenamiento
    modelo.fit(X_train, y_train)
    # Realizar predicciones con los datos de prueba
    y_predicciones = modelo.predict(X_test)
    return modelo, y_predicciones
    # Graficar matriz de confusión
    graficar_matriz_confusion(y_test, y_predicciones, nombre_modelo='Regresión Logística') 
    return modelo, y_predicciones, accuracy_score(y_test, y_predicciones)

# Modelo de árbol de decisión
def modelo_arbol_decision(X_train, y_train, X_test, y_test):