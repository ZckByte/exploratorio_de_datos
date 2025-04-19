import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"

# Ejercicio 32 – Correlación en especificaciones de notebooks
# Crear el DataFrame
# Calcular la matriz de correlación con .corr()
# Mostrar el heatmap de la matriz
# Crear dos regplot():
# precio vs bateria_horas
# precio vs peso_kg
# (Opcional) Exportar todo como correlation_2.csv
datos = {
    'modelo': ['Notebook A', 'Notebook B', 'Notebook C', 'Notebook D', 'Notebook E', 'Notebook F'],
    'precio': [1200, 950, 1500, 1100, 1700, 1400],
    'bateria_horas': [8, 6, 10, 7, 12, 9],
    'peso_kg': [1.3, 1.5, 1.2, 1.4, 1.1, 1.25]
}
df = pd.DataFrame(datos)

matriz_corr = df[['precio', 'bateria_horas', 'peso_kg']].corr()

sns.heatmap(data=matriz_corr, annot=True)
plt.show()

sns.regplot(x='precio', y='bateria_horas', data=df)
plt.show()

sns.regplot(x='precio', y='peso_kg', data=df)
plt.show()
df.to_csv(f'{path}/correlation_2.csv')