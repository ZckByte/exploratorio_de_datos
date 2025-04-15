# Crea un DataFrame de autos con columnas como marca, 
# precio, tipo_combustible y perdidas_normalizadas, 
# y simula valores faltantes.

# 🎯 Objetivo:
# Eliminar las filas donde falte el precio.
# Reemplazar los valores faltantes en perdidas_normalizadas por su promedio.
# Reemplazar los valores faltantes en tipo_combustible por el valor más común.

import pandas as pd
import numpy as np
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"
datos = {
    'marca': ['Toyota', 'BMW', 'Ford', 'Honda', 'Chevy'],
    'precio': [20000, np.nan, 15000, 18000, np.nan],
    'tipo_combustible': ['gasolina', 'diésel', np.nan, 'gasolina', np.nan],
    'perdidas_normalizadas': [np.nan, 4000, 4500, np.nan, 4200]
}
df = pd.DataFrame(datos)
#1
df.dropna(subset="precio",axis=0,inplace=True)
#2
promedio = df['perdidas_normalizadas'].mean()
df['perdidas_normalizadas'].replace(np.nan,promedio,inplace=True)
#3
moda_combustible = df['tipo_combustible'].mode()[0]
df['tipo_combustible'].replace(np.nan, moda_combustible, inplace=True)
df.to_csv(f'{path}/missing_1.csv')
print(df)

