import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"

#  Ejercicio 15 – Transmisión y análisis de autos
# Crear el DataFrame.

# Unificar los valores de transmision para que solo existan: "manual" y "automatica".

# "Manual" → "manual"

# "auto" → "automatica"

# Aplicar pd.get_dummies() sobre transmision.

# Unir las columnas dummies al DataFrame y eliminar transmision.

# Mostrar un conteo de cuántos autos hay de cada tipo de transmisión.

# Exportar como transmision_onehot.csv.}

datos = {
    'modelo': [
        'Toyota Corolla',
        'Ford Mustang',
        'Renault Kwid',
        'Audi A3',
        'Chevrolet Corsa',
        'Peugeot 208',
        'BMW M3'
    ],
    'transmision': [
        'manual',
        'automática',
        'Manual',
        'auto',
        'manual',
        'automática',
        'auto'
    ],
    'puertas': [4, 2, 4, 4, 2, 4, 2]
}
df = pd.DataFrame(datos)

df['transmision'] = df['transmision'].replace({'auto': 'automática', 'Manual': 'manual'})

dummies = pd.get_dummies(df['transmision'])
df = pd.concat([df,dummies], axis=1)
df.drop('transmision', axis=1, inplace=True)


conteo = df[['manual', 'automática']].sum().plot(kind='bar')
print(conteo)
plt.show()

df.to_csv(f'{path}/onehot_2.csv')