import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"
#  Ejercicio 21 – Agrupación de notebooks por procesador
# Crear el DataFrame con los datos
# Agrupar por procesador y calcular el precio promedio por procesador.
# Agrupar por procesador y mostrar la cantidad de notebooks con .count().
# (Opcional) Mostrar un gráfico de barras con los precios promedios por procesador.

datos = {
    'modelo': [
        'Lenovo IdeaPad',
        'HP Pavilion',
        'Dell Inspiron',
        'Acer Aspire',
        'ASUS ZenBook',
        'Lenovo ThinkPad'
    ],
    'precio': [750, 820, 660, 580, 980, 890],
    'ram_gb': [8, 16, 8, 4, 16, 8],
    'disco_gb': [512, 1000, 256, 512, 512, 1000],
    'procesador': ['Intel i5', 'AMD Ryzen 5', 'Intel i3', 'AMD Ryzen 3', 'Intel i7', 'AMD Ryzen 7']
}
df = pd.DataFrame(datos)

precio_promedio = df.groupby('procesador')['precio'].mean()
print("Precio promedio por procesador:")
print(precio_promedio)

cantidad_por_procesador = df['procesador'].value_counts()
print("\nCantidad de notebooks por procesador:")
print(cantidad_por_procesador)

plt.figure()
precio_promedio.sort_values().plot(kind='barh', title='Precio promedio por procesador')
plt.xlabel('Precio Promedio')
plt.ylabel('Procesador')
plt.tight_layout()
plt.show()

precio_promedio.to_csv(f'{path}/precio_promedio_por_procesador.csv')
df.to_csv(f'{path}/groupby_1.csv')