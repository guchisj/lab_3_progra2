class Mayusculas:
    def __init__(self, lista):
        self.lista = lista
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.lista):
            raise StopIteration
        resultado = self.lista[self.index].upper()
        self.index += 1
        return resultado

# Uso
frases = ["hola", "mundo", "python"]
for palabra in Mayusculas(frases):
    print(palabra)
