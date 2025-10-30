# Lista original de números
numeros = [1,2,3,4,5,6,7,8,9,10]

# Usando filter() con lambda para obtener solo los números impares
impares = list(filter(lambda x: x % 2 != 0, numeros))

# Mostrar resultado
print("Números impares:", impares) 
