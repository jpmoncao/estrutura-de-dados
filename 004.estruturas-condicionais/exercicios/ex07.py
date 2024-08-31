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

maior = a
if (b > maior):
    maior = b
if (c > maior):
    maior = c

menor = a
if (b < menor):
    menor = b
if (c < menor):
    menor = c

meio = a
if (b in range(maior,menor)):
    meio = b
if (c in range(maior,menor)):
    meio = c

if (i == 1):
    print(menor, meio, maior, sep=', ')
elif (i == 2):
    print(maior, meio, menor, sep=', ')
elif (i == 3):
    print(menor, maior, meio, sep=', ')
else:
    print('Comando inválido!')
