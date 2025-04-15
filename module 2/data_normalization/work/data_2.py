import pandas as pd
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"
def metodo_simple(columna, name_df, nueva_columna_nombre):
    simple = name_df[f'{columna}'] / name_df[f'{columna}'].max()
    name_df[f'{nueva_columna_nombre}'] = simple 

def metodo_min_max(columna, name_df, nueva_columna_nombre):
    min_max = (name_df[f'{columna}'] - name_df[f'{columna}'].min()) / (name_df[f'{columna}'].max() - name_df[f'{columna}'].min())
    name_df[f'{nueva_columna_nombre}'] = min_max 

def metodo_z(columna, name_df, nueva_columna_nombre):
    z_score = (name_df[f'{columna}'] - name_df[f'{columna}'].mean()) / name_df[f'{columna}'].std()
    name_df[f'{nueva_columna_nombre}'] = z_score 
# Ejercicio 9 – Datos de componentes electrónicos
# Normalizá las columnas:

# resistencia_ohm
# temperatura_max_c
# duracion_horas

# Aplicá los tres métodos:

# Simple scaling
# Min-max
# Z-score

# Guardá los resultados en nuevas columnas con nombres claros.

datos = {
    'componente': ['Resistor 1/4W', 'Capacitor Cerámico', 'Microcontrolador', 'Diodo Zener'],
    'resistencia_ohm': [220, 10, 33000, 5],
    'temperatura_max_c': [85, 105, 125, 75],
    'duracion_horas': [5000, 10000, 12000, 8000]
}
df = pd.DataFrame(datos)

#1

#Simple
metodo_simple('resistencia_ohm', df, 'resistencia_simple')
metodo_simple('temperatura_max_c', df, 'temperatura_simple')
metodo_simple('duracion_horas', df, 'duracion_simple')

#Min-Max
metodo_min_max('resistencia_ohm', df, 'resistencia_min_max')
metodo_min_max('temperatura_max_c', df, 'temperatura_min_max')
metodo_min_max('duracion_horas', df, 'duracion_min_max')

#Z-Score
metodo_z('resistencia_ohm', df, 'resistencia_z')
metodo_z('temperatura_max_c', df, 'temperatura_z')
metodo_z('duracion_horas', df, 'duracion_z')

#2

df = df[['componente','resistencia_ohm','resistencia_simple','resistencia_min_max','resistencia_z',
         'temperatura_max_c','temperatura_min_max','temperatura_z','duracion_horas','duracion_simple',
         'duracion_min_max','duracion_z']]

df.to_csv(f'{path}/data_2.csv')