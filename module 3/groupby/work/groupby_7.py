import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"

# Ejercicio 28 – Análisis de ventas por tienda y categoría con pivot_table
# Crear una pivot_table con:

# index='tienda'
# columns='categoria'
# values='ventas'
# aggfunc='sum'
# Visualizar la tabla con sns.heatmap() de Seaborn usando annot=True.
# Exportar la tabla como CSV: ventas_pivot.csv

datos = {
    'tienda': ['Tienda A', 'Tienda A', 'Tienda B', 'Tienda A', 'Tienda C', 'Tienda B', 'Tienda C'],
    'categoria': ['Electrónica', 'Oficina', 'Electrónica', 'Electrónica', 'Oficina', 'Oficina', 'Electrónica'],
    'producto': ['Monitor', 'Silla', 'Teclado', 'Teclado', 'Silla', 'Escritorio', 'Monitor'],
    'ventas': [12000, 3000, 2500, 2000, 2400, 5000, 6000],
    'unidades': [20, 10, 25, 20, 8, 5, 10]
}

df = pd.DataFrame(datos)

pivot = df.pivot_table(values='ventas', index='tienda', columns='categoria', aggfunc='sum')
sns.heatmap(pivot, annot=True)

plt.show()
df.to_csv(f'{path}/ventas_pivot.csv')