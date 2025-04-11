from dateutil import parser
import pandas as pd

def parse_fecha(fecha):
    try:
        return parser.parse(fecha)
    except:
        return pd.NaT
    
# Propósito: Convierte fechas con diferentes formatos en un objeto de tipo datetime.

#* try:
#*     return parser.parse(fecha)

# Usa dateutil.parser, que es más flexible que pd.to_datetime().

# Reconoce casi cualquier formato de fecha:
# "01/02/2023"
# "2023-02-01"
# "02.01.2023", etc.

#* except:
#*     return pd.NaT

# Si no puede interpretar la fecha, 
# en lugar de romper el código, devuelve NaT (como NaN, pero para fechas).

#? ¿Cuándo usarla?
# Cuando tus fechas vienen en formatos mixtos y pd.to_datetime() falla.

# Para limpiar una columna antes de aplicar filtros por fecha,
# agrupar por mes, año, etc.

#TIP
#TODO parser.parse() 
#TODO devuelve un objeto datetime, que después podés formatear o usar para análisis.