# Lista de palabras
palabras = ["perro","gato","pato","hamster"]

# Usando filter() con lambda para palabras que empiezan con "p"
palabras_p = list(filter(lambda palabra: palabra.startswith("p"), palabras))

# Mostrar resultado
print('Palabras que empiezan con "p":', palabras_p) 