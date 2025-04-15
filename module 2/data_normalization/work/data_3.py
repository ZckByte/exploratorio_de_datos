import pandas as pd
import func
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"
# Ejercicio 10 – Rendimiento de servidores
# Normalizá las columnas uso_cpu, uso_memoria_gb y temp_c usando:

# Simple Scaling
# Z-Score

# Agregá una columna booleana llamada riesgo_alto, que sea True si:

# El uso de CPU z-score es mayor a 1.0
# Y la temperatura z-score también es mayor a 1.0

# Ordená las columnas de forma clara y exportá el archivo como data_3.csv.

datos = {
    'servidor': ['servidor-1', 'servidor-2', 'servidor-3', 'servidor-4'],
    'uso_cpu': [45, 87, 10, 95],
    'uso_memoria_gb': [32, 64, 28, 72],
    'temp_c': [55, 70, 40, 85]
}
df = pd.DataFrame(datos)
#1
#Simple
func.metodo_simple('uso_cpu', df, 'uso_cpu_simple')
func.metodo_simple('uso_memoria_gb', df, 'uso_memoria_simple')
func.metodo_simple('temp_c', df, 'temp_c_simple')
#Z-Score
func.metodo_z('uso_cpu', df, 'uso_cpu_z')
func.metodo_z('uso_memoria_gb', df, 'uso_memoria_z')
func.metodo_z('temp_c', df, 'temp_c_z')
#2

riesgo_alto = False
df['riesgo_alto'] = (df['uso_cpu_z'] > 1.0) & (df['temp_c_z'] > 1.0)
df['riesgo_alto'] = riesgo_alto

df = df[['servidor', 'uso_cpu', 'uso_cpu_simple', 'uso_cpu_z',
         'uso_memoria_gb', 'uso_memoria_simple', 'uso_memoria_z',
         'temp_c', 'temp_c_simple', 'temp_c_z',
         'riesgo_alto']]
df.to_csv(f'{path}/data_3.csv')