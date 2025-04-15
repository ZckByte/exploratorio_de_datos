import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"
# Ejercicio 17 – Análisis básico de notebooks
# Crear el DataFrame con los datos.

# Usar .describe() para obtener estadísticas de las columnas numéricas (precio, ram_gb, disco_gb).

# Usar .value_counts() para ver la cantidad de notebooks por tipo de procesador.

# (Opcional) Mostrar un gráfico de barras con la distribución de procesadores.

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
df.describe().to_csv(f'{path}/resumen_data_a_1.csv')
df['procesador'].value_counts().plot(kind='bar')
plt.show()

df.to_csv(f'{path}/data_a_1.csv')