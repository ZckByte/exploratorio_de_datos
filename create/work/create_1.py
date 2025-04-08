# nombre	edad	grado	promedio
# Laura	    16	     10	      4.2
# Andrés	15	     9	      3.8
# Camila	17	     11	      4.5
# Mateo	    16	     10	      3.2
# Valentina	15	     9	      4.0

import pandas as pd

datos={
    'nombre': ['Laura','Andres','Camila','Mateo','Valentina'],
    'edad': [16,15,17,16,15],
    'grado': [10, 9, 11, 10, 9],
    'promedio': [4.2,3.8,4.5,3.2,4.0]
}

df_estudiantes = pd.DataFrame(datos)

df_estudiantes.to_csv('C:\datos\csv,xlsx,etc\estudiantes.csv')