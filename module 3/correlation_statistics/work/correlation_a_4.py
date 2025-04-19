import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy.stats import pearsonr
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"
def pearson(namedt, coe, p):
    coeficiente, pearsonrr = pearsonr(namedt[f'{coe}'],namedt[f'{p}'])
    print(f'Coeficiente {coe}: {coeficiente}')
    print(f'Pearson {p}: {pearsonrr}')
    print('')
    sns.regplot(x=coe, y=p, data=namedt)
    plt.title(f'Relacion {coe} - {p}')
    plt.xlabel(f'{coe}')
    plt.ylabel(f'{p}')
    plt.show()

# Crear el DataFrame
# Calcular la matriz de correlación con .corr() y visualizarla con sns.heatmap()
# Calcular el coeficiente de Pearson y valor P para cada variable contra el precio_usd
# Mostrar un gráfico regplot() por variable
# Exportar:
# El CSV como smartphones_correlacion.csv
# La matriz como matriz_smartphones.csv


datos = {
    'modelo': ['Phone A', 'Phone B', 'Phone C', 'Phone D', 'Phone E', 'Phone F', 'Phone G'],
    'precio_usd': [450, 600, 300, 750, 500, 680, 550],
    'pantalla_pulgadas': [6.1, 6.7, 5.8, 6.9, 6.4, 6.5, 6.2],
    'bateria_mAh': [3000, 4500, 2800, 5000, 4000, 4700, 4200],
    'nro_camaras': [2, 4, 2, 5, 3, 4, 3],
    'almacenamiento_gb': [64, 128, 64, 256, 128, 256, 128]
}

df = pd.DataFrame(datos)

correlacion = df[['precio_usd', 'pantalla_pulgadas', 'bateria_mAh', 'nro_camaras', 'almacenamiento_gb']].corr()
sns.heatmap(data=correlacion, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlacion')
plt.show()
correlacion.to_csv(f'{path}/matriz_smartphones.csv')

pearson(df, 'precio_usd', 'pantalla_pulgadas')
pearson(df, 'precio_usd', 'bateria_mAh')
pearson(df, 'precio_usd', 'nro_camaras')
pearson(df, 'precio_usd', 'almacenamiento_gb')


df.to_csv(f'{path}/correlation_a_4.csv')

