import unicodedata

def quitar_tildes(texto):
    if isinstance(texto, str):
        texto_normalizado = unicodedata.normalize('NFD', texto)
        return ''.join(c for c in texto_normalizado if unicodedata.category(c) != 'Mn')
    return texto 


#!      quitar_tildes(texto)

# Propósito: Elimina las tildes o acentos de un texto.
# Ejemplo: "Periféricos" → "Perifericos"

#* if isinstance(texto, str):

# Primero verifica que lo que recibe sea una cadena de texto. 
# Si no lo es, lo devuelve tal como está (para no romper el código).

#*      texto_normalizado = unicodedata.normalize('NFD', texto)

#Convierte cada letra con tilde en dos símbolos: la letra + el acento.

#* Ej: "é" → "e" + " ́"
# Esto se llama descomposición canónica.

#?     return ''.join(c for c in texto_normalizado if unicodedata.category(c) != 'Mn')

# Recorre cada carácter y elimina los que son marcas de acento ('Mn' en Unicode).
# El resultado es el texto sin tildes.

#* return texto

#Si el valor no era texto, se devuelve sin tocar.

#? ¿Cuándo usarla?
# Al estandarizar columnas de texto: categorías, nombres de productos, ciudades, etc.
# Cuando querés hacer comparaciones sin preocuparte por acentos.
# Ideal antes de agrupar o filtrar textos.

#TIP
#TODO unicodedata.normalize() es útil 
#TODO también si alguna vez querés convertir 
#TODO texto a formas comparables sin símbolos raros.