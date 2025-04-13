import func 
import pandas as pd
import numpy as np

def metodo_simple(columna, name_df, nueva_columna_nombre):
    simple = name_df[f'{columna}'] / name_df[f'{columna}'].max()
    name_df[f'{nueva_columna_nombre}'] = simple 

def metodo_min_max(columna, name_df, nueva_columna_nombre):
    min_max = (name_df[f'{columna}'] - name_df[f'{columna}'].min()) / (name_df[f'{columna}'].max() - name_df[f'{columna}'].min())
    name_df[f'{nueva_columna_nombre}'] = min_max 

def metodo_z(columna, name_df, nueva_columna_nombre):
    z_score = (name_df[f'{columna}'] - name_df[f'{columna}'].mean()) / name_df[f'{columna}'].std()
    name_df[f'{nueva_columna_nombre}'] = z_score 

def reemplazar_NA_con_promedio(columna, name_df):
    name_df[f'{columna}'] = name_df[f'{columna}'].replace("N/A", np.nan)
    name_df[f'{columna}'] = name_df[f'{columna}'].astype(float)
    promedio = name_df[f'{columna}'].mean().round(1)
    name_df[f'{columna}'] = name_df[f'{columna}'].fillna(promedio)