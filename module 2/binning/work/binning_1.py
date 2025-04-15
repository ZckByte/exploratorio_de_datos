import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"

#Ejercicio 11 – Binning de productos por precio:
# Crear 3 grupos de precio:

# "bajo"
# "medio"
# "alto"

# Usar np.linspace() para generar los cortes automáticos entre el precio mínimo y máximo.

# Crear una nueva columna llamada precio_categoria con pd.cut() y los nombres de los grupos.

# Hacer un conteo de cuántos productos hay en cada categoría.

# (Opcional) Mostrar un histograma de la columna original (precio) dividido por bins.

datos = {
    'producto': [
        'Mouse Logitech',
        'Teclado Redragon',
        'Monitor Samsung',
        'Laptop HP',
        'Audífonos Sony',
        'SSD Kingston'
    ],
    'precio': [25, 50, 180, 720, 60, 95]
}

df = pd.DataFrame(datos)

#1 
groups = ['bajo', 'medio', 'alto']

#2
bins = np.linspace(df['precio'].min(), df['precio'].max(), 4)

#3
df['precio_categoria'] = pd.cut(df['precio'], bins, labels=groups, include_lowest=True)

#4
df['precio_categoria'].value_counts().plot(kind='bar')
plt.show()

df.to_csv(f'{path}/binning_1.csv')

