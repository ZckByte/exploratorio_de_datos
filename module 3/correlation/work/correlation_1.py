import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"

#Relación entre tamaño de motor y precio de autos
#Crear el DataFrame

# Calcular la correlación entre tamaño_motor y precio con .corr()
# Graficar la relación con sns.regplot(x='tamaño_motor', y='precio', data=df)
# (Opcional) Mostrar también un heatmap de la correlación

datos = {
    'modelo': ['Auto A', 'Auto B', 'Auto C', 'Auto D', 'Auto E', 'Auto F'],
    'tamaño_motor': [1.6, 2.0, 2.2, 1.8, 3.0, 2.5],
    'precio': [15000, 22000, 25000, 18000, 35000, 30000]
}

df = pd.DataFrame(datos)
correlacion = df[['tamaño_motor', 'precio']].corr()
sns.regplot(x='tamaño_motor', y='precio', data=df)
plt.show()
sns.heatmap(correlacion, annot=True, cmap='coolwarm')
plt.title('Correlación entre variables')
plt.show()

df.to_csv(f'{path}/correlation_1.csv')