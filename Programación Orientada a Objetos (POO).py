# clima_oo.py

class ClimaDiario:
    def __init__(self):
        # Inicializar una lista vacía para almacenar las temperaturas
        self.temperaturas = []

    def ingresar_temperatura(self, temperatura):
        # Agregar una nueva temperatura a la lista
        self.temperaturas.append(temperatura)

    def calcular_promedio_semanal(self):
        total = sum(self.temperaturas)  # Sumar todas las temperaturas
        promedio = total / len(self.temperaturas)  # Calcular el promedio
        return promedio

# Función principal que organiza el flujo del programa
def main():
    # Crear una instancia de la clase ClimaDiario
    clima = ClimaDiario()
    # Bucle para ingresar la temperatura de cada día de la semana
    for i in range(7):
        temperatura = float(input(f"Ingrese la temperatura para el día {i+1}: "))
        clima.ingresar_temperatura(temperatura)
    # Calcular el promedio semanal usando el método de la clase
    promedio = clima.calcular_promedio_semanal()
    # Mostrar el promedio semanal
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}")

# Ejecutar la función principal si el archivo se ejecuta directamente
if __name__ == "__main__":
    main()
