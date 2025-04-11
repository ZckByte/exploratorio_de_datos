#! Formato y tipos de datos en un DataFrame

# ? ¿Qué es el "formato" de los datos?
# Cuando recibimos datos de distintas fuentes o personas,
# los valores pueden venir escritos o estructurados de maneras diferentes.

# Ejemplo: "New York", "NY", "N.Y.", "Ny" → todos representan lo mismo, pero están escritos distinto.

# Esto puede causar problemas al comparar, agrupar o analizar.
# Por eso conviene unificar los valores para tener un formato estándar.

# ? ¿Y si quiero detectar anomalías?
# A veces los formatos distintos ayudan (como escribir "N.Y." en lugar de "New York"),
# especialmente en análisis como detección de fraude.

# Pero en general, para limpieza de datos, se recomienda unificar el formato.

# ? Ejemplo de conversión de unidades:
# Si tenemos consumo de gasolina en millas por galón (mpg) y usamos sistema métrico...

# * Se usa esta fórmula: 
# ! 235 / mpg = litros cada 100km

# ? df['city-mpg'] = 235 / df['city-mpg'] 
# Esto convierte la columna de mpg a litros/100km

# Luego puedes renombrar la columna:
# ? df.rename(columns={'city-mpg': 'city-L/100km'}, inplace=True)

# ? Tipos de datos en pandas

# Al importar datos, a veces pandas asigna el tipo incorrecto.
# Por ejemplo, una columna de precios puede aparecer como tipo "object" (texto)
# en lugar de int o float.

# Esto puede causar errores al hacer cálculos o análisis.

# ? ¿Cómo saber el tipo de cada columna?
# ? df.dtypes

# ! Tipos comunes:
# object → texto
# int64  → números enteros
# float64 → números decimales

# ? ¿Cómo cambiar el tipo de una columna?
# ? df['columna'] = df['columna'].astype('tipo')

# Ejemplo:
# ? df['precio'] = df['precio'].astype(int)
# Esto convierte la columna precio de texto a entero.

# Es importante asegurarse que los datos estén en el tipo correcto
# para evitar errores al analizarlos o crear modelos.
