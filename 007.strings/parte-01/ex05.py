'''Exercício 5: Verifique o anagrama
Neste exercício, sua tarefa é criar uma função que verifica se duas cadeias de caracteres de entrada são anagramas uma da outra. Anagramas são palavras ou frases que contêm os mesmos caracteres, mas em uma ordem diferente.

Para concluir este exercício:

Defina uma função que receba duas strings como entrada.
Implemente um método para verificar se as duas strings são anagramas uma da outra.
Retorna um valor booleano indicando se as strings são anagramas.
'''

def comparar_anagramas(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()

    if string1 == string2:
        return False
    
    if len(string1) != len(string2):
        return False

    arr_string1 = [letra for letra in string1]
    arr_string2 = [letra for letra in string2]

    arr_string1.sort()
    arr_string2.sort()
    
    return arr_string1 == arr_string2

frase1 = input('Frase 1: ')
frase2 = input('Frase 2: ')
print(comparar_anagramas(frase1, frase2))
