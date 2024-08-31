'''
Tarefa 1: Encontrar o maior valor
Você precisa desenvolver um algoritmo que leia 3 valores (a, b, c) e identifique o maior valor entre eles. Depois de encontrar o maior valor, anote-o junto com a mensagem "É o maior".

Para concluir esta tarefa:

Comece lendo os valores de a, b e c.
Compare os valores para encontrar o maior.
Assim que o maior valor for identificado, anote-o com a mensagem especificada.
'''

a = int(input('Digite o valor a: '))
maior = a

b = int(input('Digite o valor b: '))
if (maior < b):
    maior = b

c = int(input('Digite o valor c: '))
if (maior < c):
    maior = c

resposta = f'{maior} é o maior.'
print(resposta)
