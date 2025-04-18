import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dateutil import parser
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"

def parse_fecha(fecha):
    try:
        return parser.parse(fecha)
    except:
        return pd.NaT

# Proyecto Final – Análisis de ventas y desempeño de sucursales
#  Limpieza y Formato:
# Convertir fecha_venta a formato YYYY-MM-DD usando pd.to_datetime().
# Asegurar que precio_unitario, costo_unitario y unidades_vendidas estén en formato float/int.

# 🔹 Cálculo de columnas:
# Crear columna ganancia_unitaria = precio_unitario - costo_unitario
# Crear columna total_venta = precio_unitario * unidades_vendidas
# Crear columna total_ganancia = ganancia_unitaria * unidades_vendidas

# 🔹 Agrupación y análisis:
# Agrupar por sucursal y categoria para obtener:
# Total vendido
# Total de unidades
# Promedio de ganancia unitaria
# Crear una pivot_table donde:

# index='sucursal'
# columns='producto'
# values='total_ganancia'
# aggfunc='sum'

# Mostrar la tabla con un heatmap (sns.heatmap())
# 🔹 Exportar:
# Exportar:
# El DataFrame limpio como ventas_limpio.csv
# El resumen agrupado como ventas_resumen.csv
# La pivot como ventas_pivot.csv

datos = {
    'sucursal': ['Norte', 'Norte', 'Sur', 'Sur', 'Este', 'Oeste', 'Oeste', 'Este'],
    'producto': ['Laptop', 'Teclado', 'Laptop', 'Monitor', 'Teclado', 'Laptop', 'Monitor', 'Monitor'],
    'categoria': ['Electrónica', 'Periférico', 'Electrónica', 'Electrónica', 'Periférico', 'Electrónica', 'Electrónica', 'Electrónica'],
    'precio_unitario': [1000, 50, 1100, 400, 60, 950, 420, 390],
    'unidades_vendidas': [3, 10, 2, 5, 8, 4, 6, 7],
    'costo_unitario': [800, 30, 850, 300, 40, 780, 310, 320],
    'empleado': ['Laura', 'Laura', 'Tomás', 'Tomás', 'Sofía', 'Carla', 'Carla', 'Sofía'],
    'fecha_venta': ['2023-06-10', '2023/06/10', '10-06-2023', '2023.06.11', '11-06-2023', '2023/06/12', '2023.06.12', '2023-06-13']
}

df = pd.DataFrame(datos)

df['fecha_venta'] = df['fecha_venta'].apply(parse_fecha)
print(df.info())

df['ganancia_unitaria'] = df['precio_unitario'] - df['costo_unitario']
df['total_venta'] = df['precio_unitario'] * df['unidades_vendidas']
df['total_ganancia'] = df['ganancia_unitaria'] * df['unidades_vendidas']

total_vendido = df.groupby(['sucursal', 'categoria'])['total_venta'].sum()
total_unidades = df.groupby(['sucursal', 'categoria'])['unidades_vendidas'].sum()
promedio_ganacia = df.groupby(['sucursal', 'categoria'])['ganancia_unitaria'].mean()

pivot = df.pivot_table(values='total_ganancia',index='sucursal', columns='producto', aggfunc='sum')
sns.heatmap(pivot, annot=True)
plt.title('Ganancias Sucusales')
plt.ylabel('Sucursal')
plt.xlabel('Productos')
plt.show()

df.groupby('empleado')['total_ganancia'].sum().sort_values(ascending=False).plot(kind='bar')
plt.title('Ganacia Total Por Empleado')
plt.xlabel('Empleado')
plt.ylabel('Ganacia')
plt.show()


resumen = pd.concat([total_vendido, total_unidades,promedio_ganacia], axis=1)
resumen.columns = ['Total Vendido', 'Total Unidades', 'Promedio Ganacia']
resumen.to_csv(f'{path}/ventas_resumen.csv')
pivot.to_csv(f'{path}/ventas_pivot.csv')
df.to_csv(f'{path}/ventas_limpio.csv')