#Normalizando productos

# Normalizá la columna peso_kg con:

# Simple Scaling

# Min-Max

# Z-Score

# Hacé lo mismo con la columna volumen_cm3.
import pandas as pd
import numpy as np
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"

datos = {
    'producto': ['Laptop HP', 'Monitor Samsung', 'Teclado Logitech', 'Mouse Genius'],
    'peso_kg': [1.8, 3.2, 0.9, 0.2],
    'volumen_cm3': [4200, 8800, 2600, 800]
}
df = pd.DataFrame(datos)

#1
peso_simple = df['peso_kg'] / df['peso_kg'].max()
df['peso_simple'] = peso_simple

peso_min_max = (df['peso_kg'] - df['peso_kg'].min())/(df['peso_kg'].max() - df['peso_kg'].min())
df['peso_min_max'] = peso_min_max

peso_z = (df['peso_kg'] - df['peso_kg'].mean()) / df['peso_kg'].std()
df['peso_std'] = peso_z
#2

volumen_simple = df['volumen_cm3'] / df['volumen_cm3'].max()
df['volumen_simple'] = volumen_simple
volumen_min_max = (df['volumen_cm3'] - df['volumen_cm3'].min()) / (df['volumen_cm3'].max() - df['volumen_cm3'].min())
df['volumen_min_max'] = volumen_min_max
volumen_z = (df['volumen_cm3'] - df['volumen_cm3'].mean()) / df['volumen_cm3'].std()
df['volumen_z'] = volumen_z

df = df[['producto', 'peso_kg', 'peso_simple', 'peso_min_max', 'peso_std',
         'volumen_cm3', 'volumen_simple', 'volumen_min_max', 'volumen_z']]

df.to_csv(f'{path}/data_1.csv')