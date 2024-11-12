# Cargar librerías necesarias
library(ggplot2)

# Generación de datos simulados
set.seed(42)
kilometraje <- runif(100, 10000, 100000)  # Generación de 100 observaciones entre 10,000 y 100,000 km
error <- rnorm(100, mean = 0, sd = 2000)  # Error con media 0 y desviación estándar de 2000
precio <- 50000 - 0.5 * kilometraje + error  # Cálculo del precio con la fórmula dada

# Crear un DataFrame
data <- data.frame(Kilometraje = kilometraje, Precio = precio)

# Ajustar el modelo de regresión lineal
modelo <- lm(Precio ~ Kilometraje, data = data)

# Ver el resumen del modelo
summary(modelo)

# Coeficientes del modelo
coef(modelo)

# Gráfico de dispersión con la línea de regresión
ggplot(data, aes(x = Kilometraje, y = Precio)) +
  geom_point(color = 'blue') +
  geom_smooth(method = 'lm', color = 'red') +
  labs(title = 'Regresión Lineal: Relación entre Kilometraje y Precio', 
       x = 'Kilometraje (km)', 
       y = 'Precio ($)') +
  theme_minimal()

# Predicciones para kilometrajes específicos
kilometrajes_nuevos <- c(20000, 50000, 80000)
precios_predichos <- predict(modelo, newdata = data.frame(Kilometraje = kilometrajes_nuevos))

# Imprimir predicciones
for (i in 1:length(kilometrajes_nuevos)) {
  cat(sprintf("El precio predicho para un automóvil con %d km es: $%.2f\n", kilometrajes_nuevos[i], precios_predichos[i]))
}
