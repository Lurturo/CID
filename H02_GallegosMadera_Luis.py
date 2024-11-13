class SimpleLinearRegression:
    def __init__(self, ventas, publicidad):
        # Almacena las observaciones de ventas y publicidad
        self.ventas = ventas
        self.publicidad = publicidad
        self.beta_0 = None
        self.beta_1 = None
        self.calcular_parametros()

    def calcular_parametros(self):
        # Calcula beta_1 y beta_0 usando las fórmulas de regresión lineal simple
        n = len(self.ventas)
        sum_x = sum(self.publicidad)
        sum_y = sum(self.ventas)
        sum_xy = sum(x * y for x, y in zip(self.publicidad, self.ventas))
        sum_x_cuadrada = sum(x**2 for x in self.publicidad)
        
        # Fórmulas para beta_1 y beta_0
        self.beta_1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x_cuadrada - sum_x**2)
        self.beta_0 = (sum_x_cuadrada * sum_y - sum_x * sum_xy) / (n * sum_x_cuadrada - sum_x**2)

    def prediccion(self, x):
        # Realiza una predicción con el modelo
        return self.beta_0 + self.beta_1 * x

    def get_ecuacion_regresion(self):
        # Devuelve la ecuación de regresión como un string
        return f"y = {self.beta_0:.2f} + {self.beta_1:.2f}x"



def run():
    # Datos del Caso Benetton
    ventas = [2, 4, 6, 8, 10, 12, 14, 16, 18]
    publicidad = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Crear una instancia del modelo
    modelo = SimpleLinearRegression(ventas, publicidad)

    # Imprimir la ecuación de regresión
    print("Ecuación de Regresión:", modelo.get_ecuacion_regresion())

    # Solicitar valores para predecir a través de la terminal
    try:
        x_value = float(input("Ingrese un valor de Publicidad para predecir Ventas: "))
        print(f"Predicción de Ventas para Publicidad = {x_value} : {modelo.prediccion(x_value):.2f}")
    except ValueError:
        print("Por favor ingrese un valor numérico.")


# Ejecutar la aplicación
if __name__ == "__main__":
    run()
