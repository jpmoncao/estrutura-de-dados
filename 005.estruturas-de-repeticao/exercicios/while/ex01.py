'''
1. (WHILE) Escreva um algoritmo que calcule a média aritmética das 3 notas dos alunos de uma classe. O algoritmo deverá ler, além das notas, o código do aluno e deverá ser encerrado quando o código for igual a zero.
'''

print('========== MÉDIA ARITMÉTICA ==========')

numero = -1
soma = 0
contador = 0

while (numero != 0):
    if contador <= 2:
        numero = int(input('Digite um número (0 para sair): '))

        soma += numero
        contador += 1
    else:
        print(f'↳ Média aritmética: {soma / contador:.2f}')
        print('==================================')

        soma = 0
        contador = 0
else:
    print('==================================')
