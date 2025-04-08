import pandas as pd

df = pd.read_csv('C:\datos\csv,xlsx,etc\estudiantes.csv')
df_filtado = df[df['promedio'] == 4.0]

print(df_filtado)