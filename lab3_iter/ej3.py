class CuadradosLista:
    def obtener_cuadrados(self):
        return [i**2 for i in range(1, 11)]

# Uso
cuadrados = CuadradosLista()
print(cuadrados.obtener_cuadrados())
