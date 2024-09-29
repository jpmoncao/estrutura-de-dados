'''
3. Implementação de Algoritmos de Ordenação
Implemente o algoritmo de bubble sort em uma função que recebe uma lista de números inteiros e ordena-a em ordem crescente. Teste a função com uma lista gerada aleatoriamente. Além disso, conte e imprima quantas trocas foram realizadas durante o processo de ordenação.
'''

from random import sample

def bubble_sort(lista_numeros):
    numeros = lista_numeros[:]
    numeros_ordenados = []
    numero_anterior = 0

    for index, numero in enumerate(numeros, 0):
        if index == 0:
            numeros_ordenados.append(numero)
            numero_anterior = numero
        else:
            if numero > numero_anterior:
                numeros_ordenados.append(numero)
                numero_anterior = numero
            else:
                contador = index

                while True:
                    contador -= 1
                    if numeros_ordenados[contador] <= numero:
                        contador += 1
                        break
                    if contador < 0:
                        contador = 0
                        break

                numeros_ordenados.insert(contador, numero)
                numero_anterior = numeros_ordenados[index]
    return numeros_ordenados

numeros = sample(range(1, 11), 5)

print(numeros)
print(bubble_sort(numeros))
