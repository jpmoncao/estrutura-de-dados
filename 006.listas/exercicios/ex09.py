'''
9. Listas de Listas (Matriz)
Crie uma matriz 3x3 (lista de listas) e preencha-a com números inteiros fornecidos pelo usuário. Em seguida, exiba a soma de cada linha.
'''

matriz = []

for linha in range(0,3):
    matriz.append([])
    for coluna in range(0,3):
        num = int(input(f'Digite o número [{linha + 1}x{coluna + 1}]: '))
        matriz[linha].append(num)

print('-=' * 4, end=' ')
print('MATRIZ', end=' ')
print('-=' * 4)

for linha in range(0,3):
    print(f' Soma {linha + 1}: {sum(matriz[linha])}', end='   ') 
    print('|', end=' ')
    for coluna in range(0,3):
        print(matriz[linha][coluna], end=' ')
    print('|')
