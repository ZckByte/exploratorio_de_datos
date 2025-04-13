import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"

# Crear 4 grupos de rendimiento:

# "excelente"
# "bueno"
# "regular"
# "lento"

# Usar np.linspace() para generar los cortes automáticos.

# Crear la columna clasificacion_tiempo con pd.cut().

# Mostrar:

# El conteo por grupo.

# (Opcional) Un gráfico de pastel (kind='pie') o barras.

datos = {
    'agente': ['Laura', 'Martín', 'Ana', 'José', 'Carla', 'David'],
    'tiempo_respuesta_min': [3.5, 15.0, 7.2, 20.3, 1.5, 11.1]
}

df = pd.DataFrame(datos)
#1
groups = ['excelente', 'bueno', 'regular', 'lento']
#2
bins = np.linspace(df['tiempo_respuesta_min'].min(), df['tiempo_respuesta_min'].max(), 5)

#3
df['clasificacion_tiempo'] = pd.cut(df['tiempo_respuesta_min'], bins, labels=groups, include_lowest=True)

#4
df['clasificacion_tiempo'].value_counts().plot(kind='bar')
plt.show()

df.to_excel(f'{path}/binning_3.xlsx')
