'''
4. Contagem de Ocorrências
Peça ao usuário para inserir uma frase. Em seguida, transforme a frase em uma lista de palavras e conte quantas vezes a palavra "Python" aparece.
'''

frase = input('Insira uma frase: ')

lista_frases = frase.split(' ')

print(f'Há {len(lista_frases)} palavras na frase, sendo "Python" {str(lista_frases.count('Python'))} dessas')
