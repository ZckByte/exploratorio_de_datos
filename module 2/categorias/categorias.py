#! Transformar variables categóricas en variables numéricas

# ? ¿Por qué?
# La mayoría de los modelos estadísticos o de machine learning solo aceptan números.
# No pueden trabajar directamente con texto o strings.

# ? Ejemplo:
# Supongamos que tenés una columna "fuel" con los valores:
# - "gas"
# - "diesel"

# Estos son valores categóricos. Para analizarlos, hay que convertirlos en números.

# ? ¿Cómo lo hacemos?
# Usamos una técnica llamada:
# ! One Hot Encoding

# ? ¿Qué es One Hot Encoding?
# Crea una nueva columna por cada valor único de la variable original.

# Ejemplo:
# Si tenés "fuel" con dos categorías: "gas" y "diesel"
# Se crean dos columnas nuevas:
# - una llamada "gas"
# - otra llamada "diesel"

# En cada fila:
# - Si el valor original era "gas", la columna "gas" tendrá 1 y "diesel" tendrá 0.
# - Si el valor era "diesel", la columna "diesel" tendrá 1 y "gas" tendrá 0.

# ? ¿Cómo se hace en pandas?

# ! pd.get_dummies(df['fuel'])

# Esto genera un nuevo DataFrame con las columnas binarias (0 o 1).

# ? ¿Cómo agregar esas columnas al DataFrame original?

# Podés hacer algo así:
# ! dummy = pd.get_dummies(df['fuel'])
# ! df = pd.concat([df, dummy], axis=1)

# ? ¿Y si querés eliminar la columna original?
# Simplemente hacé:
# ! df.drop('fuel', axis=1, inplace=True)

# ? ¿Cuándo usar esto?
# - Antes de entrenar modelos
# - Cuando querés analizar relaciones entre variables categóricas y numéricas
