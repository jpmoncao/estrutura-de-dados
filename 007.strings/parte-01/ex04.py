'''Exercício 4: Encontre a palavra mais longa
Para este exercício, você deve escrever uma função que localize e retorne a palavra mais longa em uma determinada frase. Você precisará identificar a palavra mais longa na frase de entrada e retorná-la como a saída da função.

Para realizar esta tarefa:

Defina uma função que recebe uma frase como entrada.
Implemente um método para identificar a palavra mais longa da frase.
Retorne a palavra mais longa como a saída da função.'''

def palavra_mais_longa(string):
    palavras = string.strip().split()
    maior_palavra = frase[0]

    for palavra in palavras[1::]:
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra
    return maior_palavra

frase = input('Frase: ')
print(palavra_mais_longa(frase))
