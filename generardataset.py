import numpy as np
import pandas as pd

# Definir el número de ejemplos y características
num_ejemplos = 10000

# Generar características aleatorias relacionadas con la preparación de yogurt griego
dataset = pd.DataFrame({
    'cantidad_leche_litros': np.round(np.random.uniform(100, 20, num_ejemplos), 2),  # Valores entre 1000 y 2000 con dos decimales
    'temperatura_fermentacion': np.round(np.random.uniform(35, 45, num_ejemplos), 2),
    'tiempo_fermentacion_horas': np.round(np.random.normal(8, 2, num_ejemplos), 2),
    'cantidad_cultivos_miligramos': np.round(np.random.normal(50, 10, num_ejemplos), 2),
    'tiempo_colado_horas': np.round(np.random.normal(3, 1, num_ejemplos), 2),
    'contenido_grasa_porcentaje': np.round(np.random.uniform(3, 10, num_ejemplos), 2),
    'nivel_acidez_pH': np.round(np.random.uniform(4, 4.5, num_ejemplos), 2),
    'cantidad_proteina_gramos': np.round(np.random.normal(6, 1, num_ejemplos), 2),
    'textura_puntuacion': np.round(np.random.uniform(1, 10, num_ejemplos), 2),
    'sabor_puntuacion': np.round(np.random.uniform(1, 10, num_ejemplos), 2)
})

# Calcular el nivel de calidad basado en algunas de las características
dataset['nivel_calidad'] = np.round(
    0.2 * dataset['cantidad_proteina_gramos'] +
    0.2 * dataset['textura_puntuacion'] +
    0.2 * dataset['sabor_puntuacion'] +
    0.2 * (5 - abs(dataset['nivel_acidez_pH'] - 4.3)) +
    0.2 * (dataset['contenido_grasa_porcentaje'] / 10), 2
)

# Guardar el dataset en un archivo CSV con punto y coma como separador
dataset.to_csv('dataset_yogurt_griego.csv', sep=';', index=False, decimal=',')

print("Archivo 'dataset_yogurt_griego.csv' generado con éxito.")
