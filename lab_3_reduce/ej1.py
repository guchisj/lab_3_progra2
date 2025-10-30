from functools import reduce

# Lista de números
numeros = [5, 10, 15, 20]

# Usando reduce() para sumar todos los elementos
suma_total = reduce(lambda a, b: a + b, numeros)

# Mostrar resultado
print("Suma de todos los elementos:", suma_total)  
