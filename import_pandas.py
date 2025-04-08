import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data" 

#df es la variable la cual almacena los datos sacados de la url, que lo esta leyendo con
#pandas como csv(tambien se puede con json, excel,etc)

df = pd.read_csv(url, header = None) #Su tiene cabezeras solamente le pasamos la url

#df.head(cantidad), Se utiliza para leer los encabezados con la definida
#df.tail(Cantidad), Se utiliza para mostrar los ultimos datos de la base






#Para definir nombre de las columnas en caso de que no esten definidos
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", 
           "num-of-doors","body-style", "drive-wheels","engine-location","wheel-base", 
           "length","width","height","curb-weight","engine-type", "num-of-cylinders", 
           "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
            "peak-rpm","city-mpg","highway-mpg","price"]

df.columns = headers #aca a la base de datos leida se le asignan los nombres a las columnas
#En este caso se le asigna headers 



#Para exportar los datos con los headers o las modificaciones
#(excel,csv,json,sql,etc..)

path = "C:\datos\datos.xlsx" 
#Al final del path se coloca el nombre de como queremos guardar el archivo, es muy importante colocar bien el tipo de dato y tener la libreria de exportación

df.to_excel(path) 
#Aca decimos que queremos sacar los datos de la url a excel, y le pasamos 
#el directorio donde queremos que se guarde



#Para mirar los tipos de datos de las columnas

#df.dtypes

#Object o String: Numbers and strings
#int64 o int: Numeric Characters
#float64 o float: Numeric characters with decimals
#datetime64, timedelta[ns]: time data



#Resumen estadistico de cada columna

df.describe()
df.info()

# Count: Terminos en la columna
# Mean: Valor promedio de la columna
# Std: desviacion de los datos de la columna
# Min: Valor minimo encontrado en la columna
# 25%: Limites de los Cuartiles
# 50%: Limites de los Cuartiles
# 75%: Limites de los Cuartiles
# Max: Valor maximo encontrado en la columna


