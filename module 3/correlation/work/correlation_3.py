import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"

# Ejercicio 33 – Correlación en especificaciones de celulares
# Crear el DataFrame
# Calcular la matriz de correlación (.corr())
# Visualizar la matriz con un heatmap (sns.heatmap())
# Crear tres gráficos regplot():
# precio vs bateria_mAh
# precio vs nro_camaras
# precio vs almacenamiento_gb
# Exportar el CSV como correlation_3.csv

datos = {
    'modelo': ['Cel A', 'Cel B', 'Cel C', 'Cel D', 'Cel E', 'Cel F'],
    'precio': [500, 650, 400, 800, 550, 700],
    'bateria_mAh': [3000, 4000, 2800, 5000, 3500, 4500],
    'nro_camaras': [2, 3, 2, 4, 2, 3],
    'almacenamiento_gb': [64, 128, 64, 256, 128, 256]
}

df = pd.DataFrame(datos)
corre_matriz = df[['precio', 'bateria_mAh', 'nro_camaras', 'almacenamiento_gb']].corr()

sns.heatmap(data=corre_matriz, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlacion')
plt.show()

sns.regplot(x='precio', y='bateria_mAh', data=df)
plt.title('Correlacion Precio - Bateria')
plt.ylabel('Bateria')
plt.xlabel('Precio')
plt.show()
sns.regplot(x='precio', y='nro_camaras', data=df)
plt.title('Correlacion Precio - Nro Camaras')
plt.xlabel('Precio')
plt.ylabel('Nro Camaras')
plt.show()
sns.regplot(x='precio', y='almacenamiento_gb', data=df)
plt.title('Correlacion Precio - Almacenamiento')
plt.xlabel('Precio')
plt.ylabel('Almacenamiento')
plt.show()
df.to_csv(f'{path}/correlation_3.csv')