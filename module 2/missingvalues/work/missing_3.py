#Inventario de smartphones usados
# Eliminar las filas donde el precio falte.
# Reemplazar los valores faltantes en almacenamiento por el promedio.
# Reemplazar los valores faltantes en estado_bateria por el valor más común.
# Reemplazar los valores faltantes en color por el más común.
# Reemplazar los valores faltantes en estado por la moda.

import pandas as pd
import numpy as np
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"
datos = {
    'modelo': ['iPhone 11', 'Galaxy S10', 'Xiaomi Mi 9', 'iPhone XR', 'Motorola G7', 'Galaxy A50'],
    'precio': [600, None, 350, 450, None, 300],
    'estado_bateria': ['buena', 'regular', None, 'buena', 'buena', None],
    'almacenamiento': [64, None, 128, None, 64, None],
    'color': ['negro', 'blanco', 'azul', None, 'negro', 'blanco'],
    'estado': ['bueno', 'bueno', None, 'bueno', 'malo', None]
}

df = pd.DataFrame(datos)
df.dropna(subset=['precio'],inplace=True)

almacenamiento_promedio = df['almacenamiento'].mean()
df['almacenamiento'].replace(np.nan, almacenamiento_promedio, inplace=True)

comun_estado_bateria = df['estado_bateria'].mode()[0]
df['estado_bateria'].replace(np.nan,comun_estado_bateria,inplace=True)

comun_color = df['color'].mode()[0]
df['color'].replace(np.nan, comun_color, inplace=True)

comun_estado = df['estado'].mode()[0]
df['estado'].replace(np.nan,comun_estado,inplace=True)  

df.to_csv(f'{path}/smartphones.csv')
print(df)