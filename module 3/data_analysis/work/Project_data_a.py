import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"
#  Proyecto – Análisis de rendimiento de estudiantes
# Crear el DataFrame con los datos.

# Usar .describe() para analizar edad, nota_final, y asistencia_pct.
# Usar .value_counts() para ver cuántos estudiantes hay por clase.
# Mostrar un boxplot de nota_final por clase.

# Hacer un scatter plot entre asistencia_pct y nota_final.
# Exportar el análisis como CSVs: alumnos.csv y resumen_alumnos.csv

datos = {
    'estudiante': [
        'Lucía Fernández', 'Mateo Díaz', 'Sofía García', 'Tomás López',
        'Valentina Torres', 'Joaquín Pérez', 'Camila Ríos',
        'Martín Ramírez', 'Emilia Castro', 'Santiago Ruiz'
    ],
    'clase': ['A', 'B', 'A', 'B', 'A', 'C', 'C', 'B', 'C', 'A'],
    'edad': [16, 17, 16, 17, 15, 18, 17, 16, 17, 15],
    'nota_final': [8.5, 7.8, 9.1, 6.9, 8.7, 7.0, 9.0, 6.5, 8.2, 7.5],
    'asistencia_pct': [95, 85, 100, 75, 92, 80, 98, 60, 90, 88]
}
df = pd.DataFrame(datos)
#1
df.describe().to_csv(f'{path}/resumen_project_data_a.csv')
#2
plt.figure()
df['clase'].value_counts().plot(kind='bar', title='Estudiantes por Clase')
plt.ylabel('Cantidad')
plt.xlabel('Clase')
#3
df.boxplot(column='nota_final', by='clase')
plt.title('Nota Final por Clase')
plt.ylabel('Nota Final')
plt.xlabel('Clase')
plt.suptitle('')
#4
plt.figure()
plt.scatter(df['asistencia_pct'], df['nota_final'])
for i in range(len(df)):
    plt.text(df['asistencia_pct'][i]+0.5, df['nota_final'][i], df['clase'][i], fontsize=8)
plt.title('Asistencia vs Nota Final')
plt.xlabel('Asistencia')
plt.ylabel('Nota Final')
plt.savefig(f'{path}/grafico_scatter_asistencia.png')
plt.show()
df.to_csv(f'{path}/project_data_a.csv')