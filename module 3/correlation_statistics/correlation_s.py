#! 📊 Correlación de Pearson

# ? ¿Qué es?
# Es una fórmula que mide la fuerza y dirección de la relación entre dos variables numéricas.

# ! from scipy import stats
# ! coef, p = stats.pearsonr(df['tamano_motor'], df['precio'])

# * coef → entre -1 y 1 (fuerza y dirección)
# * p → valor de certeza

# Interpretación:
# coef ≈ 1 → fuerte correlación positiva
# coef ≈ -1 → fuerte correlación negativa
# coef ≈ 0 → sin correlación

# p < 0.001 → certeza alta
# p entre 0.001 y 0.05 → moderada
# p entre 0.05 y 0.1 → débil
# p > 0.1 → no hay certeza

# ? ¿Y si quiero ver la correlación entre muchas columnas?
# * Mapa de calor de correlación:
# ! sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
