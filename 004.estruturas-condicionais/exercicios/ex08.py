'''
Tarefa 8: Classificando Inteiros Positivos
Escreva um algoritmo que leia três inteiros positivos (A, B, C) e os mostre em ordem decrescente.

Para concluir esta tarefa:
Leia os valores de A, B e C.
Classifique os valores em ordem decrescente.
Exiba os valores classificados.
'''

a = int(input('Digite o valor A: '))
b = int(input('Digite o valor B: '))
c = int(input('Digite o valor C: '))

if a < 0 or b < 0 or c < 0:
    print('Número inválido!')
else:
    maior = a
    menor = a
    meio = a
    
    if b > maior:
        meio = maior
        maior = b

    if c > maior:
        meio = maior
        maior = c

    if b < menor:
        meio = menor
        menor = b

    if c < menor:
        meio = menor
        menor = c

    print(maior, meio, menor, sep=', ')
