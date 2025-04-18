import pandas as pd
import matplotlib.pyplot as plt
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"
# Crear el DataFrame.
# Crear una nueva columna total_compra multiplicando cantidad * precio_unitario.
# Usar groupby(['cliente', 'categoria']) para calcular:
# a) El total gastado (sum())
# b) La cantidad de productos (sum() sobre cantidad)
# Resetear el índice para que quede como DataFrame normal.
# (Opcional) Graficar cuánto gastó cada cliente en total (agrupando solo por cliente).

datos = {
    'cliente': ['Ana', 'Luis', 'Ana', 'Carla', 'Luis', 'Ana', 'Carla'],
    'categoria': ['Electrónica', 'Oficina', 'Electrónica', 'Oficina', 'Electrónica', 'Oficina', 'Electrónica'],
    'producto': ['Teclado', 'Silla', 'Mouse', 'Escritorio', 'Monitor', 'Silla', 'Teclado'],
    'cantidad': [2, 1, 1, 1, 2, 1, 1],
    'precio_unitario': [25, 120, 15, 200, 150, 120, 25]
}

df = pd.DataFrame(datos)

df['total_compra'] = df['cantidad'] * df['precio_unitario']

total_gastado = df.groupby(['cliente', 'categoria'])['total_compra'].sum()
cantidad_productos = df.groupby(['cliente', 'categoria'])['cantidad'].sum()

df.reset_index(inplace=True)
total_por_cliente = df.groupby('cliente')['total_compra'].sum()
total_por_cliente.plot(kind='bar', title='Total gastado por cliente')
plt.ylabel('Total Compra ($)')
plt.xlabel('Cliente')
plt.tight_layout()

plt.show()
df.to_csv(f'{path}/groupby_2.csv')