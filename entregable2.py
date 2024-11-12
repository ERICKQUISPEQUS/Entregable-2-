import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Generación de datos simulados
np.random.seed(42)
kilometraje = np.random.uniform(10000, 100000, 100)  # Generación de 100 observaciones entre 10,000 y 100,000 km
error = np.random.normal(0, 2000, 100)  # Error con media 0 y desviación estándar de 2000
precio = 50000 - 0.5 * kilometraje + error  # Cálculo del precio con la fórmula dada

# Creación de un DataFrame para almacenar los datos
data = pd.DataFrame({'Kilometraje': kilometraje, 'Precio': precio})

# Separación de las variables predictoras y la variable objetivo
X = data[['Kilometraje']]
y = data['Precio']

# Creación y ajuste del modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X, y)

# Obtención de los coeficientes y el valor R²
print(f"Coeficiente de regresión (pendiente): {modelo.coef_[0]:.4f}")
print(f"Intercepción: {modelo.intercept_:.2f}")
print(f"Valor de R²: {modelo.score(X, y):.4f}")

# Creación del gráfico de dispersión con la línea de regresión
plt.figure(figsize=(10, 6))
plt.scatter(data['Kilometraje'], data['Precio'], color='blue', label='Datos observados')
plt.plot(data['Kilometraje'], modelo.predict(X), color='red', label='Línea de regresión')
plt.xlabel('Kilometraje (km)')
plt.ylabel('Precio ($)')
plt.title('Regresión Lineal: Relación entre Kilometraje y Precio')
plt.legend()
plt.grid(True)
plt.show()

# Predicciones para kilometrajes específicos
kilometrajes_nuevos = np.array([20000, 50000, 80000]).reshape(-1, 1)
precios_predichos = modelo.predict(kilometrajes_nuevos)

# Impresión de las predicciones
for km, precio in zip(kilometrajes_nuevos, precios_predichos):
    print(f"El precio predicho para un automóvil con {km[0]} km es: ${precio:.2f}")