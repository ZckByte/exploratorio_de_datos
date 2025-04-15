#! 📊 Estadística descriptiva básica en pandas

# ? ¿Cómo obtener estadísticas rápidas?
# ! df.describe()
# Te da: count, mean, std, min, 25%, 50% (mediana), 75%, max
# Solo aplica a columnas numéricas.
# NaN se ignoran automáticamente.

# ? ¿Y si la columna es categórica?
# ! df['col'].value_counts()
# Cuenta cuántas veces aparece cada categoría.

# ? ¿Y para ver distribución de valores?
# * Diagrama de caja (boxplot)
# Muestra mediana, cuartiles, IQR y valores atípicos.
# ! df.boxplot(column='precio', by='traccion')

# * Gráfico de dispersión (scatter plot)
# Muestra relación entre 2 variables numéricas:
# eje x → variable predictora
# eje y → variable objetivo
# ! plt.scatter(df['tamano_motor'], df['precio'])

# Puedes ver si hay relación lineal entre dos variables.
