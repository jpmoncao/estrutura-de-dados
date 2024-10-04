'''Exercício 2: Contagem de palavras
Neste exercício, você precisa criar uma função que conte o número de palavras em uma determinada cadeia de caracteres. Isso significa que você terá que identificar e contar as palavras individuais na string de entrada.

Para realizar esta tarefa:

Defina uma função que receba uma string como entrada.
Implemente um método para contar as palavras na string.
Retorne a contagem de palavras como a saída da função.'''

def quantidade_palavras_na_frase(string):
    return len(string.strip().split())

frase = input('Frase: ')
print(quantidade_palavras_na_frase(frase))
