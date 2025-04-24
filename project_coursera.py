import pandas as pd 
path = "C:/Code/exploratorio_de_datos/kc_house_data.csv"

df = pd.read_csv(path)
print(df.dtypes)

df.drop(['id'], axis=1, inplace=True)
print(df.describe())

zipcode_counts = df['zipcode'].value_counts().to_frame()
zipcode_counts.columns = ['conteo']
zipcode_counts.reset_index(inplace=True)
zipcode_counts.columns = ['zipcode', 'conteo']
print(zipcode_counts.head())

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
sns.boxplot(x='waterfront', y='price', data=df)
plt.title('Precio de casas con o sin vista al mar')
plt.xlabel('Vista al mar (0 = No, 1 = Sí)')
plt.ylabel('Precio')
plt.show()

plt.figure(figsize=(8, 5))
sns.regplot(x='sqft_above', y='price', data=df)
plt.title('Relación entre sqft_above y precio')
plt.xlabel('Metros cuadrados sobre el suelo (sqft_above)')
plt.ylabel('Precio')
plt.show()

from sklearn.linear_model import LinearRegression
X = df[['sqft_living']]  
y = df['price']
modelo = LinearRegression()
modelo.fit(X, y)
r2 = modelo.score(X, y)
print(f'R² con sqft_living: {r2}')

features = [
    'floors', 'waterfront', 'lat', 'bedrooms', 'sqft_basement',
    'view', 'bathrooms', 'sqft_living15', 'sqft_above', 'grade', 'sqft_living'
]
X_multi = df[features]
y = df['price']
modelo_multi = LinearRegression()
modelo_multi.fit(X_multi, y)
r2_multi = modelo_multi.score(X_multi, y)
print(f'R² con múltiples variables: {r2_multi}')

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression

features = [
    'floors', 'waterfront', 'lat', 'bedrooms', 'sqft_basement',
    'view', 'bathrooms', 'sqft_living15', 'sqft_above', 'grade', 'sqft_living'
]
X = df[features]
y = df['price']

pipe = Pipeline([
    ('scale', StandardScaler()),
    ('poly', PolynomialFeatures(degree=2)),
    ('model', LinearRegression())
])

pipe.fit(X, y)
r2_pipeline = pipe.score(X, y)
print(f'R² del pipeline: {r2_pipeline}')

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

features = [
    'floors', 'waterfront', 'lat', 'bedrooms', 'sqft_basement',
    'view', 'bathrooms', 'sqft_living15', 'sqft_above', 'grade', 'sqft_living'
]
X = df[features]
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train_scaled)
X_test_poly = poly.transform(X_test_scaled)

from sklearn.linear_model import Ridge
ridge = Ridge(alpha=0.1)
ridge.fit(X_train_poly, y_train)
r2_ridge_poly = ridge.score(X_test_poly, y_test)
print(f'R² con Ridge y polinomios: {r2_ridge_poly}')
