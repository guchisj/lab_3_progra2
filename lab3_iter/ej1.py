contador = iter(range(10, 16))  # Genera los números del 10 al 15

print(next(contador))  # 10
print(next(contador))  # 11
print(next(contador))  # 12
print(next(contador))  # 13
print(next(contador))  # 14
print(next(contador))  # 15
# Si llamas next(contador) otra vez, dará StopIteration
