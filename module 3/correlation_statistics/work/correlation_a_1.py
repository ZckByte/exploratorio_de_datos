import pandas as pd
from scipy.stats import pearsonr
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"

datos = {
    'modelo': ['Cel A', 'Cel B', 'Cel C', 'Cel D', 'Cel E', 'Cel F'],
    'precio': [500, 650, 400, 800, 550, 700],
    'bateria_mAh': [3000, 4000, 2800, 5000, 3500, 4500]
}


df = pd.DataFrame(datos)

coef, p = pearsonr(df['precio'], df['bateria_mAh'])
print('Coeficiente de Pearson:', coef)
print('Valor P:', p)

df.to_csv(f'{path}/correlation_a_1.csv')
