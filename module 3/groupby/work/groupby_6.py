import pandas as pd
import matplotlib.pyplot as plt
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"

# jercicio 27 – Estadísticas de atención al cliente por canal y agente
# Crear el DataFrame.
# Agrupar por agente y canal, y calcular:
# Total de tickets resueltos
# Promedio de tiempo de respuesta
# Crear un resumen y exportarlo como atencion_resumen.csv
# (Opcional) Graficar los tickets resueltos por agente.
datos = {
    'agente': ['Laura', 'Tomás', 'Laura', 'Carla', 'Tomás', 'Carla', 'Laura', 'Tomás'],
    'canal': ['Chat', 'Teléfono', 'Email', 'Chat', 'Chat', 'Teléfono', 'Teléfono', 'Email'],
    'tickets_resueltos': [25, 18, 12, 20, 15, 19, 17, 10],
    'tiempo_promedio_min': [4.5, 6.2, 10.1, 5.2, 4.9, 6.0, 6.5, 9.5]
}
df = pd.DataFrame(datos)
total_resueltos = df.groupby(['agente', 'canal'])['tickets_resueltos'].sum()
promedio_tiempo = df.groupby(['agente', 'canal'])['tiempo_promedio_min'].mean()

resumen4 = pd.concat([total_resueltos, promedio_tiempo], axis=1)
resumen4.columns = ['Total Tickets Resueltos', 'Tiempo de respuesta promedio']
resumen4.reset_index(inplace=True)

df.groupby(['agente'])['tickets_resueltos'].sum().plot(kind='barh')
plt.xlabel('Resueltos')
plt.ylabel('Agente')
plt.title('Tickets Resueltos Por Agente')
plt.show()

resumen4.to_csv(f'{path}/atencion_resumen.csv')
df.to_csv(f'{path}/groupby_5.csv')