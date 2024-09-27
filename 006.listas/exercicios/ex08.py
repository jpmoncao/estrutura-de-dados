'''
8. Busca e Índices
Peça ao usuário para inserir uma lista de 10 números. Em seguida, pergunte um número e retorne o índice desse número na lista. Caso o número não esteja presente, exiba uma mensagem apropriada.
'''
numeros = []

for c in range(0, 10):
    numero = int(input(f'Digite o {c+1}º número: '))
    numeros.append(numero)

print('-=' * 15)
numero_busca = int(input('Digite um número para achar índice: '))

if numero_busca in numeros:
    numero_indice = numeros.index(numero_busca)
    print(f'O número está no índice {numero_indice}')
else:
    print('Número não está na lista!')
