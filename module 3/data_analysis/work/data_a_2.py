import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"
# Ejercicio 18 – Análisis de ventas de videojuegos
# Crear el DataFrame con los datos.

# Usar .describe() para analizar precio y calificacion.

# Usar .value_counts() para contar cuántos juegos hay por plataforma.

# Mostrar un diagrama de caja (boxplot) de los precios por plataforma.

# (Opcional) Mostrar un scatter plot entre precio y calificacion.

datos = {
    'titulo': [
        'Elden Ring',
        'God of War',
        'Minecraft',
        'GTA V',
        'The Last of Us',
        'Mario Kart 8'
    ],
    'plataforma': ['PC', 'PS5', 'Switch', 'PC', 'PS5', 'Switch'],
    'precio': [59.99, 69.99, 29.99, 39.99, 59.99, 49.99],
    'calificacion': [9.5, 9.2, 8.5, 9.0, 9.4, 8.7]
}


df = pd.DataFrame(datos)

df.describe().to_csv(f'{path}/resumen_data_a_2.csv')
plt.figure()
df['plataforma'].value_counts().plot(kind='bar', title='Juegos por Plataforma')
plt.xlabel('Plataforma')
plt.ylabel('Cantidad')

plt.figure()
df.boxplot(column='precio', by='plataforma')
plt.title('Distribución de precios por plataforma')
plt.suptitle('')  # Quita el título automático de pandas

plt.figure()
plt.scatter(df['precio'], df['calificacion'])
plt.title('Precio vs Calificación')
plt.xlabel('Precio')
plt.ylabel('Calificación')

plt.show()

df.to_csv(f'{path}/data_a_2.csv')