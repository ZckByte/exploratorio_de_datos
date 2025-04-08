# 🎯 Ejercicio: Registro de empleados y cálculo de salario total
# 📌 Instrucciones:
# Pregunta al usuario cuántos empleados va a registrar. ✅
# Por cada empleado:

# Pide su nombre. ✅
# Pide su sueldo base. ✅
# Pide la cantidad de horas extra trabajadas. ✅

# Supón que cada hora extra vale 10.000 pesos.✅

# Crea un DataFrame con las columnas:
# nombre, sueldo_base, horas_extra, sueldo_total✅
# Calcula el sueldo total = sumando el sueldo base más el valor de las horas extra.✅
# Guarda el DataFrame como un archivo CSV: empleados_salario.csv ✅
# Filtra y muestra solo los empleados cuyo sueldo total sea mayor o igual a 2.000.000 pesos. ✅
path = 'C:/datos/csv,xlsx,etc'
import pandas as pd
from time import sleep
from os import system
print('....Empleados....')
cantidad = int(input("Ingrese la cantidad de empleados: "))
lista_nombres = []
lista_horas_extra = []
lista_sueldo_base = []
lista_sueldo_total = []
while True:
    horas_extra = 0 
    sueldo_total = 0
    try:
        for i in range(cantidad):
            nombre=input(f"Nombre del empleado #{i+1}: ")
            sueldo=float(input(f"Sueldo base del empleado #{i+1} (1 = Minimo): "))
            if (sueldo == 1):
                sueldo = 1300000
            extras=float(input(f"Horas extras del empleado #{i+1}: "))
            lista_nombres += [nombre]
            lista_sueldo_base += [sueldo]
            lista_horas_extra += [extras]
            horas_extra = extras * 10000
            sueldo_total = sueldo + horas_extra
            lista_sueldo_total += [sueldo_total]
            print('!Empleado registrado con exito!')
            sleep(2)
            system('cls')
        break
    except:
        print('Algo ocurrio, intente de nuevo.')
        continue
datos = {
    'nombre': lista_nombres,
    'horas_extra': lista_horas_extra,
    'sueldo_base': lista_sueldo_base,
    'sueldo_total': lista_sueldo_total
}

df_empleados = pd.DataFrame(datos)
df_empleados.to_csv(f'{path}/empleados_salario.csv')
#df_empleados['sueldo_total'] = df_empleados['sueldo_base'] + (df_empleados['horas_extra'] * 10000) para hacerse con pandas


df = pd.read_csv(f"{path}/empleados_salario.csv")
df_filtrado = df[df['sueldo_total'] >= 2000000]
print(df_filtrado)
