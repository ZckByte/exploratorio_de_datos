#Creacion dataframe 3
# 🎯 Ejercicio: Registro de estudiantes por materias y cálculo de promedio general
# 📌 Instrucciones:
# Pídele al usuario cuántos estudiantes desea ingresar.
# Por cada estudiante:
# Pide su nombre. ✅
# Pide su nota en 3 materias: Matemáticas, Historia y Ciencias. ✅
# Crea un DataFrame con los siguientes campos: ✅
# nombre, matematicas, historia, ciencias, promedio ✅
# Calcula el promedio por estudiante. ✅
# Filtra y muestra solo los estudiantes con promedio mayor o igual a 4.0.
# Guarda el archivo como estudiantes_promedios.csv.
import pandas as pd
from os import system
from time import sleep
path = "C:/datos/csv,xlsx,etc"
lista_nombres= []
lista_matematicas= []
lista_historia= []
lista_ciencias= []
system('cls')
print("....Promedio Dataframe....")
cantidad = int(input("Ingrese la cantidad de estudiantes: "))
while True:
    try:
        for i in range(cantidad):
            nombre = input(f"Nombre del estudiante #{i+1}: ")
            lista_nombres += [nombre]   
            matematicas = float(input("\nNota Matematicas: "))
            lista_matematicas += [matematicas]
            ciencias = float(input("\nNota Ciencias: "))
            lista_ciencias += [ciencias]
            historia = float(input("\nNota Historia: "))
            lista_historia += [historia]
            print(f"\nRegistro exitoso del estudiante #{i+1}")
            sleep(2)
            system('cls')
        break;
    except:
        print("Algo ocurrio, Intente de nuevo.")
        sleep(2)
        system('cls')
        continue;
datos = {
    'nombre': lista_nombres,
    'matematicas': lista_matematicas,
    'ciencias': lista_ciencias,
    'historia': lista_historia
}
df_registro = pd.DataFrame(datos)
df_registro['promedio'] = df_registro[['matematicas', 'ciencias', 'historia']].mean(axis=1)
df_registro.to_csv(f'{path}/registro.csv')

df = pd.read_csv(f'{path}/registro.csv')
df_filtrado = df[df['promedio'] >= 4]

print(df_filtrado)
