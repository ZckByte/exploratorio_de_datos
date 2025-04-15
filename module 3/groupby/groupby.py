#! 📘 Agrupación de datos (groupby)

# ? ¿Para qué sirve groupby?
# Agrupa los datos por categorías y permite calcular estadísticas por grupo.

# ! df.groupby('traccion')['precio'].mean()
# → Precio medio por tipo de tracción

# También podés agrupar por más de una columna:
# ! df.groupby(['traccion', 'carroceria'])['precio'].mean()

# ? ¿Y si quiero una tabla más clara?
# * Tabla dinámica (pivot table)
# ! df.pivot_table(values='precio', index='traccion', columns='carroceria')

# ? ¿Y cómo visualizarlo mejor?
# * Mapa de calor (heatmap)
# ! sns.heatmap(tabla_pivot, annot=True, cmap='RdBu')
