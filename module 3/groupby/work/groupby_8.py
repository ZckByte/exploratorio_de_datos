import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"

# Ejercicio 29 – Análisis de asistencia por curso y materia
# Crear el DataFrame 

# Crear una tabla dinámica (pivot_table) donde:
# index='curso'
# columns='materia'
# values='asistencia_pct'
# aggfunc='mean'
# Mostrar el resultado como un heatmap con annot=True y cmap='YlGnBu'
# Exportar la tabla como asistencia_pivot.csv

datos = {
    'estudiante': [
        'Lucía', 'Tomás', 'Sofía', 'Mateo', 'Valentina',
        'Joaquín', 'Camila', 'Martín', 'Emilia'
    ],
    'curso': ['A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A'],
    'materia': [
        'Matemática', 'Historia', 'Matemática', 'Historia', 'Historia',
        'Matemática', 'Matemática', 'Historia', 'Historia'
    ],
    'asistencia_pct': [95, 90, 100, 75, 98, 85, 99, 70, 94]
}


df = pd.DataFrame(datos)
pivot = df.pivot_table(values='asistencia_pct', columns='materia', index='curso', aggfunc='mean')
plt.figure()
sns.heatmap(pivot, annot=True)
plt.title('Asistencia por curso')
plt.xlabel('Materia')
plt.ylabel('Curso')
plt.show()

pivot.to_csv(f'{path}/asistencia_pivot.csv')
