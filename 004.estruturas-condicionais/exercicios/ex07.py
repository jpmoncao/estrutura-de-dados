'''
Tarefa 7: Classificando valores
Escreva um algoritmo que leia um conjunto de 4 valores (i, a, b, c) e execute ações específicas com base no valor de i.

Para concluir esta tarefa:

Leia os valores de i, a, b e c.
Com base no valor de i, execute a ação correspondente:
Se i = 1, escreva os três valores a, b, c em ordem crescente.
Se i = 2, escreva os três valores a, b, c em ordem decrescente.
Se i = 3, organize os valores a, b, c de modo que o valor mais alto fique entre os outros dois.
'''

a = int(input('Digite a:'))
b = int(input('Digite b:'))
c = int(input('Digite c:'))

i = int(input('''
======== COMANDOS ========
    1) Ordem crescente
    2) Ordem decrescente
    3) Mais alto no meio
'''))

meio = a

maior = a
if (b > maior):
    meio = maior
    maior = b
if (c > maior):
    meio = maior
    maior = c

menor = a
if (b < menor):
    meio = menor
    menor = b
if (c < menor):
    meio = menor
    menor = c

if (i == 1):
    print(menor, meio, maior, sep=', ')
elif (i == 2):
    print(maior, meio, menor, sep=', ')
elif (i == 3):
    print(menor, maior, meio, sep=', ')
else:
    print('Comando inválido!')
