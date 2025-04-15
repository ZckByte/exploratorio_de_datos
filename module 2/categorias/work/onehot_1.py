import pandas as pd
import numpy as np
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"

# Ejercicio 14 – Datos de vehículos y tipo de combustible
# Crear el DataFrame con los datos.

# Usar pd.get_dummies() sobre la columna fuel para obtener las variables binarias.

# Unir esas columnas al DataFrame original con pd.concat(...).

# Eliminar la columna original fuel.

# Reordenar las columnas dejando vehiculo, puertas, y luego las dummies.

# Exportar el resultado como vehiculos_onehot.csv.
datos = {
    'vehiculo': [
        'Toyota Corolla',
        'Ford Ranger',
        'Renault Sandero',
        'Peugeot 208',
        'Volkswagen Amarok',
        'Fiat Uno'
    ],
    'fuel': ['gas', 'diesel', 'gas', 'nafta', 'diesel', 'nafta'],
    'puertas': [4, 2, 4, 4, 4, 2]
}
df = pd.DataFrame(datos)

dummies =  pd.get_dummies(df['fuel'])
df = pd.concat([df,dummies], axis=1)

df.drop('fuel', axis=1, inplace=True)
df = df[['vehiculo', 'puertas', 'gas', 'diesel', 'nafta']]
df.to_csv(f'{path}/onehot_1.csv')