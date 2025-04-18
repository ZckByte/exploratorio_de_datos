import pandas as pd
import matplotlib.pyplot as plt
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"
# Ejercicio 25 – Rendimiento de vendedores por región
# Crear el DataFrame.
# Crear una columna cumplio_objetivo → True si ventas >= objetivos.
# Agrupar por vendedor y contar cuántas veces cumplió el objetivo.
# Agrupar por region para sacar:
# a) Ventas totales
# b) Media de cumplimiento (cumplio_objetivo como porcentaje)
# Exportar el resumen completo como ventas_vendedores.csv.

datos = {
    'vendedor': [
        'Carla', 'Tomás', 'Ana', 'Marcos', 'Laura',
        'Pedro', 'Carla', 'Tomás', 'Ana'
    ],
    'region': [
        'Norte', 'Sur', 'Norte', 'Oeste', 'Sur',
        'Oeste', 'Norte', 'Sur', 'Norte'
    ],
    'ventas': [
        8500, 6700, 9200, 5600, 7400,
        6100, 8700, 6900, 9500
    ],
    'objetivos': [
        8000, 7500, 9000, 6000, 7000,
        6000, 8000, 7500, 9000
    ]
}


df = pd.DataFrame(datos)

df['cumplio_objetivo'] = df['ventas'] >= df['objetivos']
veces = df.groupby(['vendedor'])['cumplio_objetivo'].sum()
ventas_totales = df.groupby('region')['ventas'].sum()
media_cumplimiento = df.groupby('region')['cumplio_objetivo'].mean() * 100

resumen2 = pd.concat([veces, ventas_totales,media_cumplimiento], axis=1 )
resumen2.columns = ['Cumpli', 'Ventas Totales', 'Media Cumplimiento']
resumen2.reset_index(inplace=True)

veces.plot(kind='bar', title='Veces que cada vendedor cumplió el objetivo')
plt.ylabel('Cantidad de veces')
plt.xlabel('Vendedor')
plt.tight_layout()
plt.show()

resumen2.to_csv(f'{path}/resumen2.csv')
df.to_csv(f'{path}/groupby_4.csv')