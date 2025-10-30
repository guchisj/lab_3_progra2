def generar_pares():
    """Genera los primeros 10 números pares usando yield."""
    for i in range(10):
        yield i * 2  # Genera el número par

# Recorremos el generador con un for
for numero in generar_pares():
    print(numero)
