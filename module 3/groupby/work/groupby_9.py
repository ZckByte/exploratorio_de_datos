import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"

# Ejercicio 30 – Ventas por región y producto con múltiples métricas
# Crear el DataFrame 

# Crear una tabla dinámica (pivot_table) con:
# index='región'
# columns='producto'
# values=['unidades', 'total_venta']
# aggfunc=['sum', 'mean']
# Visualizar los valores de total_venta con sns.heatmap (podés usar .xs() para filtrar esa parte del pivot).
# Exportar la tabla como ventas_pivot.csv

datos = {
    'vendedor': ['Ana', 'Luis', 'Carla', 'Ana', 'Luis', 'Carla', 'Luis'],
    'región': ['Norte', 'Sur', 'Norte', 'Sur', 'Norte', 'Sur', 'Norte'],
    'producto': ['Laptop', 'Monitor', 'Teclado', 'Laptop', 'Teclado', 'Monitor', 'Laptop'],
    'unidades': [3, 2, 5, 2, 3, 4, 1],
    'total_venta': [3000, 800, 250, 2000, 150, 1600, 1000]
}

df = pd.DataFrame(datos)

pivot = df.pivot_table(index='región', columns='producto', values=['unidades', 'total_venta'], aggfunc=['sum', 'mean'])

pivot_ventas = pivot.xs('sum', level=0, axis=1)['total_venta']
sns.heatmap(pivot_ventas, annot=True)
plt.title('Unidades y Ventas por región')
plt.xlabel('Suma y Promedio de Productos y cantidades')
plt.ylabel('Región')
plt.show()


pivot.to_csv(f'{path}/ventas_pivot.csv')