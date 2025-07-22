# -*- coding: utf-8 -*-
"""Notas_Estudiantes_Random Forest y Gradient Boosting.ipynb
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Cargar CSV
df = pd.read_csv('datos_estudiantes.csv')

# Variables
X = df.drop('nota_semestre', axis=1)
y = df['nota_semestre']

# Separar en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf = RandomForestRegressor(random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

gb = GradientBoostingRegressor(random_state=42)
gb.fit(X_train, y_train)
y_pred_gb = gb.predict(X_test)

import joblib

# Usar los nombres correctos
joblib.dump(rf, 'modelo_random_forest.pkl')
joblib.dump(gb, 'modelo_gradient_boosting.pkl')

from sklearn.metrics import (
    mean_absolute_error, mean_squared_error, r2_score,
    median_absolute_error
)
import numpy as np

def smape(y_true, y_pred):
    denominator = (np.abs(y_true) + np.abs(y_pred)) / 2
    diff = np.abs(y_pred - y_true) / np.maximum(denominator, 1e-8)
    return np.mean(diff) * 100

def evaluar_regresion(y_true, y_pred, nombre_modelo):
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred)
    medae = median_absolute_error(y_true, y_pred)
    smape_score = smape(y_true, y_pred)

    print(f"📊 {nombre_modelo} (Regresión)")
    print(f"🔹 MAE:    {mae:.2f}")
    print(f"🔹 RMSE:   {rmse:.2f}")
    print(f"🔹 MedAE:  {medae:.2f}")
    print(f"🔹 SMAPE:  {smape_score:.2f}%")
    print(f"🔹 R²:     {r2:.2f}")
    print("")

# Ejemplo:
evaluar_regresion(y_test, y_pred_rf, "Random Forest")
evaluar_regresion(y_test, y_pred_gb, "Gradient Boosting")

import joblib
import numpy as np
import pandas as pd

# Cargar los modelos entrenados
modelo_rf = joblib.load('modelo_random_forest.pkl')
modelo_gb = joblib.load('modelo_gradient_boosting.pkl')

# Orden de las columnas según tu dataset
columnas = [
    "anio_ingreso_universidad", "sexo", "edad", "anio_egreso_secundaria", "semestre_actual",
    "beca_rendimiento", "transporte_universidad", "horas_estudio_dia", "frecuencia_estudio_dia",
    "modalidad_aprendizaje", "smartphone", "computadora_personal", "horas_redes_sociales",
    "nivel_ingles", "asistencia_promedio", "riesgo_academico", "suspension_academica",
    "tutorias_docentes", "habilidades", "horas_habilidades_dia", "area_interes",
    "estado_sentimental", "actividades_extracurriculares", "con_quien_vives", "problemas_salud",
    "discapacidad_fisica", "creditos_completados", "ingreso_familiar_anual",
    "horas_clases_semanales", "horas_sueno_dia", "horas_ejercicio_semanal",
    "tipo_transporte", "horas_transporte_total", "horas_trabajo_semanal"
]

# 👉 Inserta aquí los valores del nuevo estudiante, respetando el orden de las columnas
nuevo_estudiante = [
    3042, 0, 21, 2019, 5,
    1, 0, 2, 3,
    1, 1, 1, 4,
    1, 90, 0, 0,
    1, 30, 2, 5,
    3, 1, 1, 0, 0,
    60, 79000, 20, 8, 3,
    1, 8, 9
]

# Convertir a DataFrame
X_nuevo = pd.DataFrame([nuevo_estudiante], columns=columnas)

# Predecir con ambos modelos
pred_rf = modelo_rf.predict(X_nuevo)[0]
pred_gb = modelo_gb.predict(X_nuevo)[0]

# Mostrar resultados
print("🎯 Predicción de nota del semestre:")
print(f"🔸 Random Forest:      {pred_rf:.2f} / 20")
print(f"🔸 Gradient Boosting:  {pred_gb:.2f} / 20")
