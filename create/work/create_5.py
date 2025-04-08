# 🎯 Ejercicio Avanzado: Registro de citas médicas y cálculo de estadísticas por mes
# 📌 Instrucciones:

# Crea un DataFrame directamente con pandas con los siguientes campos para 8 citas médicas:

# paciente (nombre) ✅
# fecha (en formato año-mes-día, por ejemplo: "2025-04-10")✅
# especialidad (ej: "Cardiología", "Dermatología", "Pediatría", etc.)✅
# costo (valor pagado por la cita)✅

# Convierte la columna fecha a tipo datetime.✅
# Agrega una nueva columna llamada mes que contenga solo el mes (por nombre o número) de la cita.
# Agrupa los datos por mes y calcula el total recaudado (suma de los costos) por cada mes.
# Filtra y muestra solo las citas con costo mayor a 80,000.
# Guarda el DataFrame original como citas_medicas.csv.

import pandas as pd

df = pd.DataFrame({
    'paciente': [],
    'fecha': [],
    'especialidad': [],
    'costo': []
})
print(df.head(5))

while True:
    try:
        for i in range (2):
            nombre = str(input(f"Nombre del paciente #{i+1}: "))
            fecha = input(f"Ingrese la fecha(año-mes-dia) del paciente {1+1}: ")
            especialidad = str(input("Especialidad: "))
            costo = int(input("Ingrese el valor pagado de la cita: "))
            df.loc[len(df)] = [nombre,fecha,especialidad,costo]
            df['fecha'] = pd.to_datetime(df['fecha'])
            df['mes'] = df['fecha'].dt.month
            df.groupby('mes')['costo'].sum()
        break
    except:
        print("Ocurrio algo mal, intente de nuevo.")
        continue

print(df)

df_filtrado = df[df['costo'] > 80000]
print(df_filtrado)