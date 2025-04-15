#! 📐 Correlación entre variables

# ? ¿Qué es la correlación?
# Es una medida de cuánto cambia una variable cuando cambia otra.
# - Positiva: sube una, sube la otra
# - Negativa: sube una, baja la otra
# - Cero: no hay relación

# ? ¿Cómo verla visualmente?
# * Gráfico de dispersión + línea de regresión:
# ! sns.regplot(x='tamano_motor', y='precio', data=df)

# Si la línea sube → correlación positiva
# Si la línea baja → negativa
# Si no hay forma → débil o nula
