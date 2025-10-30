from functools import reduce

# Lista de números
numeros = [2, 3, 4]

# Usando reduce() para multiplicar todos los elementos
producto_total = reduce(lambda a, b: a * b, numeros)

# Mostrar resultado
print("Producto de todos los elementos:", producto_total)  
