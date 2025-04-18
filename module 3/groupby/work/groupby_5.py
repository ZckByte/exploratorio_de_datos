import pandas as pd
import matplotlib.pyplot as plt
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"

# Ejercicio 26 – Evaluación de rendimiento académico por materia y curso
# Crear el DataFrame.
# Agrupar por curso y materia y calcular:
# Promedio de nota_final
# Promedio de asistencia_pct
# Crear un nuevo DataFrame con estos resultados y exportarlo.
# (Opcional) Graficar los promedios de nota por curso en un gráfico de barras.

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
    'nota_final': [8.5, 7.8, 9.1, 6.9, 8.7, 7.0, 9.0, 6.5, 8.2],
    'asistencia_pct': [95, 90, 100, 75, 98, 85, 99, 70, 94]
}

df = pd.DataFrame(datos)
promedio_final = df.groupby(['curso', 'materia'])['nota_final'].mean()
promedio_asistencia = df.groupby(['curso', 'materia'])['asistencia_pct'].mean().round(1)

resumen3 = pd.concat([promedio_final, promedio_asistencia], axis=1)
resumen3.columns = ['Promedio Nota', 'Promedio Asistencia']
resumen3.reset_index(inplace=True)

resumen3.to_csv(f'{path}/resumen3.csv')
df.to_csv(f'{path}/groupby_5.csv')