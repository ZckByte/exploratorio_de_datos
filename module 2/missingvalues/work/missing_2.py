#Reparando una tabla de laptops
#Eliminar las filas donde falte el precio.
# Reemplazar los valores faltantes en ciclos_carga por el promedio de esa columna.
# Reemplazar los valores faltantes en tipo_bateria por el valor más común.
# Reemplazar el valor faltante en estado por la moda.

import pandas as pd
import numpy as np
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"
datos = {
    'marca': ['Lenovo', 'HP', 'Asus', 'Dell', 'Toshiba'],
    'precio': [350, None, 450, 400, None],
    'tipo_bateria': ['Li-ion', None, 'NiMH', 'Li-ion', 'Li-ion'],
    'ciclos_carga': [500, 300, None, 400, None],
    'estado': ['bueno', 'regular', 'bueno', None, 'malo']
}

df = pd.DataFrame(datos)
df.dropna(subset=['precio'],inplace=True)
carga_promedio = df['ciclos_carga'].mean()
df['ciclos_carga'].replace(np.nan,carga_promedio,inplace=True)
tipo_comun = df['tipo_bateria'].mode()[0]
df['tipo_bateria'].replace(np.nan, tipo_comun,inplace=True)
estado_moda = df['estado'].mode()[0]
df['estado'].replace(np.nan,estado_moda,inplace=True)

df.to_csv(f'{path}/laptops.csv')
print(df)
