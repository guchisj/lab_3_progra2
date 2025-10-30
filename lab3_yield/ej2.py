def generar_impares(numeros):
    """Genera solo los números impares de una lista usando yield."""
    for n in numeros:
        if n % 2 != 0:  # Verifica si el número es impar
            yield n

# Ejemplo de uso:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for impar in generar_impares(lista):
    print(impar)
