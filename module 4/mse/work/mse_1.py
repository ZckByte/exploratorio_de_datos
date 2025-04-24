import pandas as pd
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot
path= "C:/Code/exploratorio_de_datos/csv,xlsx,etc"
datos = {
    'estudiante': ['Lucía', 'Tomás', 'Sofía', 'Mateo', 'Valentina', 'Joaquín'],
    'horas_estudio': [2, 4, 1, 5, 3, 6],
    'nota_final': [60, 70, 55, 80, 65, 85]
}

df = pd.DataFrame(datos)

X = df[['horas_estudio']]
y = df[['nota_final']]

from sklearn.linear_model import LinearRegression

modelo = LinearRegression()
modelo.fit(X,y)

y_pred = modelo.predict(X)

mse = mean_squared_error(y,y_pred)
r2 = modelo.score(X,y)

print(f'MSE : {mse}')
print(f'R2: {r2}')




df.to_csv(f'{path}/mse_1.csv')


