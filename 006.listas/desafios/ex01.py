'''1. Manipulação de Dados em uma Lista de Dicionários
Crie uma lista de dicionários chamada alunos para armazenar informações sobre 5 alunos, contendo nome, idade e nota. Exemplo: {"nome": "João", "idade": 21, "nota": 8.5}. Escreva um código que:
a) Liste todos os alunos com nota maior ou igual a 7.
b) Calcule a média de notas de todos os alunos.
c) Encontre o aluno mais velho e o mais novo.'''

alunos = []

for i in range(5):
    aluno = {}
    print(f'=== {i+1} ALUNO ===')

    nome = input('Nome: ')
    idade = int(input('Idade: '))
    nota = -1
    while nota not in range(0, 11):
        nota = float(input('Nota: '))

    aluno['nome'] = nome
    aluno['idade'] = idade
    aluno['nota'] = nota

    alunos.append(aluno)

notas_maiores_sete = [aluno['nome'] for aluno in alunos if aluno['nota'] >= 7]
if len(notas_maiores_sete) > 0:
    print('==== NOTAS >= 7 ====')
    print(notas_maiores_sete)

notas = [aluno['nota'] for aluno in alunos]
print('==== MÉDIA ====')
print(f'{sum(notas)/len(notas):.2f}')

maior_idade = max([aluno['idade'] for aluno in alunos])
print('==== MAIOR ====')
print(maior_idade)

menor_idade = min([aluno['idade'] for aluno in alunos])
print('==== MENOR ====')
print(menor_idade)