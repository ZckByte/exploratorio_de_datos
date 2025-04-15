import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import func
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"

#Ejercicio 13 – Análisis de sensores ambientales
# Crear una columna nueva llamada nivel_temp dividiendo temp_c en 3 grupos:

# 'baja'
# 'media'
# 'alta'

# Usá np.linspace() + pd.cut() para agrupar según los valores de temperatura una vez corregidos y limpiados.

# 🧠 Paso a paso (actualizado):
# Crear el DataFrame.
# Unificar la columna ciudad → "Buenos Aires"
# Convertir columnas numéricas (temp_c, humedad_%, altitud_m)
# Reemplazar "N/A" con np.nan

# Rellenar:

# Números → promedio
# Texto (calidad_aire) → moda

# Normalizar las columnas numéricas con Z-score.
# Agrupar temp_c en 3 niveles de temperatura con pd.cut()

# Exportar como sensores_limpio.csv

datos = {
    'sensor_id': ['S-001', 'S-002', 'S-003', 'S-004', 'S-005'],
    'ciudad': ['bs.as', 'Bs.As.', 'B.A.', 'b.a.s', 'bsas'],
    'temp_c': [25.0, 'N/A', 28, '30', 22],
    'humedad_%': [50, '65', 'N/A', 55, 'N/A'],
    'calidad_aire': ['buena', 'regular', 'buena', None, 'mala'],
    'altitud_m': [25, 30, '35', 30, 'N/A']
}

df = pd.DataFrame(datos)

df['ciudad'] = df['ciudad'].replace(
    dict.fromkeys(['bs.as', 'Bs.As.', 'bsas', 'B.A.', 'b.a.s',  'buenos aires'], 'Buenos Aires')
).str.title()

func.reemplazar_NA_con_promedio('temp_c', df)
func.reemplazar_NA_con_promedio('humedad_%', df)
func.reemplazar_NA_con_promedio('altitud_m', df)

calidad_moda = df['calidad_aire'].mode()[0]
df['calidad_aire'] = df['calidad_aire'].fillna(calidad_moda)


func.metodo_z('temp_c',df,'temp_c_z')
func.metodo_z('humedad_%',df,'humedad_%_z')
func.metodo_z('altitud_m',df,'altitud_m_z')

groups = ['baja', 'media', 'alta']
bins = np.linspace(df['temp_c'].min(), df['temp_c'].max(), 4)
df['nivel_temp'] = pd.cut(df['temp_c'], bins, labels=groups, include_lowest=True)

df = df[['sensor_id','ciudad','temp_c','nivel_temp','temp_c_z', 
        'humedad_%','humedad_%_z','calidad_aire','altitud_m','altitud_m_z'
         ]]

df['nivel_temp'].value_counts().plot(kind='bar')
plt.show()

df.to_csv(f'{path}/binning_3.csv')