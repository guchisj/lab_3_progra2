def fibonacci():
    """Genera la serie de Fibonacci hasta el décimo elemento usando yield."""
    a, b = 0, 1
    for _ in range(10):
        yield a
        a, b = b, a + b  # Actualiza los dos valores

# Ejemplo de uso:
for num in fibonacci():
    print(num)
