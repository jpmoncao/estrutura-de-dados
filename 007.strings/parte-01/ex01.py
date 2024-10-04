'''Exercício 1: Substituir caracteres em uma cadeia de caracteres
Sua tarefa é escrever uma função que recebe uma string como entrada e substitui todos os espaços por hífens ('-'). Isso significa que, se a string de entrada contiver espaços, eles deverão ser substituídos por hífens.

Para concluir este exercício:

Defina uma função que usa uma string como argumento.
Use técnicas de manipulação de strings para substituir todos os espaços por hífens.
Retorne a string modificada como a saída da função.'''

def substituir_espacos_por_hifen(string):
    return string.strip().replace(' ', '-')

frase = input('Frase: ')
print(substituir_espacos_por_hifen(frase))
