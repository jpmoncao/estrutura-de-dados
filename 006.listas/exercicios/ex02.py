'''
2. Inserção de Elementos
Peça ao usuário que insira 5 nomes e armazene-os em uma lista chamada nomes. Em seguida, adicione um nome ao início e outro ao final da lista.
'''
nomes = []

for c in range(0, 5):
    nome = input(f'Insira o {c+1}º nome: ')
    nomes.append(nome)

nomes.insert(0, 'Ínicio')
nomes.append('Fim')

print('Nomes: ' + ', '.join(nomes))
