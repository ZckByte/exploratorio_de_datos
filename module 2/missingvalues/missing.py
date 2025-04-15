
#! Datos faltantes en un dataframe 

# ?¿Qué es un valor faltante?
# Cuando en una tabla de datos (como un DataFrame) 
# falta el valor de alguna columna para una fila,
# se dice que ese dato está faltando. Aparece como:

# NaN (Not a Number)

# ?

# N/A

# 0 (aunque no siempre es faltante)

# o simplemente una celda vacía

# ?¿Qué hacer cuando hay valores faltantes?

# 1. Intentar conseguir el dato original
# Si alguien puede consultar la fuente del dato, eso es lo mejor.

# 2. Eliminar los datos faltantes
# Se puede elimina toda la fila que tenga valores faltantes → #!con axis=0
# O eliminar la columna entera → #!con axis=1

# Solo conviene si hay muy pocos valores faltantes.

# ? df.dropna(axis=0, inplace=True) Elimina filas con NaN

#inplace=True Cambia el DataFrame original directamente

# 3. Reemplazar los datos faltantes
# Si es un número: usar el promedio #!(mean())

# #? promedio = df['normalized-losses'].mean()

# ? df['normalized-losses'].replace(np.nan, promedio, inplace=True) 

# !np.nan 
# representa un valor "Not a Number" (no es un número). 
# Es la forma estándar que usa Python (vía NumPy) 
# para marcar datos faltantes o inválidos en variables numéricas.