from functools import reduce

# Lista de cadenas
cadenas = ["Hola", " ", "Mundo", "!"]

# Usando reduce() para concatenar todas las cadenas
resultado = reduce(lambda a, b: a + b, cadenas)

# Mostrar resultado
print("Concatenación de todas las cadenas:", resultado) 
