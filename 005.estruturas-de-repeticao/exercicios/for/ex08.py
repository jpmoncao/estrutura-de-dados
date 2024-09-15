'''
18. (FOR) Escreva um programa em C para verificar se um ano fornecido pelo usuário é bissexto ou não.
'''

ano = int(input('Insira um ano: '))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print('Ano bissexto')
else:
    print('Ano não é bissexto')
