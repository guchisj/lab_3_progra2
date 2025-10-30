from functools import reduce

# Lista de números
numeros = [7, 3, 9, 1, 5]

# Usando reduce() para encontrar el número mayor
mayor_numero = reduce(lambda a, b: a if a > b else b, numeros)

# Mostrar resultado
print("Número mayor de la lista:", mayor_numero)  
