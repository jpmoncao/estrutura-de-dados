'''Exercício 2: Contando palavras em um arquivo
Sua tarefa é escrever uma função que leia um arquivo de texto e conte quantas palavras estão nele. Isso significa que você precisará ler
o conteúdo do arquivo e contar as palavras presentes no texto.

Para concluir este exercício com êxito:

Defina uma função que usa o nome do arquivo como entrada.
Implemente um método para ler o conteúdo do arquivo e contar as palavras.
Retorne a contagem de palavras como a saída da função.'''

def ler_quantidade_palavras_arquivo(nome_arquivo):
    lista = []
    with open(nome_arquivo+'.txt', 'r') as arquivo:
        lista = arquivo.readlines()
    return len(lista)

nome_arquivo = input('Nome do arquivo: ')
print(ler_quantidade_palavras_arquivo(nome_arquivo))
