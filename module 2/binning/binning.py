#! Agrupación en intervalos (binning)

# ? ¿Qué es binning?
# Es una técnica de preprocesamiento de datos donde agrupamos valores numéricos en rangos.
# Se usa para simplificar, entender mejor la distribución o mejorar modelos predictivos.

# ? Ejemplo clásico:
# Agrupar edades en:
# - 0 a 5 años
# - 6 a 10 años
# - 11 a 15 años
# Esto convierte una columna numérica en una columna categórica.

# ? ¿Para qué sirve?
# - Puede mejorar la precisión de algunos modelos.
# - Facilita la interpretación de los datos.
# - Reduce la variabilidad de datos numéricos.

# ? Caso real:
# Tenemos un atributo "precio" que va de 5,000 a 45,500.
# Lo podemos agrupar en:
# * bajo → low
# * medio → medium
# * alto → high

# ? ¿Cómo se hace en Python?

# 1. Definir los bordes de los grupos:
# ? bins = np.linspace(valor_min, valor_max, cantidad_bins + 1)

# Esto crea un arreglo con números igualmente espaciados, que serán los cortes entre bins.

# 2. Crear los nombres de cada grupo:
# ? group_names = ['low', 'medium', 'high']

# 3. Aplicar binning con pandas:
# ? df['nueva_columna'] = pd.cut(df['columna_original'], bins, labels=group_names, include_lowest=True)

# * Esto divide los datos en los grupos definidos por los bins.

# ? Visualizar los bins:
# Podés usar un histograma para ver la distribución:
# ? df['nueva_columna'].value_counts().plot(kind='bar')

# * También podés usar histogramas sobre la variable original para ver cómo se distribuye con los bins:
# ? df['columna_original'].hist(bins=cantidad_bins)

# ? Ejemplo final:
# Si la columna 'price' tiene valores entre 5,188 y 45,400 y queremos 3 grupos:
# ? bins = np.linspace(5188, 45400, 4)
# ? group_names = ['low', 'medium', 'high']
# ? df['binned_price'] = pd.cut(df['price'], bins, labels=group_names, include_lowest=True)
