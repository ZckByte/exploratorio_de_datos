import pandas as pd
import matplotlib.pyplot as plt
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"
# Ejercicio 24 – Estadísticas de ventas por tienda y categoría
# Crear el DataFrame.

# Usar groupby(['tienda', 'categoria']) para calcular:
# a) El total de ventas
# b) La media de ventas
# c) El total de unidades vendidas
# Exportar el resumen como ventas_resumen.csv
# (Opcional) Hacer un gráfico de barras con las ventas totales por tienda.

datos = {
    'tienda': ['Tienda A', 'Tienda A', 'Tienda B', 'Tienda A', 'Tienda C', 'Tienda B', 'Tienda C'],
    'categoria': ['Electrónica', 'Oficina', 'Electrónica', 'Electrónica', 'Oficina', 'Oficina', 'Electrónica'],
    'producto': ['Monitor', 'Silla', 'Teclado', 'Teclado', 'Silla', 'Escritorio', 'Monitor'],
    'ventas': [12000, 3000, 2500, 2000, 2400, 5000, 6000],
    'unidades': [20, 10, 25, 20, 8, 5, 10]
}

df = pd.DataFrame(datos)

#1
total_ventas = df.groupby(['tienda', 'categoria'])['ventas'].sum()
media_ventas = df.groupby(['tienda', 'categoria'])['ventas'].mean()
total_unidades_ventas = df.groupby(['tienda', 'categoria'])['unidades'].sum()

#2
plt.figure()
total_ventas.plot(kind='barh', title='Ventas Totales por Tienda')
plt.tight_layout()
plt.xlabel('Total de Ventas')
plt.ylabel('Tienda')
plt.show()


resumen = pd.concat([total_ventas, media_ventas, total_unidades_ventas], axis=1)
resumen.columns = ['total_ventas', 'media_ventas', 'total_unidades']
resumen.to_csv(f'{path}/resumen.csv')

df.to_csv(f'{path}/groupby_3.csv')