class Impares:
    def __iter__(self):
        for i in range(1, 21):
            if i % 2 != 0:
                yield i

# Uso con for
for impar in Impares():
    print(impar)
