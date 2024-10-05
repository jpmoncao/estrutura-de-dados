'''Exercício 3: Procure uma palavra em um arquivo
Crie uma função que leia um arquivo e verifique se uma determinada palavra está presente, retornando quantas vezes ela aparece. Sua tarefa é definir uma função que recebe um nome de arquivo e uma palavra como entrada e, em seguida, verifica se a palavra está presente no arquivo, retornando o número de ocorrências.

Para concluir este exercício:

Defina uma função que receba o nome do arquivo e uma palavra como entrada.
Implemente um método para ler o arquivo e verificar a presença da palavra fornecida.
Retorna o número de ocorrências da palavra como a saída da função.'''

def verificar_palavra_no_arquivo(nome_arquivo, palavra):
    lista = []
    with open(nome_arquivo+'.txt', 'r') as arquivo:
        lista = arquivo.readlines()

    count = 0
    if palavra in lista:
       count += lista.count(palavra)
    if palavra+'\n' in lista:
       count += lista.count(palavra+'\n')
    
    return count

nome_arquivo = input('Nome do arquivo: ')
palavra = input('Palavra: ')
print(verificar_palavra_no_arquivo(nome_arquivo, palavra))
