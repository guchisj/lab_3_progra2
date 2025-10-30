# Lista de temperaturas en Celsius
celsius = [0, 10, 20, 30]

# Usando map() con lambda para convertir a Fahrenheit
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

# Mostrar resultado
print("Temperaturas en Fahrenheit:", fahrenheit)  
