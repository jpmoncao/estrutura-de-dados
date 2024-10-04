'''Exercício 3: Alterne maiúsculas e minúsculas
Seu objetivo é criar uma função que alterne entre letras maiúsculas e minúsculas em uma cadeia de caracteres, começando com uma letra maiúscula. Isso significa que você precisará alternar as maiúsculas e minúsculas de cada letra na cadeia de caracteres de entrada, começando com uma letra maiúscula.

Para concluir este exercício com êxito:

Defina uma função que receba uma string como entrada.
Implemente um método para alternar as maiúsculas e minúsculas de cada letra na string.
Retorne a string modificada como a saída da função.'''

def alternar_maiusculas_minusculas(string):
    arr_palavras_alternadas = []
    arr_palavras = string.strip().split()

    for palavra in arr_palavras:
        palavra_alternada = ''
        
        for index, letra in enumerate(palavra, 0):
            if index % 2 == 0:
                palavra_alternada += letra.upper()
            else:
                palavra_alternada += letra.lower()

        arr_palavras_alternadas.append(palavra_alternada)

    return ' '.join(arr_palavras_alternadas)
    
frase = input('Frase: ')
print(alternar_maiusculas_minusculas(frase))
