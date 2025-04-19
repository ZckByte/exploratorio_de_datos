import pandas as pd
from scipy.stats import pearsonr
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"

def pearson(namedt, coe, p):
    coeficiente, pearsonrr = pearsonr(namedt[f'{coe}'],namedt[f'{p}'])
    print(f'Coeficiente {coe}: {coeficiente}')
    print(f'Pearson {p}: {pearsonrr}')
    print('')

datos = {
    'modelo': ['Laptop A', 'Laptop B', 'Laptop C', 'Laptop D', 'Laptop E', 'Laptop F'],
    'precio': [900, 1200, 800, 1500, 1000, 1300],
    'ram_gb': [8, 16, 8, 32, 12, 16],
    'bateria_horas': [6, 9, 5, 12, 7, 10],
    'peso_kg': [2.0, 2.5, 1.8, 2.8, 2.2, 2.6]
}
df = pd.DataFrame(datos)

pearson(df, 'precio', 'ram_gb')
pearson(df, 'precio', 'bateria_horas')
pearson(df, 'precio', 'peso_kg')

df.to_csv(f'{path}/correlation_a_2.csv')
