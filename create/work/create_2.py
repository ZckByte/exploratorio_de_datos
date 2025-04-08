#Dataframe con variables desde 0
import pandas as pd
import os
import time
path = "C:/datos/csv,xlsx,etc"
print("....Dataframe....")
lista_nombres = []
lista_notas = []
while True:
    try:
        cantidad = int(input("Ingrese la cantidad de datos: "))
        for i in range (cantidad):
            nombre = str(input(f"Ingrese el nombre #{i+1}: "))
            lista_nombres += [nombre]
            nota = float(input(f"Ingrese la nota de la persona #{i+1}: "))
            lista_notas += [nota]
        break;
    except:
        print("Ocurrio un error, intenta de nuevo.")
        time.sleep(2)
        os.system('cls')
        continue;
print(lista_nombres, lista_notas)
datos = {
    'nombres': lista_nombres,
    'notas': lista_notas
}
print(datos)
df_notas = pd.DataFrame(datos)
df_notas.to_csv(f'{path}/notas.csv', index=False)