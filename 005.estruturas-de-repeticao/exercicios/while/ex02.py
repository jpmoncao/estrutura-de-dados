'''
2. (WHILE) Escreva um algoritmo que calcule a média dos números digitados pelo usuário, se eles forem pares. Termine a leitura se o usuário digitar zero (0).
'''


print('======== MÉDIA ARITMÉTICA (PARES) ========')

numero = -1
soma = 0
contador = 0
apenas_pares = True

while (numero != 0):
    if contador <= 2:
        numero = int(input('Digite um número par (0 para sair): '))

        if numero % 2 != 0: 
            apenas_pares = False

        soma += numero
        contador += 1
    else:
        if (apenas_pares):
            print(f'↳ Média aritmética: {soma / contador:.2f}')
        else:
            print('↳ Digite apenas números pares!')
        print('======================================')

        soma = 0
        contador = 0
        apenas_pares = True
else:
    print('======================================')