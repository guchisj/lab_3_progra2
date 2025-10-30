class Cuadrados:
    def __iter__(self):
        """Genera los cuadrados de los números del 1 al 10."""
        for i in range(1, 11):
            yield i ** 2  # Genera el cuadrado de i

# Ejemplo de uso:
for numero in Cuadrados():
    print(numero)
