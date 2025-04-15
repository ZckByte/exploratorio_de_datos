#! 📘 Módulo 2 – Limpieza y preparación de datos en Python (Resumen)

# ? ¿Qué aprendí en este módulo?

# 🔹 1. Formato de datos
# Aprendiste a unificar datos inconsistentes de distintas fuentes.
# Ej: "New York", "NY", "nyc" → todos deben decir lo mismo.

# 🔹 2. Conversión de unidades
# Convertiste datos como millas por galón a litros/100km:
# ! df['city-L/100km'] = 235 / df['city-mpg']

# 🔹 3. Tipos de datos
# Convertiste columnas de texto a numérico:
# ! df['precio'] = df['precio'].astype(int)

# 🔹 4. Valores faltantes
# Detectaste y reemplazaste valores como "N/A", NaN o celdas vacías.
# Reemplazaste:
# - con promedio (números)
# - con moda (texto)

# 🔹 5. Normalización de datos
# Aprendiste a aplicar:
# ! Simple Scaling → x / x_max
# ! Min-Max Scaling → (x - min) / (max - min)
# ! Z-Score → (x - media) / std

# 🔹 6. Binning
# Agrupaste variables numéricas en rangos usando:
# ! np.linspace() + pd.cut()
# También visualizaste bins con histogramas.

# 🔹 7. One Hot Encoding
# Convertiste variables categóricas (como "fuel") a numéricas:
# ! pd.get_dummies(df['fuel'])

# Y uniste los resultados con:
# ! df = pd.concat([df, dummies], axis=1)