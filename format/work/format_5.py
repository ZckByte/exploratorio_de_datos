# Ejercicio 8 – Datos de ventas en tienda física

# Convertir unidades_vendidas y precio_unitario a numérico.

# Reemplazar "N/A" por el promedio del precio.

# Unificar fecha_venta a formato "YYYY-MM-DD".

# Estandarizar forma_pago en minúsculas ("efectivo" / "tarjeta").

# Normalizar categoria → todo en minúsculas y sin tildes ("perifericos", "pantallas", "cables").

import pandas as pd
import numpy as np
from dateutil import parser
import unicodedata

def quitar_tildes(texto):
    if isinstance(texto, str):
        texto_normalizado = unicodedata.normalize('NFD', texto)
        return ''.join(c for c in texto_normalizado if unicodedata.category(c) != 'Mn')
    return texto 

def parse_fecha(fecha):
    try:
        return parser.parse(fecha)
    except:
        return pd.NaT
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"

datos = {
    'producto': ['Mouse Logitech', 'Teclado HP', 'Monitor Samsung', 'Cable HDMI'],
    'unidades_vendidas': ["10", 8, "2", "5"],
    'precio_unitario': ["15.5", 20, "150", "N/A"],
    'fecha_venta': ['2023-06-01', '01/06/2023', '01.06.2023', '2023/06/01'],
    'forma_pago': ['Efectivo', 'tarjeta', 'EFECTIVO', 'Tarjeta'],
    'categoria': ['perifericos', 'Periféricos', 'Pantallas', 'cables']
}

df = pd.DataFrame(datos)

#1
df['unidades_vendidas'] = df['unidades_vendidas'].astype(int)

#2
df['precio_unitario'] = df['precio_unitario'].replace("N/A", np.nan)
df['precio_unitario'] = df['precio_unitario'].astype(float)

precio_promedio = df['precio_unitario'].mean()
df['precio_unitario'] = df['precio_unitario'].fillna(precio_promedio)

#3
df['fecha_venta'] = df['fecha_venta'].apply(parse_fecha)
df['fecha_venta'] = df['fecha_venta'].dt.strftime('%Y-%m-%d')

#4
df['forma_pago'] = df['forma_pago'].str.lower()

#5
df['categoria'] = df['categoria'].apply(quitar_tildes)
df.to_csv(f'{path}/format_5.csv')