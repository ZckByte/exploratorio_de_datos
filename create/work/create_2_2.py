import pandas as pd
path = "C:/datos/csv,xlsx,etc"
df = pd.read_csv(f'{path}/notas.csv')

df_filtrado = df[df['notas'] >= 2]
print(df.loc[:, 'nombres'])