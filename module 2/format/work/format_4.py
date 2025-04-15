# Ejercicio 7 – Datos de envío internacional

# Convertir cantidad y peso_kg a tipo numérico.
# Reemplazá "N/A" con el promedio.
# Ojo: un valor tiene coma decimal ("0,3") → pandas no lo entiende por defecto.
# Convertir costo_envio a float.
# Unificar destino para que todos digan "New York"
# Estandarizar la columna urgente para que todos los valores estén en minúsculas ("sí" o "no").

import pandas as pd
import numpy as np
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"

datos = {
    'producto': ['Monitor Samsung', 'Mouse Logitech', 'Teclado Redragon', 'Audífonos Sony'],
    'cantidad': ["3", 10, "4", 2],
    'peso_kg': [12.5, "0.2", "N/A", "0,3"],
    'destino': ['nyc', 'New York', 'N.Y.', 'NY'],
    'costo_envio': ["25.50", 5, "10", 7.5],
    'urgente': ['sí', 'no', 'Sí', 'NO']
}

df = pd.DataFrame(datos)
#1
df['cantidad'] = df['cantidad'].astype(int)
#2
df['peso_kg'] = df['peso_kg'].replace("N/A", np.nan)
df['peso_kg'] = df['peso_kg'].astype(str).str.replace(",", ".", regex=False)
df['peso_kg'] = df['peso_kg'].astype(float)
peso_promedio = df['peso_kg'].mean()
df['peso_kg'] = df['peso_kg'].fillna(peso_promedio).round(1)
#3
df['costo_envio'] = df['costo_envio'].astype(float)
#4
df['destino'] = df['destino'].replace({'nyc': 'New York', 'N.Y.': 'New York', 'NY': 'New York'})
#5
df['urgente'] = df['urgente'].str.lower()
df.to_csv(f'{path}/format_4.csv')
