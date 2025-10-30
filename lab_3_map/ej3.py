# Lista de palabras
palabras = ["uno", "dos", "tres"]

# Usando map() con lambda para obtener la longitud de cada palabra
longitudes = list(map(lambda palabra: len(palabra), palabras))

# Mostrar resultado
print("Longitud de cada palabra:", longitudes)  
