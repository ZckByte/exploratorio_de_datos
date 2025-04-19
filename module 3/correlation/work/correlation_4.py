import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"

# Análisis de rendimiento y precio de componentes de PC
# Crear el DataFrame
# Calcular la matriz de correlación de las columnas numéricas
# Mostrarla como heatmap (usa annot=True y cmap='coolwarm')
# Hacer tres regplot():
# precio_usd vs velocidad_ghz
# precio_usd vs memoria_gb
# precio_usd vs consumo_w
# (Opcional) Mostrar un gráfico de barras con el precio promedio por tipo de componente
# Exportar:
# El DataFrame limpio como hardware_data.csv
# La matriz como correlacion_hardware.csv

datos = {
    'componente': ['CPU A', 'CPU B', 'GPU A', 'GPU B', 'RAM A', 'RAM B'],
    'tipo': ['CPU', 'CPU', 'GPU', 'GPU', 'RAM', 'RAM'],
    'precio_usd': [250, 320, 500, 650, 80, 120],
    'velocidad_ghz': [3.5, 4.0, 1.5, 1.8, 3.2, 3.6],
    'memoria_gb': [8, 12, 8, 12, 16, 32],
    'consumo_w': [65, 95, 250, 300, 45, 55]
}


df = pd.DataFrame(datos)

corre_matriz = df[['precio_usd', 'velocidad_ghz', 'memoria_gb', 'consumo_w']].corr()
sns.heatmap(data=corre_matriz, annot=True, cmap='coolwarm')
plt.title('Correlacion Matriz')
plt.show()
corre_matriz.to_csv(f'{path}/correlacion_hardware.csv')

sns.regplot(x='precio_usd', y='velocidad_ghz', data=df)
plt.title('Correlacion Precio Usd - Velocidad Ghz')
plt.xlabel('Precio')
plt.ylabel('Velocidad_ghz')
plt.show()

sns.regplot(x='precio_usd', y='memoria_gb', data=df)
plt.title('Correlacion Precio Usd - Memoria GB')
plt.xlabel('Precio')
plt.ylabel('Memoria GB')
plt.show()

sns.regplot(x='precio_usd', y='consumo_w', data=df)
plt.title('Correlacion Precio Usd - Consumo W')
plt.xlabel('Precio')
plt.ylabel('Consumo W')
plt.show()

df.groupby(by='componente')['precio_usd'].mean().sort_values(ascending=False).plot(kind='barh')
plt.ylabel('Componente')
plt.xlabel('Precio Promedio')
plt.title('Precio Promedio por Tipo de Componente')
plt.show()
df.to_csv(f'{path}/correlation_4.csv')