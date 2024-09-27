'''
5. Ordenação
Crie uma lista de números inteiros aleatórios. Organize a lista em ordem crescente e depois em ordem decrescente. Use os métodos oferecidos pela linguagem.
'''

import random

numeros = []
for numero in range(1,20,2):
    numeros.append(numero)
random.shuffle(numeros)

print('Números: ', end='')
print(numeros)

print('Ordem crescente: ', end='')
numeros.sort()
print(numeros)

print('Ordem descrescente: ', end='')
numeros.sort(reverse=True)
print(numeros)
