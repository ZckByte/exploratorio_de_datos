import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"
#  Ejercicio 20 – Análisis de películas
# Crear el DataFrame.

# Usar .describe() para analizar duracion_min y puntuacion.

# Usar .value_counts() para ver cuántas películas hay por genero.

# Mostrar un boxplot de duración por género.

# Mostrar un scatter plot entre duración y puntuación.

# Exportar como peliculas_data.csv y resumen_peliculas.csv
datos = {
    'titulo': [
        'Everything Everywhere',
        'John Wick 4',
        'Barbie',
        'Oppenheimer',
        'Super Mario Bros',
        'Spider-Man: Across...'
    ],
    'genero': ['Aventura', 'Acción', 'Comedia', 'Drama', 'Animación', 'Animación'],
    'duracion_min': [139, 169, 114, 180, 92, 140],
    'puntuacion': [8.1, 7.8, 7.2, 8.6, 7.1, 8.7]
}
df = pd.DataFrame(datos)
#1
df.describe().to_csv(f'{path}/resumen_data_a_3.csv')
#2
plt.figure()
df.value_counts('genero').plot(kind='bar', title='Peliculas por genero')
plt.ylabel('Cantidad')
plt.xlabel('Genero')
#3
df.boxplot(column='duracion_min', by='genero')
plt.title('Duracion por Genero')
plt.xlabel('')
plt.suptitle('')
#4
plt.figure()
plt.scatter(df['duracion_min'], df['puntuacion'])
plt.title('Duracion vs Puntuacion')
plt.xlabel('Duracion')
plt.ylabel('Puntuacion')
plt.show()
df.to_csv(f'{path}/data_a_3.csv')