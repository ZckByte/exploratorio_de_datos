# Analisis de tables de segunda mano

# Convertir los precios a tipo entero.

# Convertir la columna almacenamiento a tipo entero.

# Unificar todas las ciudades para que digan "New York" 
# con la primera letra en mayúscula.

# Estandarizar el texto de la columna tipo_pantalla 
# para que quede todo en mayúsculas (ej: "LCD", "AMOLED").

# Convertir peso a tipo entero, y si hay valores que no se puedan convertir 
# (como "N/A"), reemplazarlos con el promedio de los pesos válidos.

import pandas as pd
import numpy as np
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"
datos = {
    'modelo': ['iPad Air', 'Galaxy Tab S6', 'Lenovo Tab P11', 'Huawei MatePad'],
    'precio': ["650", 580, "500", 490],
    'ciudad': ['N.Y.', 'NY', 'new york', 'Ny'],
    'almacenamiento': [64, 128, "64", 128],
    'tipo_pantalla': ['LCD', 'Amoled', 'lcd', 'AMOLED'],
    'peso': ["460", 420, "N/A", 430]
}
df = pd.DataFrame(datos)

df['precio'] = df['precio'].astype(int)
df['almacenamiento'] = df['almacenamiento'].astype(int)

df['ciudad'] = df['ciudad'].str.capitalize().replace({'N.y.': 'New york', 'Ny': 'New york', 'NY': 'New york', 'new york': 'New york'})

df['tipo_pantalla'] = df['tipo_pantalla'].str.upper()

#!
df['peso'].replace("N/A", np.nan).astype(float)
df['peso'] = df['peso'].astype(float)
peso_promedio = df['peso'].mean()
df['peso'] = df['peso'].fillna(peso_promedio)

df.to_csv(f'{path}/format_2.csv')