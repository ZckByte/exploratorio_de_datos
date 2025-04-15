# Inventario de cámaras digitales

# Convertir los valores de "foto_por_galon" a litros/100km usando la fórmula 235 / valor.
# Cambiar el nombre de esa columna a fotos_por_litro_100km.
# Unificar las ciudades para que todos digan exactamente "New York".
# Asegurarte de que las columnas precio y zoom_optico estén en formato numérico (float o int).
import pandas as pd
import numpy as np
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"
datos = {
    'modelo': ['Canon T7', 'Nikon D3500', 'Sony Alpha A6000', 'Fujifilm X-T200'],
    'precio': [450, "500", 550, 620],
    'ciudad': ['NY', 'New York', 'N.Y.', 'Ny'],
    'zoom_optico': [3.0, 3.5, "4.0", 3.8],
    'foto_por_galon': [30, 28, 32, 27]
}
df = pd.DataFrame(datos)
#1
df['foto_por_galon'] = 235/df['foto_por_galon']
df.rename(columns={'foto_por_galon': 'fotos_por_litro_100km'}, inplace=True)
#2
df['ciudad'] = 'New York'
#3
df['precio'] = df['precio'].astype(int)
df['zoom_optico'] = df['zoom_optico'].astype(float)

print(df.info())
df.to_csv(f'{path}/camaras_digitales.csv')




