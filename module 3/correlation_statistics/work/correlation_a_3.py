import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy.stats import pearsonr
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"

# Crear el DataFrame
# Calcular correlación con .corr() y mostrarla con sns.heatmap()
# Usar pearsonr() entre:
# precio_usd y resolucion_mp
# precio_usd y zoom_optico
# precio_usd y peso_g
# Visualizar cada relación con sns.regplot()
# Exportar el CSV como correlation_camaras.csv

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
datos = {
    'modelo': ['Cam A', 'Cam B', 'Cam C', 'Cam D', 'Cam E', 'Cam F'],
    'precio_usd': [450, 600, 300, 750, 500, 680],
    'resolucion_mp': [20.1, 24.2, 16.0, 30.4, 22.0, 26.2],
    'zoom_optico': [3, 4, 2, 5, 3, 4],
    'peso_g': [450, 520, 380, 580, 470, 530]
}

df = pd.DataFrame(datos)

correlacion = df[['precio_usd', 'resolucion_mp', 'zoom_optico', 'peso_g']].corr()
sns.heatmap(data=correlacion, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlacion')
plt.show()

pearson(df, 'precio_usd', 'resolucion_mp')
pearson(df, 'precio_usd', 'zoom_optico')
pearson(df, 'precio_usd', 'peso_g')

df.to_csv(f'{path}/correlation_a_3.csv')
