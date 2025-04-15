#! Normalización de datos

# ? ¿Qué es la normalización?
# Es el proceso de escalar valores numéricos para que estén en un rango comparable.
# Ayuda a evitar que una variable con valores muy grandes domine el análisis o modelo.

# ? ¿Por qué es útil?
# Ejemplo: comparar ingreso (en miles) con edad (en decenas).
# Si no normalizás, el ingreso tendrá más peso en una regresión o agrupamiento, aunque no sea más importante.

# ? ¿Cuándo normalizar?
# - Cuando vas a usar modelos matemáticos (regresión, clustering, etc.)
# - Cuando querés comparar variables con diferentes rangos.

# ? Métodos de normalización comunes:

# ? 1. Simple Scaling
# Divide cada valor por el máximo de su columna.
# * Fórmula:
# ! x_new = x_old / x_max

# ? 2. Min-Max Scaling
# Escala el dato entre el mínimo y máximo, llevándolo a un rango de 0 a 1.
# * Fórmula:
# ! x_new = (x_old - x_min) / (x_max - x_min)

# ? 3. Z-Score (Estandarización)
# Centra los datos en 0 y los escala según la desviación estándar.
# Muy útil para detectar valores atípicos (outliers).
# * Fórmula:
# ! x_new = (x_old - media) / desviacion_estandar

# ? ¿Cómo se calcula cada cosa en pandas?

# ? Máximo:
# ! df['columna'].max()

# ? Mínimo:
# ! df['columna'].min()

# ? Media (promedio):
# ! df['columna'].mean()

# ? Desviación estándar:
# ! df['columna'].std()

# ? ¿Dónde se aplican estas técnicas?
# - Modelos de Machine Learning
# - Análisis estadísticos
# - Preparación de datos para visualización

# ? ¿Qué tener en cuenta?
# - No se deben normalizar columnas categóricas.
# - Siempre revisá si los datos tienen valores extremos antes de aplicar Z-Score.