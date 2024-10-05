'''Exercício 7: Contando ocorrências de uma letra
Escreva uma função que conte quantas vezes uma determinada letra aparece em uma string. Sua tarefa é criar uma função que usa uma string e uma letra como entrada e, em seguida, conta as ocorrências da letra fornecida na string.

Para concluir este exercício:

Defina uma função que receba uma string e uma letra como entrada.
Implemente um método para contar as ocorrências da letra fornecida na string.
Retorne a contagem de ocorrências como a saída da função.'''

def quantidade_letras(string, letra):
    return string.count(letra)

frase = input('Frase: ')
letra = input('Letra: ')
print(quantidade_letras(frase, letra))
