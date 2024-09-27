'''
7. Filtragem
Crie uma lista de 20 números inteiros aleatórios entre 1 e 100. Gere uma nova lista contendo apenas os números pares.
'''
import random 

numeros_aleatorios_pares = []
numeros_aleatorios = random.sample(range(1, 101), 20)

print(numeros_aleatorios)
for numero in numeros_aleatorios:
    if numero % 2 == 0:
        numeros_aleatorios_pares.append(numero)

print(numeros_aleatorios_pares)
