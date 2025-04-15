# Ejercicio 6 – Análisis de reseñas de productos tecnológicos

# Convertir calificación y precio a tipo numérico.

# Reemplazar "N/A" en calificación por la media de las calificaciones válidas.

# Unificar todas las fechas en el formato "YYYY-MM-DD" usando pd.to_datetime().

# Convertir todos los comentarios a minúsculas.

# Eliminar cualquier espacio adicional al principio o final de los comentarios.
import pandas as pd
import numpy as np
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"
datos = {
    'producto': ['Laptop HP', 'Smartwatch Xiaomi', 'Auriculares Sony', 'Teclado Logitech'],
    'calificacion': ["5", 4, "N/A", 3],
    'fecha_compra': ['2023-08-15', '2023/07/10', '10-06-2023', '2023.05.01'],
    'comentario': ['Excelente producto', 'Muy bueno!', 'sonido espectacular', ' cómodo pero frágil '],
    'precio': [850, "500", 250, 100]
}

df = pd.DataFrame(datos)

#1
df['precio'] = df['precio'].astype(int)

#2
df['calificacion'] = df['calificacion'].replace("N/A",np.nan)
df['calificacion'] = df['calificacion'].astype(float)

calificacion_promedio = df['calificacion'].mean()
df['calificacion'] = df['calificacion'].fillna(calificacion_promedio)

#3
df['fecha_compra'] = pd.to_datetime(df['fecha_compra'], errors='coerce', dayfirst=False)
df['fecha_compra'] = df['fecha_compra'].dt.strftime('%Y-%m-%d')
print(df['fecha_compra'].isna())



#4
df['comentario'] = df['comentario'].str.lower()

#5
df['comentario'] = df['comentario'].str.strip()

df.to_csv(f'{path}/format_3.csv')