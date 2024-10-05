'''Exercício 1: Escrever e ler strings em um arquivo
Para este exercício, você precisa criar uma função que grava uma lista de cadeias de caracteres em um arquivo, com cada cadeia de caracteres em uma linha separada e, em seguida, lê o arquivo, retornando as linhas como uma lista.

Para realizar esta tarefa:

Defina uma função que receba uma lista de strings como entrada.
Implemente um método para gravar as strings em um arquivo, com cada string em uma linha separada.
Crie outra função para ler o arquivo e retornar as linhas como uma lista.'''

def grava_lista_arquivo(lista):
    with open('arquivo.txt', 'w+') as arquivo:
        for linha in lista:
            arquivo.write(f'{linha}\n')

lista = []
while True:
    frase = input('Frase [vazio para parar]: ')
    if frase.strip() == '':
        break
    lista.append(frase.strip())

grava_lista_arquivo(lista)
