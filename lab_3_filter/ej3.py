# Lista de números
numeros = [10,60,30,80,50,100]

# Usando filter() con lambda para obtener solo los números mayores a 50
mayores_50 = list(filter(lambda x: x > 50, numeros))

# Mostrar resultado
print("Números mayores a 50:", mayores_50) 
