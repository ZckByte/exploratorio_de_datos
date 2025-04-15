import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"

# Ejercicio 16 – Registro de bicicletas urbanas
# Crear el DataFrame con los datos.

# Aplicar One Hot Encoding a la columna tipo usando pd.get_dummies().
# Unir las columnas dummies y eliminar tipo.

# Mostrar un conteo de cuántas bicis hay por tipo (urbana, montaña, eléctrica) usando .sum().
# Agregar una columna booleana llamada rodado_grande que sea True si el rodado es mayor o igual a 28.

# Exportar como bicicletas_onehot.csv.

datos = {
    'bici_id': ['B-101', 'B-102', 'B-103', 'B-104', 'B-105', 'B-106'],
    'color': ['rojo', 'azul', 'negro', 'rojo', 'azul', 'negro'],
    'tipo': ['urbana', 'montaña', 'eléctrica', 'urbana', 'montaña', 'eléctrica'],
    'rodado': [26, 29, 28, 26, 27, 28]
}

df = pd.DataFrame(datos)

dummies = pd.get_dummies(df['tipo']).astype(int) #astype para que aparezca con 1 y 0, sin astype aparece true o false
df = pd.concat([df, dummies], axis=1)

df.drop(['tipo'], axis=1, inplace=True)

df[['urbana', 'montaña', 'eléctrica']].sum().plot(kind='bar')
plt.show()
df['rodado_grande'] = df['rodado'] >= 28 #Crea un columna de tipo booleana con condicion

df.to_csv(f'{path}/onehot_3.csv')
