#Para crear dataframes

#Se importa pandas

import pandas as pd

#Luego se define un diccionario o array

#Se guardan los datos
datos = {
    'persona': ['Pepe', 'Juan', 'Santiago'],
    'dinero': [2000, 3000, 4000],
    'edad': [14, 16, 20]
    #Cabezera, #Datos
}

#Se guarda en una variable junto con pandas que convertira
#El diccionario a dataframe
df_personas = pd.DataFrame(datos)

#Lo convierte en dataframe, y se espeficica la ruta
path = "C:\datos\csv,xlsx,etc"
df_personas.to_csv(f'{path}\personas.csv', index=False) #Index = false, es para que no agregue un indice en el df

#Leer el df
df = pd.read_csv(f'{path}/personas.csv')

#Para consultar datos espeficicos de una csv o base
#Se tiene una forma que es filtrando el df:
df_filtrado = df[df['dinero'] >= 2500]

#Con .loc()
#Con indice obtiene la fila con el indidice 0
df.loc[0]

#Con el nombre de la columna(imprime la columna)
df.loc[:,'persona'] 

#Con el indice y el nombre de la columna 
df.loc[1, 'persona'] #Juan

#Para asignar datos
df.loc[2, 'persona'] = 'byte' #Asigna el nombre de la fila del indice 2 de persona

#Agregar fila
#(se utiliza len(df) porque cuando se crea una df el indice es 0, por lo que se agregara una fila en el indice 0 y sucesivamente)
df.loc[len(df)] = ['Alan', 3000,17]

#Agregar columnas
df['nueva'] = 'es nueva' #tiene que concordar con la cantidad de indices que tiene el df

print(df.head(5))
